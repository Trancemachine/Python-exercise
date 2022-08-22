import requests
import json
from pandas import DataFrame

# 所有城市都是17页数据，这里地区以四川为例
city = '四川'
url = 'https://datacenter-web.eastmoney.com/api/data/v1/get'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

oil_dict = {
    '地区': [],
    '日期': [],
    '92汽油价格(单位:元/升)': [],
    '涨跌': []
}

for page in range(1, 18):
    param = {
        'callback': 'datatable4579981',
        'reportName': 'RPTA_WEB_YJ_JH',
        'columns': 'ALL',
        'sortColumns': 'DIM_DATE',
        'sortTypes': '-1',
        'filter': f'(CITYNAME="{city}")',
        'pageNumber': page,
        'pageSize': '10',
        'source': 'WEB',
        'p': page,
        'pageNo': page,
        'pageNum': page,
        '_': '1658826577033'
    }
    response = requests.get(url=url, headers=header, params=param)

    # 获取到是纯文本格式字符串数据，将其转化为字典格式
    response_dict = json.loads(response.text[response.text.find('(')+1:-2])
    data_list = response_dict['result']['data']

    for item in data_list:
        oil_dict['地区'].append(f'{city}')
        oil_dict['日期'].append(item['DIM_DATE'][0:10])
        oil_dict['92汽油价格(单位:元/升)'].append(item['V92'])
        oil_dict['涨跌'].append(item['ZDE92'])

# 保存为excel数据
df = DataFrame(data=oil_dict)
df.to_excel(f'{city}92油价.xlsx')



