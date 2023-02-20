#!/usr/bin/python
import logging
import psycopg2
#
# # Connect to your postgres DB
conn = psycopg2.connect(database="airlines", user="postgres", password="postgres", host="localhost", port="5432")


# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.basicConfig(filename='app_error.log', format='%(asctime)s - %(message)s', level=logging.INFO)
logging.warning('This is a Warning')
# logging.info('This is a debug message')

# Open a cursor to perform database operations
cur = conn.cursor()

# cur.execute("INSERT INTO company.flights (NAME) VALUES ('vikasall')");
# cur.execute("INSERT INTO company.flights (NAME) VALUES ('vikasall')");
# cur.execute("INSERT INTO company.flights (NAME) VALUES ('all')");
# conn.commit()

# Execute a query
# cur.execute("SELECT NAME as t  FROM company.flights")

# Retrieve query results
# records = cur.fetchall()
# print(records)
# print('===')

cur.execute("SELECT NAME as t  FROM company.flights")
records = cur.fetchall()

logging.error('%s Record List', records)

print(records)

# for row in records:
#     print(row, " : ")

print("Operation done successfully");

cur.close()
conn.close()