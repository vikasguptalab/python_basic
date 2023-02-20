#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="airlines", user="postgres", password="postgres", host="localhost", port="5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("UPDATE company.flights set name = 'MyAIR' where ID = 1")
conn.commit()
print("Total number of rows updated :", cur.rowcount)

cur.execute("SELECT id, name  from company.flights")
rows = cur.fetchall()
for row in rows:
    print("ID = ", row[0])
    print("NAME = ", row[1])

print("Operation done successfully");
conn.close()