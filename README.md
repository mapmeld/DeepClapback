# DeepClapback

## Running with cloud services
- sudo apt-get install python3-pip postgresql-client-10 postgresql-client-common
- cd /mnt/DISK
- bzip -d /mnt/DISK/reddit_data/year/RC_YEAR-MONTH.bz2
- python3 reddit_json_converter.py
- python3 reddit_comment_sql.py

```sql
CREATE TABLE common_clapbacks_2016_01 AS (
  SELECT LOWER(TRIM(body)), COUNT(*)
  FROM comments_2016_01
  WHERE is_clapback = TRUE
  GROUP BY LOWER(TRIM(body))
  ORDER BY COUNT(*) DESC
  LIMIT 100
);

CREATE TABLE all_clapbacks_2016_01 AS (
  SELECT body, score, plainparent, yyyymm, ''::text AS parent_body
  FROM comments_2016_01
  WHERE is_clapback = TRUE
  AND LOWER(TRIM(body)) IN (
    SELECT lower FROM common_clapbacks_2016_01
  )
);

UPDATE all_clapbacks_2016_01 SET parent_body = (
  SELECT body
  FROM comments_2016_01
  WHERE comments_2016_01.id = all_clapbacks_2016_01.plainparent
);
```
