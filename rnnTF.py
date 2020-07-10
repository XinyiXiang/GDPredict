#this script uses encoder and decoder
import collections
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

encoder_vocab = 1000
decoder_vocab = 2000

encoder_input = layers.Input(shape=(None,))
encoder_embedded = layers.Embedding(input_dim = encoder_vocab,
                    output_dim=64)(encoder_input)

output,state_h,state_c = layers.LSTM(
    64,return_state=True,name='encoder')(encoder_embedded)
encoder_state = [state_h,state_c]

decoder_input = layers.Input(shape=(None,))
decoder_embedded = layers.Embedding(input_dim=decoder_vocab,output_dim=64)(decoder_input)

#Pass the 2 states to a new LSTM layer, as initial state
decoder_output = layers.LSTM(
    64,name='decoder')(decoder_embedded,initial_state=encoder_state)
output = layers.Dense(10)(decoder_output)

model = tf.keras.Model([encoder_input,decoder_input],output)
model.summary()