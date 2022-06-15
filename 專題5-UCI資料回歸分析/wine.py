import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
# 匯入資料，這邊是用我電腦上的路徑，請自行修改
dfred = pd.read_csv('C:/Users/user/Desktop/OneDrive_1_2021-6-26/R/data/winequality-red2.csv', sep = ',')

correlation_matrixred = dfred.corr().round(2)

sns.heatmap(data=correlation_matrixred, annot = True)

dfred.shape
# (1599, 12)

dfred.isnull().sum()
# fixed acidity           0
# volatile acidity        0
# citric acid             0
# residual sugar          0
# chlorides               0
# free sulfur dioxide     0
# total sulfur dioxide    0
# density                 0
# pH                      0
# sulphates               0
# alcohol                 0
# quality                 0
# dtype: int64

# 各個項目與"品質"的關係
y2=dfred['quality']

plt.subplot(231)
plt.scatter(dfred['fixed acidity'], y2, linewidths=0.1)
plt.title(label='fixed acidity-quality')

plt.subplot(232)
plt.scatter(dfred['volatile acidity'], y2, linewidths=0.1)
plt.title(label='volatile acidity-quality')

plt.subplot(233)
plt.scatter(dfred['citric acid'], y2, linewidths=0.1)
plt.title(label='citric acid-quality')

plt.subplot(234)
plt.scatter(dfred['residual sugar'], y2, linewidths=0.1)
plt.title(label='residual sugar-quality')

plt.subplot(235)
plt.scatter(dfred['chlorides'], y2, linewidths=0.1)
plt.title(label='chlorides-quality')

plt.subplot(236)
plt.scatter(dfred['free sulfur dioxide'], y2, linewidths=0.1)
plt.title(label='free sulfur dioxide-quality')

plt.show()
###------------------------------------------------------
plt.subplot(231)
plt.scatter(dfred['total sulfur dioxide'], y2, linewidths=0.1)
plt.title(label='total sulfur dioxide-quality')

plt.subplot(232)
plt.scatter(dfred['density'], y2, linewidths=0.1)
plt.title(label='density-quality')

plt.subplot(233)
plt.scatter(dfred['pH'], y2, linewidths=0.1)
plt.title(label='pH-quality')

plt.subplot(234)
plt.scatter(dfred['sulphates'], y2, linewidths=0.1)
plt.title(label='sulphates-quality')

plt.subplot(235)
plt.scatter(dfred['alcohol'], y2, linewidths=0.1)
plt.title(label='alcohol-quality')
plt.show()


X = pd.DataFrame(np.c_[dfred['volatile acidity'],dfred['chlorides'],dfred['total sulfur dioxide'],dfred['sulphates'],dfred['alcohol']], columns = ['volatile acidity','chlorides','total sulfur dioxide','sulphates','alcohol'])
y = dfred['quality']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)

reg = LinearRegression()

reg.fit(X_train,y_train)

reg.predict(X_test)

Y_pred = reg.predict(X_test)
plt.scatter(Y_pred, y_test)
plt.xlabel('Y_pred')
plt.ylabel('y_test')
plt.show()

print(X_train.shape) 
print(X_test.shape) 
print(y_train.shape) 
print(y_test.shape) 

coeff_df = pd.DataFrame(reg.coef_, X_train.columns, columns=['Coefficient'])  

print('R2: ', reg.score(X_test, y_test))
print('intercept:',reg.intercept_)
print(coeff_df)
# R2:  0.3816379037532992
# intercept: 3.2485805427283436
#                       Coefficient
# volatile acidity        -1.225973
# chlorides               -1.762929
# total sulfur dioxide    -0.002157
# sulphates                0.902243
# alcohol                  0.258064

import statsmodels.api as sm

