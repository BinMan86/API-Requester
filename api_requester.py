import requests
from loguru import logger


class RequestToAPI:
    def __init__(self, url, username=None, password=None):
        logger.info(f"{url}, {username}, {password}")
        self.url = f"https://{url}/"
        self.session = requests.Session()
        if username and password:
            self.session.auth = (username, password)
        self.headers = {"Content-Type": "application/json"}
        self.verify = False

    def delete(self, rest_url):
        request_url = f"{self.url}{rest_url}"
        logger.info(f"DELETE request- {request_url}")
        response = self.session.delete(request_url, headers=self.headers, verify=self.verify)

        return response

    def head(self, rest_url):
        request_url = f"{self.url}{rest_url}"
        logger.info(f"HEAD request- {request_url}")
        response = self.session.head(request_url, headers=self.headers, verify=self.verify)

        return response

    def get(self, rest_url, query_params=None):
        request_url = f"{self.url}{rest_url}"
        logger.info(f"GET request- {request_url}")
        response = self.session.get(request_url, headers=self.headers, params=query_params, verify=self.verify)

        return response

    def patch(self, rest_url, payload=None):
        request_url = f"{self.url}{rest_url}"
        logger.info(f"PATCH request- {request_url}")
        response = self.session.patch(request_url, data=payload, headers=self.headers, verify=self.verify)

        return response

    def post(self, rest_url, payload=None, json=None):
        request_url = f"{self.url}{rest_url}"
        logger.info(f"POST request- {request_url}")
        response = self.session.post(request_url, data=payload, json=json, headers=self.headers, verify=self.verify)

        return response

    def put(self, rest_url, payload=None):
        request_url = f"{self.url}{rest_url}"
        logger.info(f"PUT request- {request_url}")
        response = self.session.put(request_url, data=payload, headers=self.headers, verify=self.verify)

        return response
