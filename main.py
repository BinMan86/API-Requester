from api_requester import RequestToAPI
from loguru import logger
import json

def main():
    logger.info("TEST")

if __name__ == "__main__":
    logger.info("TEST")

    request = RequestToAPI("httpbin.org")
    response = request.get("get")
    logger.info(response.status_code)
    logger.info(response.content)


    payload = json.dumps({ "name": "Apple AirPods 2", "data": { "color": "white", "generation": "3rd", "price": 135}})
    response = request.post("post", payload=payload)
    logger.info(response.status_code)
    logger.info(response.content)


    response = request.get("get")
    logger.info(response.status_code)
    logger.info(response.content)

