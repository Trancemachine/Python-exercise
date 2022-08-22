import pandas as pd
# 免时间戳问题
pd.plotting.register_matplotlib_converters()
import numpy as np
import scipy
import math
import collections
import seaborn as sns
import matplotlib.pyplot as plt

# 数据完整性检查、预处理
file = pd.read_csv('D:\python\数分\scindex\Smart_City_index_headers.csv')
file.info()
file.isnull().sum()
file.isna().sum()
file.columns
file.replace(' ', '')
file.columns = file.columns.str.replace(' ', '')
sci = file.drop(columns='Id')
sci = sci.drop(columns='SmartCity_Index_relative_Edmonton', ).\
    sort_values('SmartCity_Index', ascending=False)

# 智慧城市平均指标前10的国家
scimean = sci.groupby('Country').median().astype(int).\
    sort_values('SmartCity_Index', ascending=False).head(10)
# pycharm不能显示，就保存进网页
scimean_table = scimean.style.background_gradient(cmap='GnBu').to_html('./平均指标前十国家.html')

# 描述性统计
sci.describe()

# 绘制平均值散点图图像
scimean = sci.groupby('Country').median().astype(int).sort_values('SmartCity_Index', ascending=False)
sns.scatterplot(data=scimean)
sns.set_style('whitegrid')
plt.ylabel('Countries', fontsize=10)
plt.title('Smart City Subindexes per Country', fontsize=15)
ticks = plt.xticks(rotation=90)

# 绘制各指标的箱线图
plt.figure(figsize=(16, 6))
sns.boxplot(data=sci, showmeans=True, palette='pastel')
sns.set_style('whitegrid')
plt.title('Boxplot of Smart City Subindexes', fontsize=15)

# 根据正态分布检查两列数据
fig = plt.figure()
res1 = scipy.stats.probplot(sci['SmartCity_Index'], plot=plt)
res2 = scipy.stats.probplot(sci['Smart_People'], plot=plt)

# 绘制直方图
sns.set_theme()
scihist = sci.hist(figsize=(20, 10))
scihist

# 相关性
scicorr = sci.copy()
sns.set_theme()
plt.figure(figsize=(8, 10))
sns.pairplot(scicorr, kind='scatter', height=2.5)
# 相关表
corr = sci.corr('spearman')
corrstyle = sci.corr('spearman').style.background_gradient(cmap='GnBu')
corrstyle.to_html('./秩相关系数.html')

# 计算综合指标与以下副指标的p值:scl、scg、sce
res = scipy.stats.spearmanr(sci['SmartCity_Index'], sci['Smart_Living'])
print('Smart Living coefficient:', res[0])
print('p-value:', res[1])

res = scipy.stats.pearsonr(sci['SmartCity_Index'], sci['Smart_Government'])
print('Smart Government correlation to Smart City Index')
print('Spearman\'s coeffient:', res[0])
print('p-value:', res[1])

res = scipy.stats.pearsonr(sci['SmartCity_Index'], sci['Smart_People'])
print('Smart People correlation to Smart City Index')
print('Spearman\'s coeffient:', res[0])
print('p-value:', res[1])

res = scipy.stats.pearsonr(sci['SmartCity_Index'], sci['Smart_Environment'])
print('Smart Environment correlation to Smart City Index')
print('Spearman\'s coeffient:', res[0])
print('p-value:', res[1])
# 绘制图像
g = sns.PairGrid(sci, y_vars=['SmartCity_Index'], x_vars=['Smart_People', 'Smart_Government', 'Smart_Living', 'Smart_Environment'])
g.map(sns.regplot)
g.set()