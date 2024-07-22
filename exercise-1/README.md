# Exercise 1

About once every two weeks, SWORD asks its patients how much they would recommend
its therapy to someone they know on a scale from 0 to 10. Assume you have a table called
Scores having a json string containing (among other things) the satisfaction scores of
SWORD’s patients along with the corresponding date, as follows:

```
| id | patient_id | scores                                        | date       |
|----|------------|-----------------------------------------------|------------|
| 1  | 1323       | {'satisfaction': 9, 'pain': 2, 'fatigue': 2}  | 2020-06-25 |
| 2  | 9032       | {'satisfaction': 2, 'pain': 7, 'fatigue': 5}  | 2020-06-30 |
| 3  | 2331       | {'satisfaction': 7, 'pain': 1, 'fatigue': 1}  | 2020-07-05 |
| 4  | 2303       | {'satisfaction': 8, 'pain': 9, 'fatigue': 0}  | 2020-07-12 |
| 5  | 1323       | {'satisfaction': 10, 'pain': 0, 'fatigue': 0} | 2020-07-09 |
| 6  | 2331       | {'satisfaction': 8, 'pain': 9, 'fatigue': 5}  | 2020-07-20 |
```

One of our most important metrics is the NPS which is calculated with the following formula:

```
NPS = (number of promoters − number of detractors)/number of patients
```
Patients are classified in the following groups according to their most recent satisfaction report:
● > 8 is a promoter
● < 7 is a detractor

Write a SQL query to calculate SWORD’s Digital Therapist NPS for each month. E.g.:

```
| month    | NPS |
| January  | 50  |
| February | 45  |
| March    | 53  |
| ...      | ... |
```

# SOLUTION

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
