# speech_model.py - TensorFlow Speech Detection

import tensorflow as tf
import numpy as np

# Load the Speech Commands dataset (you can change this to a custom dataset)
SPEECH_COMMANDS = ['yes', 'no', 'stop', 'go']

def detect_speech(audio_file):
    model = tf.keras.models.load_model('speech_model.h5')
    audio_data = np.load(audio_file)
    prediction = model.predict(audio_data)
    return SPEECH_COMMANDS[np.argmax(prediction)]


# backend/models/speech_model.py
def detect_speech(audio_data):
    return "Fake speech recognition result"
