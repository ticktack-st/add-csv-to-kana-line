import csv

length = 0
with open("./opt/data/drug_unique_search.csv", "r", encoding="utf-8", errors="", newline="") as rf:
# with open("./trkkey_1_csvgen.csv", "r", encoding="utf-8", errors="", newline="") as rf:
    reader = csv.reader(
        rf,
        delimiter=",",
        doublequote=True,
        lineterminator="\r\n",
        quotechar='"',
        skipinitialspace=True,
    )
    for row in reader:
        tmp = len(row[0])
        if length < tmp:
            length = tmp

print(length)