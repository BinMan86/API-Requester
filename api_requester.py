import requests
from loguru import logger


class RequestToAPI:
    def __init__(self, url, username=None, password=None):
        """
        :param url: Base url. Example abc.com
        :username: 
        :password:
        """
        # TODO - Remove password
        logger.info(f"{url}, {username}, {password}")
        self.url = f"https://{url}/"
        self.session = requests.Session()
        if username and password:
            self.session.auth = (username, password)
        self.headers = {"Content-Type": "application/json"}
        self.verify = False

    def delete(self, rest_url):
        """
        :param rest_url: The extension of the url

        :return repsonse: Returns the repsonse, output can be used with .status_code and .content
        """
        request_url = f"{self.url}{rest_url}"
        logger.info(f"DELETE request- {request_url}")
        response = self.session.delete(request_url, headers=self.headers, verify=self.verify)

        return response

    def head(self, rest_url):
        """
        :param rest_url: The extension of the url

        :return repsonse: Returns the repsonse, output can be used with .status_code and .content
        """
        request_url = f"{self.url}{rest_url}"
        request_url = f"{self.url}{rest_url}"
        logger.info(f"HEAD request- {request_url}")
        response = self.session.head(request_url, headers=self.headers, verify=self.verify)

        return response

    def get(self, rest_url, query_params=None):
        """
        :param rest_url: The extension of the url
        :query_params:

        :return repsonse: Returns the repsonse, output can be used with .status_code and .content
        """
        request_url = f"{self.url}{rest_url}"
        request_url = f"{self.url}{rest_url}"
        logger.info(f"GET request- {request_url}")
        response = self.session.get(request_url, headers=self.headers, params=query_params, verify=self.verify)

        return response

    def patch(self, rest_url, payload=None):
        """
        :param rest_url: The extension of the url
        :param payload:

        :return repsonse: Returns the repsonse, output can be used with .status_code and .content
        """
        request_url = f"{self.url}{rest_url}"
        request_url = f"{self.url}{rest_url}"
        logger.info(f"PATCH request- {request_url}")
        response = self.session.patch(request_url, data=payload, headers=self.headers, verify=self.verify)

        return response

    def post(self, rest_url, **kwargs):
        """
        :param rest_url: The extension of the url
        :param payload:
        :param json:

        :return repsonse: Returns the repsonse, output can be used with .status_code and .content
        """
        logger.warning(kwargs)
        request_url = f"{self.url}{rest_url}"
        logger.info(f"POST request- {request_url}")
        response = self.session.post(request_url, **kwargs, headers=self.headers, verify=self.verify)

        return response

    def put(self, rest_url, payload=None):
        """
        :param rest_url: The extension of the url
        :param payload:

        :return repsonse: Returns the repsonse, output can be used with .status_code and .content
        """        
        request_url = f"{self.url}{rest_url}"
        logger.info(f"PUT request- {request_url}")
        response = self.session.put(request_url, data=payload, headers=self.headers, verify=self.verify)

        return response
