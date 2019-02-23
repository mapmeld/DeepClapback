import json
import psycopg2

# pip install psycopg2
# createdb reddit

conn = psycopg2.connect("dbname='reddit' host='localhost'")
cursor = conn.cursor()

#cursor.execute('DROP TABLE IF EXISTS comments')
cursor.execute('CREATE TABLE IF NOT EXISTS comments ( \
    id VARCHAR(20), \
    body TEXT, \
    year INT, \
    score INT, \
    parent_id VARCHAR(20), \
    link_id VARCHAR(20), \
    clapback BOOLEAN, \
    parent_score INT \
)')
cursor.execute('DELETE FROM comments WHERE 1 = 1')
conn.commit()

with open('RC_2010-07', 'r') as allcomments:
    index = 0
    for comment_text in allcomments:
        comment = json.loads(comment_text)
        #cursor.execute('INSERT INTO comments (id, body, year, score, parent_id, link_id) \
        #    VALUES (%s, %s, %s, %s, %s, %s)',
        #    (comment['id'], comment['body'], 2010, comment['score'], comment['parent_id'], comment['link_id']))

        index = index + 1
        if index % 1000 == 0:
            print(index)
            #conn.commit()
#conn.commit()

cursor.execute('\\copy ')
conn.commit()

"""
DROP TABLE IF EXISTS parentsrc;
CREATE TABLE parentsrc AS SELECT * FROM comments;
ALTER TABLE parentsrc DROP COLUMN plainparent;
CREATE INDEX parentid ON parentsrc (id);
CLUSTER parentsrc USING parentid;
ANALYZE parentsrc;

ALTER TABLE comments ADD COLUMN IF NOT EXISTS plainparent VARCHAR(20);
UPDATE comments SET plainparent = SUBSTR(parent_id, 4);

UPDATE comments SET parent_score = (
    SELECT score FROM parentsrc WHERE parentsrc.id = plainparent
)
WHERE plainparent IN (SELECT id FROM comments);

SELECT COUNT(*) FROM comments WHERE score > parent_score;
SELECT COUNT(*) FROM comments WHERE score > parent_score * 1.5;

SELECT COUNT(*), TRIM(LOWER(body))
    FROM comments
    WHERE score > parent_score * 1.5
        AND parent_score > 0
    GROUP BY TRIM(LOWER(body))
    ORDER BY COUNT(*) DESC
    LIMIT 15;
"""