X3, y3 = dfred.loc[:, ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']], dfred.loc[:, ['quality']]
X3 = sm.add_constant(X3)  
model = sm.OLS(y3, X3)
result = model.fit()
print('迴歸係數：', result.params)
result.summary()

# 迴歸係數： 
# const                   21.965208
# fixed acidity            0.024991
# volatile acidity        -1.083590
# citric acid             -0.182564
# residual sugar           0.016331
# chlorides               -1.874225
# free sulfur dioxide      0.004361
# total sulfur dioxide    -0.003265
# density                -17.881164
# pH                      -0.413653
# sulphates                0.916334
# alcohol                  0.276198
# dtype: float64

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                quality   R-squared:                       0.361
Model:                            OLS   Adj. R-squared:                  0.356
Method:                 Least Squares   F-statistic:                     81.35
Date:                Thu, 09 Sep 2021   Prob (F-statistic):          1.79e-145
Time:                        04:55:40   Log-Likelihood:                -1569.1
No. Observations:                1599   AIC:                             3162.
Df Residuals:                    1587   BIC:                             3227.
Df Model:                          11                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                   21.9652     21.195      1.036      0.300     -19.607      63.538
fixed acidity            0.0250      0.026      0.963      0.336      -0.026       0.076
volatile acidity        -1.0836      0.121     -8.948      0.000      -1.321      -0.846
citric acid             -0.1826      0.147     -1.240      0.215      -0.471       0.106
residual sugar           0.0163      0.015      1.089      0.276      -0.013       0.046
chlorides               -1.8742      0.419     -4.470      0.000      -2.697      -1.052
free sulfur dioxide      0.0044      0.002      2.009      0.045       0.000       0.009
total sulfur dioxide    -0.0033      0.001     -4.480      0.000      -0.005      -0.002
density                -17.8812     21.633     -0.827      0.409     -60.314      24.551
pH                      -0.4137      0.192     -2.159      0.031      -0.789      -0.038
sulphates                0.9163      0.114      8.014      0.000       0.692       1.141
alcohol                  0.2762      0.026     10.429      0.000       0.224       0.328
==============================================================================
Omnibus:                       27.376   Durbin-Watson:                   1.757
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               40.965
Skew:                          -0.168   Prob(JB):                     1.27e-09
Kurtosis:                       3.708   Cond. No.                     1.13e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.13e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

# In[]
dfwhite = pd.read_csv('C:/Users/user/Desktop/OneDrive_1_2021-6-26/R/data/winequality-white2.csv', sep = ',')

dfwhite.shape
# (4898, 12)

dfwhite.isnull().sum()
# fixed acidity           0
# volatile acidity        0
# citric acid             0
# residual sugar          0
# chlorides               0
# free sulfur dioxide     0
# total sulfur dioxide    0
# density                 0
# pH                      0
# sulphates               0
# alcohol                 0
# quality                 0
# dtype: int64
correlation_matrixwhite = dfwhite.corr().round(2)

sns.heatmap(data=correlation_matrixwhite, annot = True)

y1=dfwhite['quality']

plt.subplot(231)
plt.scatter(dfwhite['fixed acidity'], y1, linewidths=0.1)
plt.title(label='fixed acidity-quality')

plt.subplot(232)
plt.scatter(dfwhite['volatile acidity'], y1, linewidths=0.1)
plt.title(label='volatile acidity-quality')

plt.subplot(233)
plt.scatter(dfwhite['citric acid'], y1, linewidths=0.1)
plt.title(label='citric acid-quality')

plt.subplot(234)
plt.scatter(dfwhite['residual sugar'], y1, linewidths=0.1)
plt.title(label='residual sugar-quality')

plt.subplot(235)
plt.scatter(dfwhite['chlorides'], y1, linewidths=0.1)
plt.title(label='chlorides-quality')

plt.subplot(236)
plt.scatter(dfwhite['free sulfur dioxide'], y1, linewidths=0.1)
plt.title(label='free sulfur dioxide-quality')

plt.show()
###------------------------------------------------------
plt.subplot(231)
plt.scatter(dfwhite['total sulfur dioxide'], y1, linewidths=0.1)
plt.title(label='total sulfur dioxide-quality')

plt.subplot(232)
plt.scatter(dfwhite['density'], y1, linewidths=0.1)
plt.title(label='density-quality')

plt.subplot(233)
plt.scatter(dfwhite['pH'], y1, linewidths=0.1)
plt.title(label='pH-quality')

plt.subplot(234)
plt.scatter(dfwhite['sulphates'], y1, linewidths=0.1)
plt.title(label='sulphates-quality')

plt.subplot(235)
plt.scatter(dfwhite['alcohol'], y1, linewidths=0.1)
plt.title(label='alcohol-quality')
plt.show()

X2 = pd.DataFrame(np.c_[dfwhite['volatile acidity'],dfwhite['residual sugar'],dfwhite['free sulfur dioxide'],dfwhite['density'],dfwhite['pH'],dfwhite['sulphates'],dfwhite['alcohol']], columns = ['volatile acidity','residual sugar','free sulfur dioxide','density','pH','sulphates','alcohol'])
y2 = dfwhite['quality']
from sklearn.model_selection import train_test_split
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size = 0.2, random_state=5)

