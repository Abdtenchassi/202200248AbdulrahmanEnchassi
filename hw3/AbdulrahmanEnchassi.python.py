import json
import requests

# QST 1

with open("C:/Users/ROG/Desktop/Abd.json.json", 'r') as file:
    data = json.load(file)

keys_list = list(data.keys())
name, projects, pets = keys_list[0], keys_list[6], keys_list[7]
print("Name:", data[name])
print("Client of the second project:", data[projects][1][' client '])
print("Second pet's name:", data[pets][1][' name '])

# Qst 2

prompt = "Please use this data to generate a story"
api_key = "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"
url = "https://api.openai.com/v1/chat/completions"
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.7
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
if response.status_code == 200:
    response_data = response.json()
    text = response_data["choices"][0]['message']['content']

# QST 3

with open("response.txt", "w") as file:
    file.write(text)