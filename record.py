import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
 
NOTE_MIN = 60       # C4
NOTE_MAX = 69       # A4
FSAMP = 22050       # Sampling frequency in Hz
FRAME_SIZE = FSAMP   # How many samples per frame?
FRAMES_PER_FFT = 16 # FFT takes average across how many frames?

SAMPLES_PER_FFT = FRAME_SIZE*FRAMES_PER_FFT
FREQ_STEP = float(FSAMP)/SAMPLES_PER_FFT

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=FRAME_SIZE)

stream.start_stream()

print "recording..."

frames = stream.read(FRAME_SIZE)
buf = np.fromstring(frames, np.int16) 

stream.stop_stream()
stream.close()
audio.terminate()

plt.plot(buf)
plt.show()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()