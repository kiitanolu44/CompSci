from requests import post
from json import dumps, loads
from argparse import ArgumentParser
from os import system

def generate_text(prompt:str, model:str) -> str:
    response = post(
        url="http://localhost:11434/api/generate",
        data=dumps(
            dict(
                model=model,
                prompt=prompt,
                stream=False
                )
            )
        )

    if response.ok:
        payload = loads(response.text)
        return payload['response']
    response.raise_for_status()


if __name__=="__main__":
    parser = ArgumentParser(description="")
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--model", type=str, default="llama3.2")
    parser.add_argument("--speak", action="store_true")
    args = parser.parse_args()

    reply = generate_text(
        prompt=args.prompt,
        model=args.model
    )

    print(reply)
    if args.speak:
        system(f'say "{reply}"')