#!/usr/bin/env python

from sqlalchemy import create_engine, text, MetaData, Table
import sqlalchemy
import pandas as pd
import json

# Connect to the database
engine = create_engine("mysql://codetest:swordfish@database/codetest")

conn = engine.connect()

# Load data from CSV files
people_df = pd.read_csv('/data/people.csv')
places_df = pd.read_csv('/data/places.csv')

# Insert data into the places table
places_df.to_sql('places',con=conn, if_exists='append', index=False)

# Insert data into the people table
people_df.to_sql('people', con=conn, if_exists='append', index=False)

conn.close()

with engine.connect() as conn:

    # Find the country summary
    query = text("""SELECT p.country, COUNT(*) AS total_people
    FROM people AS pe
    JOIN places AS p ON pe.place_of_birth = p.city
    GROUP BY p.country;""")

    res = conn.execute(query)
    result = res.fetchall()


# Save to a file
with open('/data/sample_output.json', 'w') as summary:
    json.dump(dict(result),summary)
