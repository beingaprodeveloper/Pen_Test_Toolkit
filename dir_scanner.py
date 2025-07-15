import requests

def scan_directories(base_url, wordlist):
    for word in wordlist:
        url = base_url + "/" + word
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[FOUND] {url}")
