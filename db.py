import Mysql.connector

# Establish a connection to the MySQL database
mydb = Mysql.connector.connect(
    host='localhost',
    user='Naresh',
    passwd='nareshhasthi@16'
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute the SQL query to show databases
mycursor.execute('SHOW DATABASES')

# Fetch and print all databases
for database in mycursor:
    print(database)

# Close the cursor and connection
mycursor.close()
mydb.close()
