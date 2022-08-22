from urllib import request
from lxml import etree
import json

xhs_data = []

# 请求数据
url = 'https://www.xiaohongshu.com/explore'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
text = res.read().decode('utf-8')

# 数据xpath解析
root = etree.HTML(text)
origin_path = "//div[@class='note-wrapper']"
info_list = root.xpath(origin_path)

# 保护函数
def get_first(contents):
    if isinstance(contents, list):
        if len(contents) > 0:
            return contents
    else:
        return ""

# 运行主逻辑线
for info in info_list:
    note_name = get_first(info.xpath(".//div[@class='note-info']/a/text()"))
    user_name = get_first(info.xpath(".//div[@class='note-append']//span/text()"))
    user_num = len(user_name)
    for j in range(user_num):
        xhs_data.append({'用户名称': user_name[j],
                       '笔记名称': note_name[j]
                       })

print(xhs_data)