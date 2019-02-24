import json, csv

csvout = csv.writer(open("2017_01.csv","w"), quoting=csv.QUOTE_NONNUMERIC, escapechar='\\', quotechar='"')

with open('RC_2017-01', 'r') as allcomments:
    index = 0
    for comment_text in allcomments:
        comment = json.loads(comment_text)
        if comment['body'] != '[deleted]':
            csvout.writerow([ comment['id'], comment['body'].replace('\n', ' '), comment['score'], comment['parent_id'] ])

            # every 10,000 successful rows, print to let us know there's progress
            index = index + 1
            if index % 10000 == 0:
                print(index)


"""
CREATE TABLE IF NOT EXISTS comments_2017_01 (
    id VARCHAR(20),
    body TEXT,
    score INT,
    parent_id VARCHAR(20)
);
\copy comments_2017_01 FROM '2017_01.csv' CSV;
"""
