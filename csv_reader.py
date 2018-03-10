import csv

with open("data/coin_data.csv", newline='') as csvfile:
    data = []
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        data.append(row[0].split(","))

    data.sort(key=lambda x: x[1])

    print(data)
