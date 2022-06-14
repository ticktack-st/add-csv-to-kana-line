import csv
from pykakasi import kakasi

kakasi = kakasi()
kakasi.setMode("J", "H")
conv = kakasi.getConverter()

# 処理
with open('./data/write_drug_unique_search.csv', 'w') as wf:
    writer = csv.writer(wf, quoting=csv.QUOTE_ALL)

    with open("./data/drug_unique_search.csv", "r", encoding="utf-8", errors="", newline="") as rf:
        reader = csv.reader(
            rf,
            delimiter=",",
            doublequote=True,
            lineterminator="\r\n",
            quotechar='"',
            skipinitialspace=True,
        )
        for row in reader:
            writer.writerow([row[0], row[1],row[2],row[3],row[4]])
            writer.writerow([conv.do(row[0]), row[1],row[2],row[3],row[4]])