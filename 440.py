from numpy.fft import rfft
import pyaudio
import numpy as np
import wave
import matplotlib.pyplot as plt

# wf = wave.open("Tritone.wav", 'rb')
wf = wave.open("440.wav", 'rb')

stream = pyaudio.PyAudio().open(
                format = pyaudio.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

Tab = []

flag = False
while True:
    data = wf.readframes(1024)
    buf = np.fromstring(data, np.int16)
    stream.write(data)
    if buf.shape[0] == 1024:
        buf = np.abs(rfft(buf))
        if flag:
            Tab = np.c_[Tab, buf]
        else:
            flag = True
            Tab = buf
    else: 
        break

Tab = np.array(Tab)
Tab = Tab[:100].T[:50]
Time = Tab.shape[0]*1024./wf.getframerate()

print Tab.shape

df = wf.getframerate()/1024.
MaxFrequency = Tab.shape[1]*df
        
fig, ax = plt.subplots(figsize=(12,5))
ax.imshow(Tab, extent=[0,MaxFrequency,Time,0], aspect="auto")
plt.xticks(fontsize=15)
plt.xlabel("czestotliwosc [Hz]", fontsize = 30)
plt.yticks(fontsize=15)
plt.ylabel("czas [s]", fontsize = 30)
plt.show()
