from sys import exit

import csv_reader as cr
import data_grapher as dg
import model as m
import numpy as np


def menu():

    # Until menu option exit.
    while True:

        print('''
Menu:

1. View Graphs
2. Model Currency
3. Exit
        ''')

        # Until a valid input is given.
        while True:

            menu_choice = input("Choice:   ")

            try:
                menu_choice = int(menu_choice)
                assert menu_choice in [1, 2, 3]

            except TypeError or AssertionError:
                print("You did not enter a menu number.")
                continue
            break

        if menu_choice == 1:
            show_graphs()
        elif menu_choice == 2:
            model_currency()
        elif menu_choice == 3:
            exit()


def show_graphs():

    data_dict = cr.split_data_coins(*cr.read_csv())
    coin = select_currency(data_dict)
    dg.graph_coin(data_dict, coin)


def model_currency(k=10):
    """
    Creates a neural network to model a currency.
    :param k: The degree of cross-validation to be performed.
    :return:
    """

    coin_dict, data = cr.read_csv()

    coin = select_currency(coin_dict)

    data = cr.split_data_coins(coin_dict, data)[coin]
    model_weights = []
    model_errors = []

    split_data = cr.split_data(data, k)
    split_data = [[[float(e[2]), float(e[5]), float(e[3]), float(e[4])] for e in s] for s in split_data]

    print("Modeling neural networks with k-fold cross-validation")

    for i in range(k):
        model = m.create_model(4, [8, 8, 2])

        raw_data = split_data[:i] + split_data[i+1:]
        training_data = np.array([s[:-1] for s in raw_data])
        m.train_model(model, training_data, np.array([to_expected(s) for s in raw_data]))
        error = m.test_model(model, np.array([split_data[i][:-1]]), np.array([to_expected(split_data[i])]))
        model_weights.append(np.array(m.get_weights(model)))
        model_errors.append(error[0])

    sum_error = sum(1/e for e in model_errors)

    for idx, error in enumerate(model_errors):

        proportion = (1/error)/sum_error
        model_weights[idx] = proportion * model_weights[idx]
        # model_weights[idx] = np.vectorize(lambda x: proportion * x)(model_weights[idx])

    true_weights = sum(model_weights)
    true_model = m.create_model(4, [8, 8, 2])
    m.set_weights(true_model, true_weights)
    result = m.test_model(true_model, np.array([s[:-1] for s in split_data]), np.array([to_expected(s) for s in split_data]))
    pass


def inv_g(x):
    return x / (1 + x)


def to_expected(s):
    result = []
    it = enumerate(s)
    it.__next__()
    for idx, entry in it:
        result.append([inv_g(entry[2] / s[idx - 1][2]), inv_g(entry[3] / s[idx - 1][3])])
    return result


def select_currency(data_dict):
    """
    Get user input for which currency to view.
    :param data_dict: A dictionary of currencies.
    :return: The currency that's been selected.
    """

    print("Which currency would you like?")

    num_to_key = list(enumerate(data_dict.keys()))

    for pair in num_to_key:
        print("{:>3}. {}".format(pair[0], pair[1].title()))

    while True:

        curr_choice = input("Choose your currency:   ")

        try:
            curr_choice = int(curr_choice)
            assert curr_choice in range(1, len(data_dict.keys()) + 1)

        except TypeError or AssertionError:
            print("You did not enter a currency number.")
            continue
        break

    return num_to_key[curr_choice][1]


if __name__ == "__main__":
    menu()
