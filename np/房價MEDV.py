import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
from sklearn.datasets import load_boston

house = load_boston()
df = pd.DataFrame(data=house.data, 
                  columns=house.feature_names)

# 用 seaborn一次把圖表的美化格式設定好，這裡是只有先設定圖表長寬
sns.set(rc={'figure.figsize':(10,10)})
# 使用的資料是房價MEDV
sns.distplot(df['MEDV'])
plt.show()

df.columns


sns.distplot(df['TAX'])
plt.show()
df['TAX'].max() #711
df['TAX'].min() #187
df['TAX'].std() #168.54

# sns.distplot(df['ZN'])
# plt.show()
# df['ZN'].max() #711
# df['ZN'].min() #187
# df['ZN'].std() #168.54

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
plt.style.use('fivethirtyeight')

df.loc[:, ['TAX']]
df.loc[:, ['MEDV']]
       
x, y = df.loc[:, ['TAX']], df.loc[:, ['MEDV']]

lrRM = LinearRegression()

lrRM.fit(x, y)

print('w_1 =', lrRM.coef_[0])
# w_1 = [9.10210898]
print('w_0 =', lrRM.intercept_)
# w_0 = [-34.67062078]

plt.scatter(x, y, facecolor='xkcd:azure', edgecolor='black', s=20)
plt.xlabel('TAX', fontsize=14)
plt.ylabel("MEDV", fontsize=14)
# plt 繪製迴歸線 y = -34.67062078 + 9.10210898 * x
n_x = np.linspace(x.min(), x.max(), 100)
n_y = lrRM.intercept_ + lrRM.coef_[0] * n_x
plt.plot(n_x, n_y, color='r', lw=3);