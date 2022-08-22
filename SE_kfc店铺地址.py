from urllib import request
from urllib import parse
import json
from pandas import DataFrame

excel_dict = {
    '店名': [],
    '地址': [],
    '状态': []
    }

# 配置全局变量
post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

# 配置请求对象
def prepare_request(url, headers, data_dict):
    data = parse.urlencode(data_dict)
    data = data.encode('utf-8')
    req = request.Request(url=url, headers=headers, data=data)
    return req

# 请求数据
def request_with_url(req):
    response = request.urlopen(req)
    content = response.read().decode('utf-8')
    return content

# 对响应数据进一步解析
def parse_data(content):
    json_obj = json.loads(content)
    if len(json_obj['Table1']) == 0:
        return True
    for i in json_obj['Table1']:
        excel_dict['店名'].append(i['storeName'])
        excel_dict['地址'].append(i['addressDetail'])
        excel_dict['状态'].append(i['pro'])

pageIndex = 1
while True:
    data_dict = {
        'cname': '成都',
        'pageIndex': pageIndex,
        'pageSize': 10
        }
    request_url = prepare_request(post_url, headers, data_dict)
    content = request_with_url(request_url)
    if parse_data(content) == True:
        break
    else:
        pageIndex += 1
