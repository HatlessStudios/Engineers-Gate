from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense
from keras.backend import std
from tensorflow import squared_difference


def std_difference(y_true, y_pred):
    return std(squared_difference(y_true, y_pred))


def create_model(input_size, layer_sizes, batch_size=None):
    model = Sequential()
    model.add(Dense(input_size, input_shape=(batch_size, input_size)))
    for layer_size in layer_sizes:
        model.add(LSTM(layer_size))
        model.add(Activation("sigmoid"))
    model.compile(optimizer="rmsprop", loss="mse", metrics=[std_difference])
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
