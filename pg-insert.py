#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="airlines", user="postgres", password="postgres", host="localhost", port="5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("INSERT INTO company.flights (NAME) VALUES ('Paul' )");

cur.execute("INSERT INTO company.flights (NAME) VALUES ('Allen')");

conn.commit()
print("Records created successfully");
conn.close()