import requests
import json
from pandas import DataFrame
import csv

# 读取内容为爬取区域编码的csv文件
def read_csv(csv_path):
    region_list = []
    with open(csv_path, newline='') as f:
        content = csv.reader(f)
        for row in content:
            if row[2] == '':
                break
            else:
                region_list.append(row[2])
    region_list.remove(region_list[0])
    return region_list

# 向网页发起请求，获取信息
def get_data(key, keywords, types, city_limit, page_size, output):
    for region in region_list:
        page_num = 1
        while True:
            # 向网页发起请求
            url = f'https://restapi.amap.com/v5/place/text?' \
                  f'key={key}&keywords={keywords}&types={types}&region={region}&city_limit={city_limit}' \
                  f'&page_size={page_size}&page_num={page_num}&output={output}'
            try:
            response = requests.get(url)
            except (requests.exceptions.ConnectionError):
                continue
            # 数据解析
            response_dict = json.loads(response.text)
            if response_dict['pois']:
                page_num += 1
                for item in response_dict['pois']:
                    data_dict['名称'].append(item['name'])
                    data_dict['坐标'].append(item['location'])
                    data_dict['城市'].append(item['cityname'])
                    data_dict['区县'].append(item['adname'])
                    data_dict['具体位置'].append(item['address'])
            else:
                print(f'{region}无充电站')
                break
    return data_dict


# 数据转化为excel
def save_data(data_dict):
    df = DataFrame(data_dict)
    df.to_excel('./充电站信息.xlsx')

if __name__ == '__main__':
    # 设置基础参数
    data_dict = {
        '名称': [],
        '坐标': [],
        '城市': [],
        '区县': [],
        '具体位置': []
    }
    key = 'f4d2a497d4ea384eff8fc98326d1694b'
    keywords = '充电站'
    types = '011100'
    city_limit = True
    page_size = 20
    output = 'json'
    csv_path = 'D:\python\爬虫练习\新能源汽车\四川区域.csv'
    # 调用函数
    region_list = read_csv(csv_path)
    data_dict = get_data(key, keywords, types, city_limit, page_size, output)
    save_data(data_dict)
