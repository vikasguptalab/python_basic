#!/usr/bin/python
from memory_profiler import profile

# instantiating the decorator
@profile
def readFile() -> None:
    fileNameCSV = "tmp/techcrunch.csv"

    lines = (line for line in open(fileNameCSV))

    list_line = (s.rstrip().split(",") for s in lines)
    cols = next(list_line)
    company_dicts = (dict(zip(cols, data)) for data in list_line)

    funding = (
        int(company_dict["raisedAmt"])
        for company_dict in company_dicts
        if company_dict["round"] == "a"
    )

    total_series_a = sum(funding)

    print(f"Total series A fundraising: ${total_series_a}")


readFile()
