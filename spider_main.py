# alt enter 然后就可以新建class
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager


class SpiderMain(object):

    #g构造函数：初始化对象
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_url(root_url)
        try:
            while self.urls.has_url():
                url = self.urls.get_url()
                print(count,url)
                html_content = self.downloader.download(url)
                new_urls, new_data = self.parser.parser(url, html_content)

                #print(new_data)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count = count+1
                if count == 100:
                    continue
        except:
            print('获取url失败')

        self.outputer.output_html()


if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
