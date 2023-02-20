#!/usr/bin/python
from memory_profiler import profile


# instantiating the decorator
@profile
def readFile() -> None:
    fileNameCSV = "tmp/techcrunch.csv"

    total_series_a = count = 0
    company_list = []
    with open(fileNameCSV) as fp:
        for line in fp:
            count = count + 1
            if count == 1:
                cols = line.rstrip().split(",")
                continue

            data = line.rstrip().split(",")
            company_dic = dict(zip(cols, data))
            company_list.append(company_dic)

            if company_dic["round"] == "a":
                total_series_a = total_series_a + int(company_dic["raisedAmt"])

    print(f"Total series A fundraising: ${total_series_a}")


readFile()
