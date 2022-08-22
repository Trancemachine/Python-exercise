import pandas as pd
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import SymbolType, ChartType, ThemeType

# 读取前1000数据，否则数据过大渲染容易达不到效果
df = pd.read_csv('D:\\python\\爬虫练习\\新能源汽车\\四川_充电站_84.csv', encoding='gbk').iloc[:1001]

g = Geo(
    init_opts=opts.InitOpts(width='4000px', height='3000px', theme=ThemeType.DARK)
)
g.add_schema(maptype='四川')

data = []
for i in range(len(df)):
    g.add_coordinate(df.iloc[i]['name'], df.iloc[i]['x'], df.iloc[i]['y'])
    data.append((df.iloc[i]['name'], 1))

g.add('四川部分充电站分布',
      data_pair=data,
      type_='scatter',
      symbol_size=6,
      color='red')
g.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
g.set_global_opts(title_opts=opts.TitleOpts(title='四川部分充电站分布'))

g.render('四川部分充电站分布.html')
