#!/usr/bin/python

fileNameCSV = "tmp/techcrunch.csv"

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result


# csv_gen = csv_reader(fileNameCSV)
#
# row_count = 0
#
# for row in csv_gen:
#     row_count += 1
#
# print(f"Row count is {row_count}")
#############################################
# File read Line by Line

count = 0
with open(fileNameCSV) as fp:
    for line in fp:
        count = count + 1
        print("Line{}: {}".format(count, line.strip()))