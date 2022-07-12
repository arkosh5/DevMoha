# Audio formats
# .mp3
# .flac
# .wav
import wave

# Audio signal parameters
# - number of channels
# - sampling rate
# - frame rate/sample rate: 44,100 Hz
# - number of frames
# - values of frame

voice = wave.open('Recording.wav', 'rb')

print('Number of channels: ', voice.getnchannels())
print('Sampling rate: ', voice.getframerate())
print("sample width: ", voice.getsampwidth())
print('Frame rate: ', voice.getframerate())
print('Number of frames: ', voice.getnframes())
print("parameters: ", voice.getparams())

time_audio = voice.getnframes() / voice.getframerate()
print('Time of audio: ', time_audio)

frames = voice.readframes(voice.getnframes())
print('Frames: ', len(frames)//2)
print(type(frames), type(frames[0]))
voice.close()

new_voice = wave.open("Recording_2.wav", "wb")
new_voice.setnchannels(1)
new_voice.setsampwidth(2)
new_voice.setframerate(44100)
new_voice.writeframes(frames)

new_voice.close()