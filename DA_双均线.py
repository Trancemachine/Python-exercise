import numpy as np
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
from pandas import Series

# 数据获取与处理
data = ts.get_k_data(code='600519')
data.isnull().sum()
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

# 均线
# 计算五日均线和30日均线
ma5 = data['close'].rolling(5).mean()
ma30 = data['close'].rolling(30).mean()

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
# 计算金叉与死叉日期
date_golden = data_ma.loc[golden_jud].index
date_death = data_ma.loc[death_jud].index

# 金叉尽量买入，死叉全部卖出
s1 = Series(data=1, index=date_golden)
s2 = Series(data=0, index=date_death)
s = pd.concat([s1, s2])
s = s.sort_index()


first_money = 100000 # 本金
money = first_money # 可变变量，买股票的钱和买股票的收入都从该变量操作
hold = 0 # 持有股票数量
for i in range(0, len(s)):
    if s[i] == 1:
        p = data.loc[s.index[i]]['open'] # 每只股票单价
        hand_count = 100 * (money // (p*100)) # 可买入的股票数
        money -= (hand_count * p) # 将买入股票钱从money中减去
    else:
        # 将买入的股票卖出去
        p_death = data.loc[s.index[i]]['open']
        money += (p_death * hand_count)
        hold = 0

#如何判定最后一天为金叉还是死叉
last_money = hand_count * data['close'][-1]
print(money + last_money -first_money)


