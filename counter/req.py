
def fetch(url):
    import requests
    rep = requests.get(url)
    return rep.json()
