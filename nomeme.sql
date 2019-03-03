ALTER TABLE comments_2016_06 ADD COLUMN bad_meme BOOLEAN;

UPDATE comments_2016_06 SET bad_meme = TRUE
  WHERE score < 0
  AND LOWER(TRIM(body)) IN (
    SELECT lower FROM clapbacks_2016_10
  );

ALTER TABLE comments_2016_06 ADD COLUMN plainparent VARCHAR(20);

UPDATE comments_2016_06 SET plainparent = SUBSTR(parent_id, 4)
  WHERE bad_meme = TRUE;

ALTER TABLE comments_2016_06 ADD COLUMN parent_body TEXT;

CREATE TABLE backup AS (SELECT id, body FROM comments_2016_06);

UPDATE comments_2016_06 SET parent_body = (
  SELECT body FROM backup
  WHERE backup.id = comments_2016_06.plainparent
) WHERE bad_meme = TRUE;

DELETE FROM comments_2016_06 WHERE bad_meme IS NULL;

CREATE TABLE bad_memes AS (
  SELECT body, parent_body
  FROM comments_2016_06
  WHERE bad_meme = TRUE
  AND LENGTH(parent_body) > 0
);
\copy bad_memes TO './bad_memes.csv' CSV;

DROP TABLE comments_2016_06;
DROP TABLE backup;
