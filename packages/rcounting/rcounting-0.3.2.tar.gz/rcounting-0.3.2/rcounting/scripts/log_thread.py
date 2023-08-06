#! /usr/bin/python3
# encoding=utf8
import os
from pathlib import Path
import pandas as pd
from datetime import datetime
import sqlite3

import rcounting.parsing as parsing
import rcounting.thread_navigation as tn
from rcounting.counters import apply_alias
from rcounting.utils import format_timedelta
from rcounting.reddit_interface import reddit
import rcounting.models as models


def hoc_string(df, title):
    getter = apply_alias(df.iloc[-1]['username'])

    def hoc_format(username):
        username = apply_alias(username)
        return f'**/u/{username}**' if username == getter else f'/u/{username}'

    df['hoc_username'] = df['username'].apply(hoc_format)
    dt = pd.to_timedelta(df.iloc[-1].timestamp - df.iloc[0].timestamp, unit='s')
    table = df.iloc[1:]['hoc_username'].value_counts().to_frame().reset_index()
    data = table.set_index(table.index + 1).to_csv(None, sep='|', header=0)

    header = (f'Thread Participation Chart for {title}\n\nRank|Username|Counts\n---|---|---')
    footer = (f'It took {len(table)} counters {format_timedelta(dt)} to complete this thread. '
              f'Bold is the user with the get\n'
              f'total counts in this chain logged: {len(df) - 1}')
    return '\n'.join([header, data, footer])


def main(args):
    t_start = datetime.now()
    output_directory = Path(args.output_directory)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    if not args.get_id:
        subreddit = reddit.subreddit('counting')
        wiki_page = subreddit.wiki['directory']
        document = wiki_page.content_md.replace("\r\n", "\n")
        result = parsing.parse_directory_page(document)
        comment_id = result[1][1][0][4]
        comment = tn.find_previous_get(reddit.comment(comment_id))
        get_id = comment.id
    else:
        get_id = args.get_id
        comment = reddit.comment(get_id)

    print(f'Logging {"all" if args.all_counts else args.n} '
          f'reddit submission{"s" if args.n > 1 else ""} '
          f'starting at {get_id} and moving backwards')

    last_submission_id = ''
    known_submissions = []
    if args.sql:
        db_file = output_directory / Path(args.filename)
        db = sqlite3.connect(db_file)
        try:
            submissions = pd.read_sql("select * from submissions", db)
            known_submissions = submissions['submission_id'].tolist()
            checkpoints = pd.read_sql("select submission_id from last_submission", db)
            last_submission_id = checkpoints.iat[-1, 0]
        except pd.io.sql.DatabaseError:
            pass
    completed = 0

    def is_already_logged(comment):
        if args.sql:
            return comment.submission.id in known_submissions
        else:
            body = parsing.strip_markdown_links(comment.body)
            basecount = parsing.find_count_in_text(body) - 1000
            hoc_path = output_directory / Path(f'TABLE_{basecount}to{basecount+1000}.csv')
            return os.path.isfile(hoc_path)

    is_updated = False
    while (completed < args.n) or (args.all_counts and comment.submission.id != last_submission_id):
        is_updated = True
        completed += 1
        if not is_already_logged(comment):
            df = pd.DataFrame(tn.fetch_comments(comment, use_pushshift=False))
            df = df[['comment_id', 'username', 'timestamp', 'submission_id', 'body']]
            n = (df['body'].apply(lambda x: parsing.find_count_in_text(x, raise_exceptions=False))
                 - df.index).median()
            basecount = int(n - (n % 1000))
            if args.sql:
                submission = pd.DataFrame([models.Submission(comment.submission).to_dict()])
                submission = submission[['submission_id', 'username', 'timestamp', 'title', 'body']]
                submission['basecount'] = basecount
                df.to_sql('comments', db, index_label='position', if_exists='append')
                submission.to_sql('submissions', db, index=False, if_exists='append')
            else:
                hoc_path = output_directory / Path(f'TABLE_{basecount}to{basecount+1000}.csv')
                hog_path = output_directory / Path(f'LOG_{basecount}to{basecount+1000}.csv')
                if not os.path.isfile(hoc_path):
                    title = comment.submission.title

                    hog_columns = ['username', 'timestamp', 'comment_id', 'submission_id']
                    output_df = df.set_index(df.index + basecount)[hog_columns].iloc[1:]
                    output_df.to_csv(hog_path, header=None)
                    with open(hoc_path, 'w') as f:
                        print(hoc_string(df, title), file=f)
        comment = tn.find_previous_get(comment)

    if is_updated and args.sql and (comment.submission.id == last_submission_id):
        new_submission_id = pd.read_sql("select submission_id "
                                        "from submissions order by basecount", db).iloc[-1]
        new_submission_id.to_sql('last_submisison', db, index=False)

    print(f'Running the script took {datetime.now() - t_start}')
