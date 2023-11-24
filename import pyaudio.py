import pyaudio
import requests
import json
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
API_ENDPOINT = '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'

def transcribe_audio(data):
    headers = {
        'Content-Type': 'audio/wav'
    }
    response = requests.post(API_ENDPOINT, headers=headers, data=data)
    
    if response.status_code == 200:
        result = response.json()
        if 'transcript' in result:
            return result['transcript']
        else:
            return 'Transcription not available'
    else:
        return 'Error occurred during transcription'
def listen_for_signal():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)
    
    print('Listening for signal...')
    frames = []
    while True:
        data = stream.read(CHUNK_SIZE)
        frames.append(data)
        # Check for a specific keyword or phrase to indicate the second signal
        if b'Food is ready' in data:
            print('Your food is ready!')
            break
        # Check for a specific duration to stop listening
        if len(frames) * CHUNK_SIZE >= RATE * 10:
            print('No second signal received within the specified duration')
            break
    stream.stop_stream()
    stream.close()
    p.terminate()
    # Convert the captured audio frames to a WAV file format
    audio_data = b''.join(frames)
    return audio_data
#Example
audio_data = listen_for_signal()
transcription = transcribe_audio(audio_data)
print('Transcription:', transcription)
