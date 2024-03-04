import requests

class Response:
    def __init__(self, content, statusCode, url):
        self.content = content
        self.statusCode = statusCode
        self.url = url
    def __repr__(self): 
        return f"Response ({self.statusCode})\n{self.url} \n{self.content}"

    
class HttpUtils:
    def Get(url):
        respons = requests.get(url)
        return Response(content=respons.text,statusCode=respons.status_code, url=url)
    
    def Post(url, data):
        answer = {answer:data}
        respons = requests.post(url,json=answer)
        return Response(content=respons.json(),statusCode=respons.status_code, url=url)