import json
import requests
API_TOKEN=''
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
# API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
# API_URL ="https://api-inference.huggingface.co/models/google/pegasus-large"
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

with open('input.txt') as f:
    data = query(
        {
            "inputs": f.read(),
            "parameters": {
                "do_sample": False,
                "temperature":20.0,
                "repetition_penalty":80.0,
                "max_length":110,
                "min_length":50,
            },
            "options":{
                "use_cache":False
            }
        }
    )
try:
    print(data[0]['summary_text'])
except Exception as e:
    print("error : ",e)
