from keras.models import Sequential
from keras.layers import LSTM, Activation
from keras.backend import std
from keras.utils.generic_utils import get_custom_objects
from tensorflow import squared_difference


def std_deviation(y_true, y_pred):
    return std(squared_difference(y_true, y_pred))


def g(x):
    return x / (1 - x)


def create_model(input_size, layer_sizes, batch_size=None):
    """
    Creates a neural network model.
    :param input_size: The number of nodes in the input
    :param layer_sizes: A list of the sizes of each layer.
    :param: batch_size
    :return: A neural network model.
    """

    model = Sequential()
    layer_sizes = layer_sizes.__iter__()
    model.add(LSTM(layer_sizes.__next__(), input_shape=(batch_size, input_size), return_sequences=True))
    model.add(Activation("sigmoid"))
    for layer_size in layer_sizes:
        model.add(LSTM(layer_size, return_sequences=True))
        model.add(Activation("sigmoid"))
    model.add(Activation(g))
    model.compile(optimizer="rmsprop", loss="mse", metrics=[std_deviation])
    return model


def train_model(model, training_data, expected_output, batch_size=32, epochs=1):
    """
    Trains a neural network.
    :param model: The neural network to be trained.
    :param training_data: The dataset used for training.
    :param expected_output: The expected output of the model.
    :param batch_size:
    :param epochs:
    :return: A trained model.
    """

    return model.fit(training_data, expected_output, batch_size, epochs)


def test_model(model, testing_data, expected_output, steps=1):
    """
    Tests a neural network.
    :param model: The neural network to be tested.
    :param testing_data: The dataset used for testing.
    :param expected_output: The expected output of the model.
    :param steps:
    :return: A tested model.
    """
    return model.evaluate(testing_data, expected_output, steps=steps)


def predict_model(model, data, steps=1):
    """
    Runs some data through the neural network.
    :param model: The neural network to be used.
    :param data: The data being fed in.
    :param steps:
    :return: The results of feeding the data into the network.
    """

    return model.predict(data, steps=steps)


def get_weights(model):
    """
    Gets the weights of the pathways.
    :param model: The neural network to retrieve the weights from.
    :return: A list of weights from the model.
    """

    return [layer.get_weights() for layer in model.model.layers if type(layer) == LSTM]


def set_weights(model, weights):
    """
    Sets the weights of the pathways.
    :param model: The neural network to be modified.
    :param weights: The list of weights to use.
    :return:
    """

    for layer, w in zip((layer for layer in model.model.layers if type(layer) == LSTM), weights):
        layer.set_weights(w)


get_custom_objects().update({"damned": Activation(g)})
if __name__ == "__main__":
    import numpy as np
    dummy = create_model(2, [2])
    dummy_result = test_model(dummy, np.array([[[0, 0], [0, 0]]]), np.array([[[0, 1], [2, 4]]]))
