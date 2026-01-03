import requests
import json


def audio_gen(text, loc, voice="af_heart"):
    url = "http://localhost:5001/synthesize"
    payload = json.dumps({
        "text": text,
        "voice": voice
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    
    if response.status_code == 200:
        audio_data = response.content
        with open(loc, "wb") as audio_file:
            audio_file.write(audio_data)
        print(f"Audio file saved as {loc}")
    else:
        print(f"Error: {response.status_code}, {response.text}")