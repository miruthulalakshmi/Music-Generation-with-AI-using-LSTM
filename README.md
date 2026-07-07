🎵 Music Generation with AI using LSTM

📌 Overview

This project is an AI-powered music generation system that learns musical patterns from MIDI files and composes new melodies using a Long Short-Term Memory (LSTM) neural network. The model is trained on classical piano music, extracts notes and chords from MIDI files, learns sequential relationships, and generates original music that can be saved as a MIDI file.

⸻

🚀 Features

* Train an LSTM neural network on MIDI music files
* Extract notes and chords using the music21 library
* Learn musical sequences from classical compositions
* Generate new melodies based on learned patterns
* Export generated music as a playable MIDI file
* Simple and modular Python implementation

⸻

🛠️ Technologies Used

* Python 3.11
* TensorFlow / Keras
* music21
* NumPy
* Pickle
* Glob

⸻

📁 Project Structure

Music-Generation-AI/
│
├── dataset/
│   ├── *.mid
│
├── model/
│   └── music_model.keras
│
├── output/
│   └── generated_music.mid
│
├── preprocess.py
├── train.py
├── generate.py
├── requirements.txt
├── README.md
└── .gitignore

⸻

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/Music-Generation-AI.git
cd Music-Generation-AI

Create and activate a virtual environment (recommended):

conda create -n musicai python=3.11
conda activate musicai

Install the required packages:

pip install -r requirements.txt

⸻

📂 Dataset

Place your MIDI (.mid) files inside the dataset folder.

Example:

dataset/
├── song1.mid
├── song2.mid
├── song3.mid
└── ...

The project works best with classical piano MIDI files.

⸻

▶️ How to Run

Step 1: Preprocess the Dataset

python preprocess.py

This extracts notes and chords from all MIDI files and stores them in notes.pkl.

⸻

Step 2: Train the Model

python train.py

The LSTM model learns musical patterns and saves the trained model as:

model/music_model.keras

⸻

Step 3: Generate Music

python generate.py

A new melody is generated and saved as:

output/generated_music.mid

⸻

🔄 Workflow

MIDI Dataset
      │
      ▼
Preprocessing
      │
      ▼
Extract Notes & Chords
      │
      ▼
Sequence Creation
      │
      ▼
LSTM Model Training
      │
      ▼
Music Generation
      │
      ▼
Save as MIDI File

⸻

🧠 Model Architecture

* Input: Musical note sequences
* Neural Network: LSTM (Long Short-Term Memory)
* Dense Output Layer with Softmax Activation
* Loss Function: Categorical Crossentropy
* Optimizer: Adam

⸻

📈 Results

The trained model learns sequential musical patterns from the provided MIDI dataset and generates original note sequences that are converted into a playable MIDI file.

⸻

📚 Learning Outcomes

* Deep Learning with TensorFlow/Keras
* Sequence Modeling using LSTM
* MIDI File Processing
* Music Data Preprocessing
* AI-Based Music Generation
* Neural Network Training
* Creative AI Applications

⸻

🔮 Future Enhancements

* Train on larger and more diverse music datasets
* Support multiple music genres
* Add attention mechanisms or Transformer models
* Build a web interface using Flask or Streamlit
* Convert generated MIDI to MP3 or WAV
* Add tempo and instrument customization

⸻

👩‍💻 Author

Miruthulalakshmi D

Passionate about Artificial Intelligence, Machine Learning, and Deep Learning, with a focus on building practical AI applications that solve real-world problems and demonstrate modern machine learning techniques.

⸻

📄 License

This project is intended for educational and learning purposes. Feel free to fork, modify, and build upon it with appropriate attribution.