import csv

with open("data/coin_data.csv", newline='') as csvfile:
    coin_dict = {}
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        coin = row[0].split(",")[1]
        if coin not in coin_dict.keys():
            coin_dict[coin] = 1
        else:
            coin_dict[coin] += 1

    print(coin_dict)
    coin_dict_under200 = {k: v for k, v in coin_dict.items() if v < 200}
    print(len(coin_dict_under200))
