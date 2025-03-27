from requests import post
from json import dumps, loads
from enum import Enum
from pathlib import Path
from typing import Generator
from base64 import b64encode
from logging import getLogger, basicConfig, DEBUG

# __name__ gives you the name of the file you are in
logger = getLogger(__name__)

# an ENUM is a string with specific values
# standard practice to do all caps
class Model(Enum):
    LLAME="llama3.2"
    MULTIMODAL = "llava"

# good practice to use capital "P" Path object
def encode_images(paths:list[Path]) -> Generator[str,None,None]:
    if paths is not None:
        for path in paths:
            with path.open("rb") as image_file:
                # yield is good because it does not store in memory
                # "streams" the data
                yield b64encode(image_file.read()).decode("utf-8")

def generate_text(prompt:str, model:Model, image_paths:list[Path]=None) -> str:
    logger.debug(image_paths)
    response = post(
        url="http://localhost:11434/api/generate",
        data=dumps(
            dict(
                model=model.value,
                prompt=prompt,
                images=list(encode_images(paths=image_paths)),
                stream=False
            )
        )
    )
    if response.ok:
        payload = loads(response.text)
        logger.debug(payload)
        return payload['response']
    response.raise_for_status()

if __name__ == "__main__":
    basicConfig(level=DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    reply = generate_text(
        prompt="What are are these images about?",
        model=Model.MULTIMODAL,
        image_paths=list(Path('../images/').glob("*.jpg"))
    )
    print(reply)