from requests import post
from json import dumps, loads

response = post(
    url="http://localhost:11434/api/generate",
    data=dumps(
        dict(
            model="llava",
            prompt="what should i have for dinner?",
            stream=False
        )
    )
)

if response.ok:
    payload = loads(response.text)
    print(payload)