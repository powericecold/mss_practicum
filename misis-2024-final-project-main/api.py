import requests
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from src.handler import Handler


class Prompt(BaseModel):
    text: str
    num_steps: int = 6
    negative_prompt: str = "bad quality, worse quality, low resolution"
    num_frames: int = 20


app = FastAPI()
handler = Handler()


@app.post("/generate_video")
def read_root(
        prompt: Prompt
):
    result = handler(
        text=prompt.text,
        generator_kwargs=dict(
            num_steps=prompt.num_steps,
            negative_prompt=prompt.negative_prompt,
            num_frames=prompt.num_frames,
        )
    )
    return result

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8889)

import requests

def send_data_to_service1(data):
    url = 'http://dialog-api:8000/api/v1/users/receive_data'
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        return None, {"error 11144": str(e)}

import time
import random

def simulate_response():
    time.sleep(10)
    return f"The answer is: {random.randint(0, 50)}"
