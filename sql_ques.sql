SELECT auto_number
FROM our_base
WHERE region = 11 and auto_number IS NOT NULL
ORDER BY rand()
LIMIT 3


SET @a = (SELECT COUNT
(auto_number)
FROM image WHERE auto_number
IS NOT NULL GROUP BY region
= 11 );

CREATE TEMPORARY TABLE temp_
SELECT
@i:
=@i+1 id,
auto_number
FROM our_base,
(SELECT
@i:
=0) X
WHERE region = 11 and auto_number IS NOT NULL;

CREATE TEMPORARY
TABLE tmp
SELECT floor(@a*rand()) id
FROM temp_ LIMIT
3;

SELECT i.auto_number
FROM temp_ i, tmp
WHERE tmp.id = i.id;