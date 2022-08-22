import numpy as np
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt

# 数据获取与处理
data = ts.get_k_data(code='600519')
data.isnull().sum()
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

# 股票收盘比开盘上涨3%的日期：（收盘-开盘）/开盘 > 0.03
data.loc[(data['close']-data['open'])/data['open'] > 0.03].index
# 股票开盘比前日收盘低2%的日期： （开盘-前日收盘）/前日收盘 < -0.02
data.loc[(data['open']-data['close'].shift(1)) / data['close'].shift(1) < -0.02].index

# 2020至今每月买一手股票，每年年底抛售， 求其盈亏
# 切片
data1 = data['2020-01':'2022-08']
# 购买费用
# 买入股票的日期
data_monthly = data1.resample('M').first()
cost = data_monthly['open'].sum() * 100

# 2022之前的收益
# 卖出股票的日期
data_yearly = data1.resample('A').last()[:-1]
resv = data_yearly['open'].sum() * 1200

# 目前手中股票的价值，每只用最后一天的收盘价估值
last_stock = 800 * data1['close'][-1]
# 目前的盈亏
profit = resv + last_stock - cost



# 均线
# 计算五日均线和30日均线
ma5 = data['close'].rolling(5).mean()
ma30 = data['close'].rolling(30).mean()

# 画出日均线图
plt.plot(ma5)
plt.plot(ma30)
plt.show()

# 获取金叉与死叉日期
# 截取可使用数据
ma5 = ma5[30:]
ma30 = ma30[30:]
data_ma = data[30:]
# 判断
judge1 = ma5 < ma30
judge2 = ma5 > ma30
# 判断条件
golden_jud = ~(judge1 | judge2.shift(1))
death_jud = judge1 & judge2.shift(1)
# 一直出错啊
# date_golden = data_ma.loc[golden_jud].index
# date_death = data_ma.loc[death_jud].index
date_golden = data_ma.loc[golden_jud, index=d]
