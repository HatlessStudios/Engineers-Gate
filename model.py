from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense


def create_model(input_size, layer_sizes, batch_size=None):
    model = Sequential()
    model.add(Dense(input_size, input_shape=(batch_size, input_size)))
    for layer_size in layer_sizes:
        model.add(LSTM(layer_size))
        model.add(Activation("sigmoid"))
    model.compile(optimizer="rmsprop", loss="mse")
    return model


def train_model(model, training_data, expected_output, batch_size=32, epochs=1):
    return model.fit(training_data, expected_output, batch_size, epochs)


def test_model(model, testing_data, expected_output, batch_size=32):
    return model.evaluate(testing_data, expected_output, batch_size)
