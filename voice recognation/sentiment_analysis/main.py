from api import *

'''import json
from yt_extractor import get_audio_url, get_info
from api import saved_transcript

def save_sentiments(url):
    video_info = get_info(url)
    audio_url = get_audio_url(video_info)
    title = video_info["title"]
    title = title.strip().replace(" "," ")
    title = "data/" + title
    saved_transcript(audio_url, title, sentiments=True)
    
if __name__ == "__main__":
    save_sentiments("https://www.youtube.com/watch?v=yrqyol4B1RU")
    with open("data/first_500.json","r")as f:
        data = json.load(f)


    positives = []
    negatives = []
    neutrals = []
    word = input(">")
    for result in data:
        text = result['text']
        if word in text and result['sentiment'] == 'POSITIVE':
            positives.append(text)
        elif word in text and result['sentiment'] == 'NEGATIVES':
            negatives.append(text)
        else:
            neutrals.append(text)
    num_pos = len(positives)
    num_neg = len(negatives)
    num_neut = len(neutrals)
    print("Num of positives: ", num_pos)
    print("Num of negatives: ", num_neg)
    print("Num of neutrals: ", num_neut)
    try:
        r = num_pos/ (num_pos+num_neg)
        print(f"Positive ratio: {r:.3f}")
    except ZeroDivisionError as e:
        print("can't get the percentage")
'''
