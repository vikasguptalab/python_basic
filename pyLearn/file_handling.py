#!/usr/bin/python

fileNameCSV = "tmp/test.log"


def readFileContent(fileName):
    try:
        fileCsv = open(fileName, "r")
        fileContent = fileCsv.read()
    finally:
        # close the file
        fileCsv.close()

    return fileContent


# Print File content
readFileContent(fileNameCSV)


def read_WithOpen(fileName):
    with open(fileName, "r") as fileData:
        read_content = fileData.read()
        print(read_content)


read_WithOpen(fileNameCSV)
