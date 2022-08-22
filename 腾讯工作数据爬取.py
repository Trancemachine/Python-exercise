#获取json数据
import requests
import json
from fake_useragent import UserAgent

json_data = []

#获取30页
for i in range(1, 31):
        params = {
                "keyword":"Python",
                "pageIndex":i,
                "pageSize":10,
                "language":"zh-cn",
                "area":"cn"
                }
        headers = {
                "User-Agent": UserAgent().random
                }
        url = "https://careers.tencent.com/tencentcareer/api/post/Query"
        json_data += requests.get(url, params=params, headers=headers).json()["Data"]["Posts"]

with open("data.json", "w", encoding = "UTF-8") as f:
        json.dump(json_data, f)


#转换为excel
import json
from pandas import DataFrame

f1 = open("data.json")
data = json.load(f1)
f1.close()

excel_dict = {
        "工作岗位名": [],
        "招聘国家": [],
        "招聘城市名": [],
        "工作责任": [],
        "最后更新时间": [],
        "详细页网址": []
        }

for i in data:
        excel_dict["工作岗位名"].append(i["RecruitPostName"])
        excel_dict["招聘国家"].append(i["CountryName"])
        excel_dict["招聘城市名"].append(i["LocationName"])
        excel_dict["工作责任"].append(i["Responsibility"])
        excel_dict["最后更新时间"].append(i["LastUpdateTime"])
        excel_dict["详细页网址"].append(i["PostURL"])

df = DataFrame(data=excel_dict)
df.to_excel("data.xlsx")
