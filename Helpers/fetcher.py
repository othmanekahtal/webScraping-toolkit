import requests


def fetch(url):
    response = requests.get(url)
    response_code = response.status_code
    contentPage = response.content
    return {'response': response, 'status_code': response_code, 'content': contentPage}
