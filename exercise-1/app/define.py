import sqlite3
import json

def create_and_insert_data_into_sqlite_db(
    db_file: str,
    ddl_query: str,
    dml_query: str,
    data: list[tuple]
) -> None:
    # Create a SQL Lite connection and cursor
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Create/define data schema
    cursor.execute(ddl_query)
    
    # Insert data into the table
    cursor.executemany(dml_query, data)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print(f"Database {db_file} created and data inserted successfully.")

# SQL Lite database
db_file: str = 'scores.db'

# SQL Lite Data Definition Language (DDL)
ddl_query: str = '''
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    scores TEXT,
    date DATE
)
'''

# SQL Lite Data Manipulation Language (DML)
dml_query: str = '''
INSERT INTO scores (id, patient_id, scores, date) 
VALUES (?, ?, ?, ?)
'''

# Prepare the data
data: list[tuple] = [
    (1, 1323, json.dumps({'satisfaction': 9, 'pain': 2, 'fatigue': 2}), '2020-06-25'),
    (2, 9032, json.dumps({'satisfaction': 2, 'pain': 7, 'fatigue': 5}), '2020-06-30'),
    (3, 2331, json.dumps({'satisfaction': 7, 'pain': 1, 'fatigue': 1}), '2020-07-05'),
    (4, 2303, json.dumps({'satisfaction': 8, 'pain': 9, 'fatigue': 0}), '2020-07-12'),
    (5, 1323, json.dumps({'satisfaction': 10, 'pain': 0, 'fatigue': 0}), '2020-07-09'),
    (6, 2331, json.dumps({'satisfaction': 8, 'pain': 9, 'fatigue': 5}), '2020-07-20')
]

create_and_insert_data_into_sqlite_db(db_file, ddl_query, dml_query, data)
