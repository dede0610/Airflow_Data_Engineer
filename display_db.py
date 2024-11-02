"""Pyhton script created to query the weather database"""

import sqlite3

DB_PATH = "./weather_data.db"

def display_db(query, db_path=DB_PATH):

    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch the latest entries in the `weather` table
    cursor.execute(query)

    # Retrieve and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()


query =  """
        SELECT * FROM weather
    """

display_db(query=query)
