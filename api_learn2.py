from requests import post
from json import dumps, loads

response = post(
    url="http://localhost:11434/api/embed",
    data=dumps(
        dict(
            model="all-minilm",
            input=["Shy is the sky blue?", "Why is the grass green?"]
        )
    )
)

if response.ok:
    payload = loads(response.text)
    print(payload)