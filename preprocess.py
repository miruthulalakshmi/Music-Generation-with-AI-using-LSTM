from music21 import converter, note, chord
import glob
import pickle

notes = []

# Read both .mid and .MID files
midi_files = glob.glob("dataset/*.mid") + glob.glob("dataset/*.MID")

for file in midi_files:
    print(f"Processing: {file}")

    midi = converter.parse(file)

    # Read all notes directly
    for element in midi.recurse().notes:

        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append(".".join(str(n) for n in element.normalOrder))

print(f"\nTotal Notes: {len(notes)}")

with open("notes.pkl", "wb") as f:
    pickle.dump(notes, f)