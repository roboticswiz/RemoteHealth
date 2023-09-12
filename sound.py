import pyaudio
import wave
from pydub import AudioSegment
import os
import numpy as np
import pyrebase

chunk = 1024  # Record in chunks of 1024 samples

sample_format = pyaudio.paInt32  # 32 bits per sample
#sample_format = pyaudio.paFloat32  # 16 bits per sample - not good
channels = 1
fs = 44100  # Record at 48000 samples per second
seconds = 10
filename = "C:/Users/vaibh/Desktop/HealthCode/output.wav" # file name with its path
filenamemp3 = "C:/Users/vaibh/Desktop/HealthCode/output1.mp3"

# mic sensitivity correction and bit conversion
mic_sens_dBv = -10.0
mic_sens_corr = np.power(10.0,mic_sens_dBv/20.0)



p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True, # yes for input
                input_device_index=1 #selecting the input mic
               )

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)


# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')


# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

# Converting WAV file to MP3 file format
AudioSegment.from_wav(filename).export(filenamemp3, format="mp3")


# trasferring files to Firebase Cloud Storage
# Firebase / Pyrebase variables setup
config = {
  "apiKey": "AIzaSyCCJ8mPbuKJb-Hv-ABgD1DnSkaEQdTgprk",
  "authDomain": "remotehealth-40d3f.firebaseapp.com",
  "projectId": "remotehealth-40d3f",
  "storageBucket": "remotehealth-40d3f.appspot.com",
  "serviceAccount": "servicekey.json",
  "databaseURL": " "
 # "messagingSenderId": "1078999652192",
 # "appId": "1:1078999652192:web:55e96bb3b0da32f2f17005",
  #"measurementId": "G-V114G87MVC",
}

#initializing firebase storage
firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()

#transferring required file
storage.child("output1.MP3").put("output1.MP3")
