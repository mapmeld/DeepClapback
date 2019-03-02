import json
import psycopg2

credentials = json.loads(open('credentials.json', 'r').read())

conn = psycopg2.connect("dbname='" + credentials['dbname'] + "' host='" + credentials['host'] + "' user='" + credentials['user'] + "' password='" + credentials['passw'] + "' port='" + str(credentials['port']) + "'")
cursor = conn.cursor()

for y in [2016]:
    year = str(year)
    for m in range(1, 13):
        month = str(m)
        if len(month) == 1:
            month = '0' + month

        cursor.execute('DELETE FROM comments_' + year + '_' + month + ' WHERE body = \'[removed]\' OR body = \'[deleted]\'')
        cursor.execute('CREATE INDEX comments_' + year + '_' + month + '_idx ON comments_' + year + '_' + month + ' (id)')

        cursor.execute('ALTER TABLE comments_' + year + '_' + month + ' ADD yyyymm INT')
        cursor.execute('UPDATE comments_' + year + '_' + month + ' SET yyyymm = ' + year + month + '')
        conn.commit()

        cursor.execute('ALTER TABLE comments_' + year + '_' + month + ' ADD plainparent VARCHAR(20)')
        cursor.execute('UPDATE comments_' + year + '_' + month + ' SET plainparent = SUBSTR(parent_id, 4)')
        cursor.execute('CREATE TABLE comment_ids_' + year + '_' + month + ' AS (SELECT id, score FROM comments_' + year + '_' + month + ')')
            #>x< INSERT INTO comment_ids_2017 (id, score) VALUES (SELECT id, score FROM comments_2017_02);
        cursor.execute('CREATE INDEX idstr' + year + '_' + month + ' ON comment_ids_' + year + '_' + month + ' (id)')
        cursor.execute('CLUSTER comment_ids_' + year + '_' + month + ' USING idstr' + year + '_' + month)
        cursor.execute('ANALYZE comment_ids_' + year + '_' + month)
        conn.commit()

        cursor.execute('ALTER TABLE comments_' + year + '_' + month + ' ADD is_reply BOOLEAN')
        cursor.execute('UPDATE comments_' + year + '_' + month + ' SET is_reply = TRUE WHERE plainparent IN (SELECT id FROM comment_ids_' + year + '_' + month + ')')
        conn.commit()

        cursor.execute('ALTER TABLE comments_' + year + '_' + month + ' ADD parent_score INT')
        cursor.execute('UPDATE comments_' + year + '_' + month + ' SET parent_score = (SELECT score FROM comment_ids_' + year + '_' + month + ' WHERE comment_ids_' + year + '_' + month + '.id = plainparent) WHERE is_reply')
        conn.commit()

        cursor.execute('ALTER TABLE comments_' + year + '_' + month + ' ADD comment_was_better BOOLEAN')
        cursor.execute('UPDATE comments_' + year + '_' + month + ' SET comment_was_better = TRUE WHERE (is_reply = TRUE) AND score > parent_score')

        cursor.execute('ALTER TABLE comments_' + year + '_' + month + ' ADD is_clapback BOOLEAN')
        cursor.execute('UPDATE comments_' + year + '_' + month + ' SET is_clapback = TRUE WHERE (comment_was_better = TRUE) AND score > 7 AND parent_score > 0 AND score > parent_score * 1.5')

        cursor.execute('ALTER TABLE comments_' + year + '_' + month + ' ADD is_relevant_parent BOOLEAN')
        cursor.execute('UPDATE comments_' + year + '_' + month + ' SET is_relevant_parent = TRUE WHERE (comment_was_better IS NULL) AND id IN (SELECT plainparent FROM comments_' + year + '_' + month + ' WHERE comment_was_better = TRUE)')
        conn.commit()

        cursor.execute('DELETE FROM comments_' + year + '_' + month + ' WHERE (comment_was_better IS NULL) AND (is_relevant_parent IS NULL)')
        conn.commit()
