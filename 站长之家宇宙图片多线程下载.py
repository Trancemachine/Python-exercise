import sys
sys.path.append('./zrequest.py')
from zrequest import ZRequest
import urllib.request
from lxml import etree
import os

url = "https://sc.chinaz.com/tu/yuzhou.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)
content = res.read().decode('utf-8')
root = etree.HTML(content)
img_node_path = "//div[@id='ulcontent']//a/img"
img_list = root.xpath(img_node_path)

def get_first(contents):
    if isinstance(contents, list):
        if len(contents) > 0:
            return contents[0]
        else:
            return ""

def save_img(content, file_path, file_name):
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    save_path = os.path.join(file_path, file_name)
    with open(save_path, 'wb') as f:
        f.write(content)

def callback(response, meta):
    url = response.geturl()
    content = response.read()
    alt = meta['alt']
    suffiex = url.split('.')[-1]
    file_name = alt + '.' + suffiex
    save_img(content=content, file_path='./images', file_name=file_name)


for img_node in img_list:
    alt = get_first(img_node.xpath('./@alt'))
    src = get_first(img_node.xpath('./@data-src'))
    src_url = "http:" + src.replace('\\', '/')
    request = ZRequest(url=src_url, callback=callback, headers=headers, meta={'alt': alt})
    request.start()


