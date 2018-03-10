import csv
import data_grapher


def read_csv():

    """
    Parse a CSV file and return the list of cryptocurrencies used,
    along with their associated data.
    :return: A dictionary of the coins, A list of data.
    """

    with open("data/coin_data.csv", newline='') as csvfile:

        data = []
        coin_dict = {}
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        # Read each row in the csv
        for row in spamreader:

            # Convert row into a list of values and add to the dataset
            line = row[0].split(",")
            data.append(line)

            # Increment or add the coin to the coin dictionary
            if line[1] not in coin_dict:
                coin_dict[line[1]] = 1
            else:
                coin_dict[line[1]] += 1

        # Sort the data by coin name
        data.sort(key=lambda x: x[1])

    return coin_dict, data


def filter_data(coin_dict, data, k, coin):

    """
    Parses the data, removing currencies with less than 200 available data,
    Separates data into categories based on the currency,
    Splits the list into two data sets - one for training, and one for testing.
    :param coin_dict: Dictionary of currencies and their occurrences.
    :param data: Values from data set e.g. low/high prices.
    :return: A batch of test data, and training data.
    """

    data_by_coin = split_data_coins(coin_dict, data)

    segment_size = len(data_by_coin[coin]) // k
    k_set = []

    for i in range(0, len(data_by_coin[coin]), segment_size):
        k_set.append(data_by_coin[coin][i:i + segment_size])



    return k_set

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



