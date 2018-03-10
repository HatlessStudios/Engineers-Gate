from model import get_score


def evaluate_currency(cur_name, data):

    if type(cur_name) == list:
        for currency in cur_name:
            print(currency, get_score(currency, data))

    else:
        print(cur_name, get_score(cur_name, data))
