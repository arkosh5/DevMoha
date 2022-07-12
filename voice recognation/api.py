import requests
import time
import json
from api_config import KEY_API, API_KEY_LISTENNOTES
import sys
import pprint

upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
listennotes_endpoint = "https://listen-api.listennotes.com/api/v2/episodes"
ai_headers = {'authorization': KEY_API}
listennotes_headers = {'X-ListenAPI-Key': API_KEY_LISTENNOTES}


def upload(filename):
    def read_file(filename, chunk_size=5242880):

        with open(filename, "rb") as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
        print(type(chunk_size))
    upload_response = requests.post(upload_endpoint, headers=ai_headers, data=read_file(filename))
    audio_url = upload_response.json()['upload_url']
    return audio_url

def get_audio_url(episode_id):
    url = listennotes_endpoint + '/' + episode_id
    response = requests.request('GET', url, headers=listennotes_headers)

    data = response.json()
    pprint.pprint(data)


# transcribe

def transcribe(audio_url, sentiments):
    transcript_request = {
        "audio_url": audio_url,
        "sentiment_analysis": sentiments
    }
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=ai_headers)
    job_id = transcript_response.json()['id']
    return job_id


# poll
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=ai_headers)
    return polling_response.json()


def get_results_url(audio_url, sentiments):
    transcript_id = transcribe(audio_url, sentiments)
    while True:
        data = poll(transcript_id)

        if data['status'] == 'completed':
            return data, None
        elif data["status"] == 'error':
            return data, data['error']

        print("waiting 30 secs...")
        time.sleep(30)


# save transcript
def saved_transcript(audio_url, title, sentiments=False):
    data, error = get_results_url(audio_url, sentiments)

    if data:
        file_text = title + ".txt"
        with open(file_text, "w") as f:
            f.write(data['text'])
        if sentiments:
            file_text = title + "_sentiments.json"
            with open(file_text, "w") as f:
                sentiments = data["sentiment_analysis_results"]
                json.dump(sentiments, f, indent=4)

        print("transcription is saved!!")
    elif error:
        print("Error!!", error)


# upload

vid = sys.argv[1]

audio_url = upload(vid)
saved_transcript(audio_url, vid)

