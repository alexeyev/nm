# coding:utf-8

from keras.layers import Input, LSTM
from keras.layers.core import RepeatVector
from keras.layers.recurrent import SimpleRNN
from keras.models import Model
from keras.optimizers import Adam


def construct_model(maxlen, input_dimension, output_dimension, lstm_vector_output_dim):
    """
    Склеены три слова
    """
    input = Input(shape=(maxlen, input_dimension), name='input')

    # lstm_encode = LSTM(lstm_vector_output_dim)(input)
    lstm_encode = SimpleRNN(lstm_vector_output_dim, activation='relu')(input)

    encoded_copied = RepeatVector(n=maxlen)(lstm_encode)

    # lstm_decode = LSTM(output_dim=output_dimension, return_sequences=True, activation='softmax')(encoded_copied)
    lstm_decode = SimpleRNN(output_dim=output_dimension, return_sequences=True, activation='softmax')(encoded_copied)

    encoder = Model(input, lstm_decode)

    adam = Adam()
    encoder.compile(loss='categorical_crossentropy', optimizer=adam)

    return encoder
