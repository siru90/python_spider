#Python3 没有urllib2 ，所有功能都集合到了urllib
import urllib.request


class HtmlDownloader(object):
    
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()