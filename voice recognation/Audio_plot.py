import wave
import matplotlib.pyplot as plt
import numpy as np
import youtube_dl


object = wave.open("Recording.wav", "rb")

sample_freq = object.getframerate()
number_of_samples = object.getnframes()# n_samples
sample_wave = object.readframes(-1) #signal_wave

object.close()

length = number_of_samples / sample_freq # t_audio

print(length)

signal = np.frombuffer(sample_wave, dtype=np.int16)

excess = np.linspace(0,length,num=number_of_samples)# times

plt.figure(figsize=(15,5))
plt.plot(excess,signal)
plt.title("Audio signal")
plt.ylabel("signal wave")
plt.xlabel("time(s)")
plt.xlim(0,length)
plt.show()
