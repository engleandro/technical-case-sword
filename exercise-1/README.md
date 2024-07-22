# SOLUTION OF EXERCISE 1

The SQL Query to make this operations is defined below as:

```sql
WITH monthly_scores AS (
  SELECT
    strftime('%m', date) AS month_num,
    CASE strftime('%m', date)
      WHEN '01' THEN 'Jan'
      WHEN '02' THEN 'Feb'
      WHEN '03' THEN 'Mar'
      WHEN '04' THEN 'Apr'
      WHEN '05' THEN 'May'
      WHEN '06' THEN 'Jun'
      WHEN '07' THEN 'Jul'
      WHEN '08' THEN 'Aug'
      WHEN '09' THEN 'Sep'
      WHEN '10' THEN 'Oct'
      WHEN '11' THEN 'Nov'
      WHEN '12' THEN 'Dec'
    END AS month,
    patient_id,
    CAST(json_extract(scores, '$.satisfaction') AS INTEGER) AS satisfaction
  FROM scores
)
SELECT 
  month,
  CAST(
    (
    	SUM(CASE WHEN satisfaction > 8 THEN 1 ELSE 0 END)
    	- SUM(CASE WHEN satisfaction < 7 THEN 1 ELSE 0 END)
    ) * 100.0 / COUNT(patient_id) 
  	AS INTEGER
  ) AS NPS
FROM monthly_scores
GROUP BY month_num, month
ORDER BY month_num;
```

To test it locally, you need a simple Python runtime installed in your computer. 

Then, follow the steps:

```bash
# go to the app repository
cd app

# create the local SQL Lite database file (you can change the inserted data in the DML query in the define.py file)
python define.py

# run the query
python query.py
```

The output is a CSV file with schema: Month as a string, NPS as an integer. The result below is based on the inserted data in the file `define.py`:

```
Month,NPS
Jun,0
Jul,25
```