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
    return model.fit(training_data, expected_output, batch_size, epochs)


def test_model(model, testing_data, expected_output, steps=1):
    return model.evaluate(testing_data, expected_output, steps=steps)


def predict_model(model, data, steps=1):
    return model.predict(data, steps=steps)


def get_weights(model):
    return [layer.get_weights() for layer in model.model.layers]


def set_weights(model, weights):
    for layer, w in zip(model.model.layers, weights):
        layer.set_weights(w)


get_custom_objects().update({"damned": Activation(g)})
if __name__ == "__main__":
    import numpy as np
    dummy = create_model(2, [2])
    dummy_result = test_model(dummy, np.array([[[0, 0], [0, 0]]]), np.array([[[0, 1], [2, 4]]]))
