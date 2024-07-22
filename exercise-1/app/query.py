import sqlite3
import csv

# Calculate the Monthly NPS Scores and write the results to a CSV file
def calc_monthly_nps_scores(db_file: str, csv_file: str, query: str) -> None:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        # Execute the query
        cursor.execute(query)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Write results to CSV file
        with open(csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            
            # Write header
            csv_writer.writerow(['Month', 'NPS'])
            
            # Write data rows
            csv_writer.writerows(results)
        
        print(f"Data has been successfully written to {csv_file}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the database connection
        conn.close()

if __name__ == '__main__':
    # SQLite database file path
    db_file = 'scores.db'

    # Output CSV file path
    csv_file = 'monthly_nps_scores.csv'

    # SQL query
    query = '''
    WITH monthly_scores AS (
    SELECT
        strftime('%m', date) AS month_num,
        CASE strftime('%m', date)
        WHEN '01' THEN 'Jan' WHEN '02' THEN 'Feb' WHEN '03' THEN 'Mar'
        WHEN '04' THEN 'Apr' WHEN '05' THEN 'May' WHEN '06' THEN 'Jun'
        WHEN '07' THEN 'Jul' WHEN '08' THEN 'Aug' WHEN '09' THEN 'Sep'
        WHEN '10' THEN 'Oct' WHEN '11' THEN 'Nov' WHEN '12' THEN 'Dec'
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
    '''
    
    calc_monthly_nps_scores(db_file, csv_file, query)
