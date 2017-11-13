#BeautifulSoup 事先需要安装，Python3 需安装beautifulsoup4。 如何安装：pip install beautifulsoup4
#BeautifulSoup就是Python的一个HTML或XML的解析库，我们可以用它来方便地从网页中提取数据
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self, url, content):
        if url is None or content is None:
            return
        #print(content)
        soup = BeautifulSoup(content, 'html.parser')
        #soup = BeautifulSoup(markup, "html.parser")
        urlList = self.getUrls(url, soup)
        dataList = self.getData(url, soup)

        return urlList, dataList

    def getUrls(self, url, soup):
        urlList = set()
        links = soup.find_all('a', href=re.compile(r"/item/[\u4e00-\u9fa5_a-zA-Z0-9]+")) #https://baike.baidu.com/item/Python/407313
        for link in links:
            href = link['href']
            fullUrl = urljoin(url, href)  #从相对路径获取绝对路径
            urlList.add(fullUrl)
        return urlList


    def getData(self, url, soup):
        data = {}
        data['url'] = url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        titleNode = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        data['title'] = titleNode.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summaryNode = soup.find('div',class_="lemma-summary")
        data['summary'] = summaryNode.get_text()

        #print(data['summary'])
        return data