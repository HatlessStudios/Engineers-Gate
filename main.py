from sys import exit

import csv_reader
import evaluate_earnings
import data_grapher
import model


def menu():

    print('''
    Menu:
    
    1. View Graphs
    2. Model Currency
    3. Exit
    ''')

    # Until menu option exit.
    while True:
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
    pass


def model_currency():
    pass


if __name__ == "__main__":
    menu()
