#!/usr/bin/python3
import mysql.connector

# Establish the connection
cnx = mysql.connector.connect(
  host="localhost",
  user="Brain-Effects",
  password="BraEff9003"
)

# Create a cursor object
cursor = cnx.cursor()

# Execute the SQL command
cursor.execute("SHOW DATABASES")

# Fetch all the rows
databases = cursor.fetchall()

# Print all databases
for database in databases:
  print(database[0])

# Close the cursor and connection
cursor.close()
cnx.close()
