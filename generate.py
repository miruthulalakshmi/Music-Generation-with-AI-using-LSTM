import pickle
import numpy as np
from random import randint

from tensorflow.keras.models import load_model

from music21 import note, stream

sequence_length = 100

notes = pickle.load(open("notes.pkl", "rb"))

pitchnames = sorted(set(notes))

note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

network_input = []

for i in range(len(notes)-sequence_length):
    sequence = notes[i:i+sequence_length]
    network_input.append([note_to_int[n] for n in sequence])

network_input = np.array(network_input)

model = load_model("model/music_model.keras")

start = randint(0, len(network_input)-1)

pattern = network_input[start]

prediction_output = []

for note_index in range(500):

    prediction_input = np.reshape(pattern,
                                  (1, len(pattern), 1))

    prediction_input = prediction_input / float(len(pitchnames))

    prediction = model.predict(prediction_input, verbose=0)

    index = np.argmax(prediction)

    result = int_to_note[index]

    prediction_output.append(result)

    pattern = np.append(pattern, index)

    pattern = pattern[1:]

offset = 0

output_notes = []

from music21 import instrument, note, chord

for pattern in prediction_output:

    # If it's a chord (e.g. "4.7")
    if "." in pattern or pattern.isdigit():
        notes_in_chord = pattern.split(".")
        chord_notes = []

        for current_note in notes_in_chord:
            new_note = note.Note(int(current_note))
            new_note.storedInstrument = instrument.Piano()
            chord_notes.append(new_note)

        new_chord = chord.Chord(chord_notes)
        new_chord.offset = offset
        output_notes.append(new_chord)

    else:
        new_note = note.Note(pattern)
        new_note.offset = offset
        new_note.storedInstrument = instrument.Piano()
        output_notes.append(new_note)

    offset += 0.5

midi_stream = stream.Stream(output_notes)

midi_stream.write('midi', fp='output/generated_music.mid')

print("Music Generated Successfully!") 