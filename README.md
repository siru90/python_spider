# python_spider
python 简单爬虫项目

简单的爬虫架构
【1】url管理器：管理备爬取的url集合，已爬取的url集合
【2】网页下载器：urllib下载等待备爬取的url
【3】网页解析器：BeautifulSoup对网页内容进行解析得到新的url列表和感兴趣的价值数据

此实例：编写爬取百度百科页面
【1】爬虫调度类：spider_main.py
【2】url管理类：url_manager.py
【3】网页下载类：html_downloader.py
【4】网页解析类：html_parser.py
【5】内容输出类：html_outputer.py
