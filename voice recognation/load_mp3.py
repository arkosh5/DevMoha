from pydub import AudioSegment

audio = AudioSegment.from_wav("Recording.wav")

audio = audio+6

audio = audio*2

audio = audio.fade_in(2000)

audio.export("sarah.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("sarah.mp3")

print("Done")