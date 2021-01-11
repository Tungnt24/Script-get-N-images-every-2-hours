import urllib
import requests
import logging

from typing import List
from src.config import Config
from src.app import app
from datetime import datetime

logging.basicConfig(
    format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)


@app.task
def save_image(images: List[str]):
    for src in images:
        urllib.request.urlretrieve(
            src, f"./images/{datetime.now().strftime('%H:%M:%S')}.jpeg"
        )
    return "images have been downloaded"


@app.task
def get_images():
    params = {
        "client_id": Config.client_id,
        "count": Config.count,
        "query": Config.query,
        "orientation": Config.orientation,
    }
    try:
        response = requests.get(Config.url, params=params)
        images = [image["urls"]["regular"] for image in response.json()]
        logging.info("get images done")
        return save_image(images)
    except Exception as e:
        logging.error(e)
