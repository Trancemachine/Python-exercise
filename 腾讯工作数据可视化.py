#招聘城市信息可视化
from pyecharts.charts import Pie
import pyecharts.options as opts
import json
from collections import Counter

f = open("data.json")
data = json.load(f)
f.close()

#获取所有城市
cities = [i["LocationName"] for i in data]

#统计城市数量
city_num = list(Counter(cities).items())

pie = (
    Pie(init_opts=opts.InitOpts(width="720px", height="720px"))
    .add(series_name="招聘城市占比", data_pair=city_num)
    )

pie.render("city_pie.html")
