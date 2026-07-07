import pickle
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

sequence_length = 100

notes = pickle.load(open("notes.pkl", "rb"))

pitchnames = sorted(set(notes))

note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

network_input = []
network_output = []

for i in range(len(notes)-sequence_length):

    sequence_in = notes[i:i+sequence_length]
    sequence_out = notes[i+sequence_length]

    network_input.append([note_to_int[char] for char in sequence_in])
    network_output.append(note_to_int[sequence_out])

n_patterns = len(network_input)

network_input = np.reshape(network_input,
                           (n_patterns, sequence_length, 1))

network_input = network_input / float(len(pitchnames))

network_output = to_categorical(network_output)

model = Sequential()

model.add(LSTM(
    512,
    input_shape=(network_input.shape[1], network_input.shape[2]),
    return_sequences=True
))

model.add(Dropout(0.3))

model.add(LSTM(512))

model.add(Dense(256, activation='relu'))

model.add(Dense(len(pitchnames), activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam'
)

model.fit(
    network_input,
    network_output,
    epochs=50,
    batch_size=64
)

model.save("model/music_model.keras")