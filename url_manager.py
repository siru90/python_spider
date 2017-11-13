
#url管理器
class UrlManager(object):
    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()

    #单个添加url
    def add_url(self, url):
        if url is None:
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    #批量增加url
    def add_new_urls(self, urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_url(url)

    def has_url(self):
        return len(self.newUrls) != 0

    def get_url(self):
        new_url = self.newUrls.pop()
        self.oldUrls.add(new_url)
        return new_url

