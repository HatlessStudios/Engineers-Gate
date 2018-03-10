from model import predict_model, test_model


def evaluate_currency(model, steps, data, s_d, ):

    """
    Calculates the likely revenue per stock, accompanied by a failure rate and standard deviation.
    :param model: The RNN
    :param history:
    :param steps:
    :param data:
    :return:
    """

    cur_mult = predict_model(model, data, steps)
