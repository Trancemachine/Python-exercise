import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# 读取数据
df = pd.read_csv('D:\python\数分\ev\ElectricCarData_Clean.csv')
# 数据清洗、整理
df.isnull().sum()
df.isna().sum()
df.info()

# 分析数据
a = np.arange(1, 104)
# 双变量关系
sns.pairplot(df, hue='RapidCharge')
# 热力图相关性
plt.figure(figsize=(15, 8))
sns.heatmap(df.corr(), linewidths=1, linecolor='white', annot=True)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('变量相关性热力图', fontsize=20)
# 品牌频率
plt.figure(figsize=(20, 5))
sns.barplot(x='Brand', y=a, data=df)
plt.grid(axis='y')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('品牌频率', fontsize=25)
plt.xlabel('Brand')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
# 品牌最高速度
plt.figure(figsize=(20, 5))
sns.barplot(x='Brand', y='TopSpeed_KmH', data=df, palette='Spectral_r')
plt.grid(axis='y')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('各品牌最高速度', fontsize=25)
plt.xlabel('Brand')
plt.ylabel('Top Speed')
plt.xticks(rotation=45)
# 各品牌汽车可达到的最大范围
plt.figure(figsize=(20, 5))
sns.barplot(x='Brand', y='Range_Km', data=df, palette='Spectral_r')
plt.grid(axis='y')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('各品牌能达到的最大范围', fontsize=25)
plt.xlabel('Brand')
plt.ylabel('Range')
plt.xticks(rotation=45)
# 汽车功效
plt.figure(figsize=(20, 5))
sns.barplot(x='Brand', y='Efficiency_WhKm', data=df, palette='Spectral_r')
plt.grid(axis='y')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('各品牌汽车功效', fontsize=25)
plt.xlabel('Brand')
plt.ylabel('Efficiency')
plt.xticks(rotation=45)
# 汽车座位数
plt.figure(figsize=(20, 5))
sns.barplot(x='Brand', y='Seats', data=df, palette='Spectral_r')
plt.grid(axis='y')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('汽车座位数', fontsize=25)
plt.xlabel('Brand')
plt.ylabel('Seats')
plt.xticks(rotation=45)
# 汽车价格频率
plt.figure(figsize=(20, 5))
sns.barplot(x='Brand', y='PriceEuro', data=df, palette='Spectral_r')
plt.grid(axis='y')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('各汽车价格频率', fontsize=25)
plt.xlabel('Price in Euro')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
# 插座类型
df['PlugType'].value_counts().plot.\
    pie(figsize=(8, 8), autopct='%.0f%%', explode=(.1,.1,.1,.1), colors=['darkseagreen', 'pink', 'lightskyblue', 'peachpuff'])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('插座类型', fontsize=10)
# .....
# 设置因变量与自变量
x = df[['AccelSec', 'Range_Km', 'TopSpeed_KmH', 'Efficiency_WhKm']]
y = df['PriceEuro']
# 使用最小二乘法建立价格多元回归模型
x = sm.add_constant(x) # 线性回归增加常数项
results = sm.OLS(y, x) # 普通最小二乘模型
model = results.fit()
model.summary()

# 从Scikit Learn 导入训练测试拆分
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)
pred = lr.predict(x_test
from sklearn.metrics import r2_score
r2 = r2_score(y_test, pred)
print(r2*100)

# 将yes设为1， no设为0，进行logistic回归
df['RapidCharge'].replace(to_replace=['No', 'Yes'], value=[0, 1], inplace=True)
x1 = df[['PriceEuro']]
y1 = df[['RapidCharge']]
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.2, random_state=365)
from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
log.fit(x1_train, y1_train)
pred1 = log.predict(x1_test)
pred1
# 回归的混淆矩阵
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y1_test, pred1)
cm
# 找出准确度分数
from sklearn.metrics import accuracy_score
score = accuracy_score(y1_test, pred1)
print(score*100)