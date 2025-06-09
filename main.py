from api_requester import RequestToAPI
from loguru import logger
import json

if __name__ == "__main__":
    logger.info("TEST")

    # Test url
    request = RequestToAPI("httpbin.org")
    request.verify = True
    response = request.get("get")
    logger.info(response.status_code)
    logger.info(response.content)
    
    # Test url
    request = RequestToAPI("httpbin.org")
    json_payload = json.dumps({"1": 123})
    response = request.post("post", json=json_payload)
    logger.info(response.status_code)
    logger.info(response.content)

