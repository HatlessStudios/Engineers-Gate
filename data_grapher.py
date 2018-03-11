import matplotlib.pyplot as plt


def reorganise_data(data_by_coin, coin):

    date = []
    open_data = []
    close_data = []
    high_data = []
    low_data = []
    volume = []

    for line in data_by_coin[coin]:
        date.append(line[0])
        open_data.append(line[2])
        high_data.append(line[3])
        low_data.append(line[4])
        close_data.append(line[5])
        volume.append(line[6])

    return date, open_data, close_data, high_data, low_data, volume


def graph_coin(data_by_coin, coin):

    date, open_data, close_data, high_data, low_data, volume = reorganise_data(data_by_coin, coin)

    high_low_diff = []
    open_close_diff = []

    for i in range(len(date)):
        high_low_diff.append(float(high_data[i]) - float(low_data[i]))
        open_close_diff.append(float(close_data[i]) - float(open_data[i]))

    plt.title("High-Low Difference for " + coin)
    plt.plot(high_low_diff)
    plt.show()

    plt.title("High and Low for " + coin)
    plt.plot(high_data, 'r', low_data, 'b')
    plt.show()

    plt.title("Volume for " + coin)
    plt.plot(volume)
    plt.show()

    plt.title("Open-Close Difference for " + coin)
    plt.plot(open_close_diff)
    plt.show()

    plt.title("Open and Close for " + coin)
    plt.plot(open_data, 'r', close_data, 'b')
