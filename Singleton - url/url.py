import urllib.parse
import urllib.request


class URLFetcher:
    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)

                urls = self.urls
                urls.append(url)
                self.urls = urls


if __name__ == '__main__':
    # URLFetcher().fetch('https://www.wikipedia.org/')
    f1 = URLFetcher()
    f2 = URLFetcher()
    print(f1 is f2)
    # print(URLFetcher() is URLFetcher())

