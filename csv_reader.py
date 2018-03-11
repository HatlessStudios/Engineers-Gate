import csv


def read_csv():
    """
    Parse a CSV file and return the list of cryptocurrencies used,
    along with their associated data.
    :return: A dictionary of the coins, A list of data.
    """

    with open("data/coin_data.csv", newline='') as csvfile:

        data = []
        coin_dict = {}
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        reader.__next__()
        # Read each row in the csv
        for row in reader:
            data.append(row)
            # Increment or add the coin to the coin dictionary
            if row[1] not in coin_dict:
                coin_dict[row[1]] = 1
            else:
                coin_dict[row[1]] += 1

        # Sort the data by coin name
        data.sort(key=lambda x: x[1])

    return coin_dict, data


def split_data(coin_data, k):
    """
    Splits the list into two data sets - one for training, and one for testing.
    :param k:
    :param coin_data: List of coins mapping to data as returned by split_data_coins.
    :return: A batch of test data, and training data.
    """

    segment_size = len(coin_data) // k
    return [coin_data[i:i + segment_size] for i in range(0, len(coin_data), segment_size)]


def split_data_coins(coin_dict, data):
    # Filter out unusable coins from the data
    data = [p for p in data if coin_dict[p[1]] >= 200]
    return {coin: [p for p in data if p[1] == coin] for coin, v in coin_dict.items()}


if __name__ == '__main__':
    read_csv()
