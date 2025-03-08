import sqlite3
import csv

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('majors_courses.db')
cursor = conn.cursor()

# Create the table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    major TEXT,
    course TEXT
)
''')

# Commit the changes and close the cursor
conn.commit()

# Open the CSV file and read the data
with open('majors_courses.csv', 'r') as file:
    csv_reader = csv.DictReader(file)  # Read the file as a dictionary (fieldnames are used as keys)
    
    # Loop through each row and insert the data into the SQLite table
    for row in csv_reader:
        cursor.execute('''
        INSERT INTO courses (major, course)
        VALUES (?, ?)
        ''', (row['Major'], row['Course']))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()

print("Data imported successfully into the database!")

# Connect to the database
conn = sqlite3.connect('majors_courses.db')
cursor = conn.cursor()

# Query the data
cursor.execute('SELECT * FROM courses')

# Fetch and print all rows
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()