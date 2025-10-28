import threading
import requests

urls = [
    "https://httpbin.org/get",
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts/1",
]


def fetch(url):
    try:
        response = requests.get(url=url)
        if response.ok:
            print("{}: [+] SUCCESS ({})".format(url, response.status_code))
        else:
            print("{}: [-] FAILED ({})".format(url, response.status_code))
    except Exception as e:
        print("{}: [-] FAILED with {}".format(url, e))


threads = []

for url in urls:
    thread = threading.Thread(target=fetch, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All requests completed.")
