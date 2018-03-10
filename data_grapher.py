import matplotlib.pyplot as plt
import csv_reader

def split_data_coins(coin_dict, data):
    coin_dict_over_200 = {k: v for k, v in coin_dict.items() if v >= 200}
    # Filter out coins which are usable from the dict
    coin_dict = {k: v for k, v in coin_dict.items() if v < 200}

    # Filter out unusable coins from the data
    for coin in coin_dict.keys():
        data = list(filter(lambda a: a[1] != coin, data))

    data_by_coin = {}

    for coin in coin_dict_over_200.keys():
        data_by_coin[coin] = list(filter(lambda a: a[1] == coin, data))

    return data_by_coin

def reorganise_data(data_by_coin, coin):

    date = []
    open_data = []
    close_data = []
    high_data = []
    low_data = []

    for line in data_by_coin[coin]:
        date.append(line[0])
        open_data.append(line[2])
        high_data.append(line[3])
        low_data.append(line[4])
        close_data.append(line[5])

    return date, open_data, close_data, high_data, low_data

def graph_coin(data_by_coin, coin):

    date, open_data, close_data, high_data, low_data = reorganise_data(data_by_coin, coin)

    plt.plot(open_data)

    plt.show()


coin_dict, data = csv_reader.readCSV()
data_by_coin = split_data_coins(coin_dict, data)
graph_coin(data_by_coin, "bitcoin")


