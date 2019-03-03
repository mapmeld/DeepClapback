CREATE TABLE union_clapbacks AS (
  (SELECT body, parent_body FROM all_clapbacks_2017_02 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_text FROM all_clapbacks_2017_03 WHERE parent_text IS NOT NULL)
  UNION (SELECT body, parenttext FROM all_clapbacks_2016_01 WHERE parenttext IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_02 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_03 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_04 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_05 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_06 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_07 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_08 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_09 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_10 WHERE parent_body IS NOT NULL)
  UNION (SELECT body, parent_body FROM all_clapbacks_2016_11 WHERE parent_body IS NOT NULL)
);

\copy union_clapbacks TO 'clapbacks.csv' CSV;
