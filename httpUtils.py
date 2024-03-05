import requests

class Response:
    def __init__(self, content, statusCode, url):
        self.content = content
        self.statusCode = statusCode
        self.url = url
    def __repr__(self): 
        return f"Response ({self.statusCode})\n{self.url} \n{self.content}"

class HttpUtils:
    @staticmethod
    def Get(url):
        response = requests.get(url)
        return Response(content=response.text, statusCode=response.status_code, url=url)

    @staticmethod
    def Post(url, data):
        answer = {"answer": data}
        response = requests.post(url, json=answer)
        return Response(content=response.json(), statusCode=response.status_code, url=url)