import requests
import os
from lxml import etree
import sys
sys.path.append('./zrequest.py')
from zrequest import ZRequest

# 爬虫：首页与详情页解析
class BQGSpider(object):
    name = 'BQGSpider'

    def run(self):
        home_url = 'https://www.bbiquge.net/book/128390/'
        response = requests.get(home_url)
        page_urls = self.parse_home(response)
        for page_url in page_urls[:5]:
            # 多线程获取详情页url
            request = ZRequest(url=page_url, callback=self.parse_page)
            request.start()

    def parse_home(self, response):
        response.encoding = 'gbk'
        root = etree.HTML(response.text)
        pageurl_list = root.xpath("//div[@class='zjbox']/dl[@class='zjlist']//a/@href")
        base_url = 'https://www.bbiquge.net/book/128390/'
        page_urls = []
        for pageurl in pageurl_list[:5]:
            page_urls.append(base_url + pageurl)
        return page_urls

    def parse_page(self, response, meta):
        response.encoding = 'gbk'
        title_path = "/html/body/div[@id='main']/h1/text()"
        content_path = "//div[@id='content']//text()"
        root = etree.HTML(response.text)
        title = root.xpath(title_path)[0]
        content_list = root.xpath(content_path)

        model = BQGModel()
        model.save_data(title, content_list, path)

path = './笔趣阁'

# 所有数据的存储
class BQGModel(object):
    def __init__(slef, name=''):
        slef.name = name

    def save_data(self, title, content_list, path):
        if not os.path.exists(path):
            os.mkdir(path)
        file_name = title + '.txt'
        file_path = os.path.join(path, file_name)
        content_string = ''
        for i in content_list:
            i = i.replace('\xa0', '')
            content_string += i.strip() + '\n'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_string)



if __name__ == '__main__':
    spider = BQGSpider()
    spider.run()