reg = LinearRegression()

reg.fit(X2_train,y2_train)

reg.predict(X2_test)

Y2_pred = reg.predict(X2_test)
plt.scatter(Y2_pred, y2_test)
plt.xlabel('Y2_pred')
plt.ylabel('y2_test')
plt.show()

print(X2_train.shape)
print(X2_test.shape) 
print(y2_train.shape) 
print(y2_test.shape)

coeff_df = pd.DataFrame(reg.coef_, X2_train.columns, columns=['Coefficient'])  


print('R2: ', reg.score(X2_test, y2_test))
print('intercept:',reg.intercept_)
print(coeff_df)
# R2:  0.2937453356267793
# intercept: 109.73733717426884
#                      Coefficient
# volatile acidity       -1.900095
# residual sugar          0.065381
# free sulfur dioxide     0.003557
# density              -108.814577
# pH                      0.432620
# sulphates               0.543768
# alcohol                 0.252183

import statsmodels.api as sm

X4, y4 = dfwhite.loc[:, ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']], dfwhite.loc[:, ['quality']]
X4 = sm.add_constant(X4)  
model = sm.OLS(y4, X4)
result = model.fit()
print('迴歸係數：', result.params)
result.summary()

# 迴歸係數： 
# const                   150.192842
# fixed acidity             0.065520
# volatile acidity         -1.863177
# citric acid               0.022090
# residual sugar            0.081483
# chlorides                -0.247277
# free sulfur dioxide       0.003733
# total sulfur dioxide     -0.000286
# density                -150.284181
# pH                        0.686344
# sulphates                 0.631476
# alcohol                   0.193476
# dtype: float64

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                quality   R-squared:                       0.282
Model:                            OLS   Adj. R-squared:                  0.280
Method:                 Least Squares   F-statistic:                     174.3
Date:                Thu, 09 Sep 2021   Prob (F-statistic):               0.00
Time:                        05:01:57   Log-Likelihood:                -5543.7
No. Observations:                4898   AIC:                         1.111e+04
Df Residuals:                    4886   BIC:                         1.119e+04
Df Model:                          11                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                  150.1928     18.804      7.987      0.000     113.328     187.057
fixed acidity            0.0655      0.021      3.139      0.002       0.025       0.106
volatile acidity        -1.8632      0.114    -16.373      0.000      -2.086      -1.640
citric acid              0.0221      0.096      0.231      0.818      -0.166       0.210
residual sugar           0.0815      0.008     10.825      0.000       0.067       0.096
chlorides               -0.2473      0.547     -0.452      0.651      -1.319       0.824
free sulfur dioxide      0.0037      0.001      4.422      0.000       0.002       0.005
total sulfur dioxide    -0.0003      0.000     -0.756      0.450      -0.001       0.000
density               -150.2842     19.075     -7.879      0.000    -187.679    -112.890
pH                       0.6863      0.105      6.513      0.000       0.480       0.893
sulphates                0.6315      0.100      6.291      0.000       0.435       0.828
alcohol                  0.1935      0.024      7.988      0.000       0.146       0.241
==============================================================================
Omnibus:                      114.161   Durbin-Watson:                   1.621
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              251.637
Skew:                           0.073   Prob(JB):                     2.28e-55
Kurtosis:                       4.101   Cond. No.                     3.74e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.74e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

