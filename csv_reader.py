import csv

with open("data/coin_data.csv", newline='') as csvfile:
    data = []
    coin_dict = {}
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    #Read each row in the csv
    for row in spamreader:

        #Convert row into a list of values and add to the dataset
        line = row[0].split(",")
        data.append(line)

        #Increment or add the coin to the coin dictionary
        if line[1] not in coin_dict:
            coin_dict[line[1]] = 1
        else:
            coin_dict[line[1]] += 1

    #Sort the data by coin name
    data.sort(key=lambda x: x[1])

    #Filter out coins which are usable from the dict
    coin_dict = {k: v for k, v in coin_dict.items() if v < 200}

    #Filter out unusable coins from the data
    for coin in coin_dict.keys():
        data = list(filter(lambda a: a[1] != coin, data))

    print(data)
    print(coin_dict)

