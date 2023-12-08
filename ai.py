import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf

import keras
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense, Masking
from keras import Sequential

from keras.datasets import imdb

import warnings

num_words = 5000
embeding_dim = 32 
output_lstm = 100

model = Sequential() 
model.add(Embedding(num_words, embeding_dim, input_length=500)) 
model.add(LSTM(output_lstm)) 
model.add(Dense(1, activation='sigmoid')) 
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy']) 
model.summary()

model.save('moviereviews3.h5')
