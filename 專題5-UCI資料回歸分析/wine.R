winequality.red <- read.csv("C:/Users/user/Desktop/OneDrive_1_2021-6-26/R/data/winequality-red.csv", sep=";")

View(winequality.red)

summary(winequality.red)
# fixed.acidity   volatile.acidity  citric.acid    residual.sugar  
# Min.   : 4.60   Min.   :0.1200   Min.   :0.000   Min.   : 0.900  
# 1st Qu.: 7.10   1st Qu.:0.3900   1st Qu.:0.090   1st Qu.: 1.900  
# Median : 7.90   Median :0.5200   Median :0.260   Median : 2.200  
# Mean   : 8.32   Mean   :0.5278   Mean   :0.271   Mean   : 2.539  
# 3rd Qu.: 9.20   3rd Qu.:0.6400   3rd Qu.:0.420   3rd Qu.: 2.600  
# Max.   :15.90   Max.   :1.5800   Max.   :1.000   Max.   :15.500  
#     chlorides       free.sulfur.dioxide total.sulfur.dioxide    density      
# Min.   :0.01200   Min.   : 1.00       Min.   :  6.00       Min.   :0.9901  
# 1st Qu.:0.07000   1st Qu.: 7.00       1st Qu.: 22.00       1st Qu.:0.9956  
# Median :0.07900   Median :14.00       Median : 38.00       Median :0.9968  
# Mean   :0.08747   Mean   :15.87       Mean   : 46.47       Mean   :0.9967  
# 3rd Qu.:0.09000   3rd Qu.:21.00       3rd Qu.: 62.00       3rd Qu.:0.9978  
# Max.   :0.61100   Max.   :72.00       Max.   :289.00       Max.   :1.0037  
#          pH          sulphates         alcohol         quality     
# Min.   :2.740   Min.   :0.3300   Min.   : 8.40   Min.   :3.000  
# 1st Qu.:3.210   1st Qu.:0.5500   1st Qu.: 9.50   1st Qu.:5.000  
# Median :3.310   Median :0.6200   Median :10.20   Median :6.000  
# Mean   :3.311   Mean   :0.6581   Mean   :10.42   Mean   :5.636  
# 3rd Qu.:3.400   3rd Qu.:0.7300   3rd Qu.:11.10   3rd Qu.:6.000  
# Max.   :4.010   Max.   :2.0000   Max.   :14.90   Max.   :8.000  
# -------------------------------------------
par(mfrow=c(1,3))
boxplot(winequality.red$fixed.acidity)$out
boxplot(winequality.red$volatile.acidity)$out
boxplot(winequality.red$citric.acid)$out

par(mfrow=c(1,3))
boxplot(winequality.red$residual.sugar)$out
boxplot(winequality.red$chlorides)$out
boxplot(winequality.red$free.sulfur.dioxide)$out

par(mfrow=c(1,3))
boxplot(winequality.red$total.sulfur.dioxide)$out
boxplot(winequality.red$density)$out
boxplot(winequality.red$pH)$out

par(mfrow=c(1,2))
boxplot(winequality.red$sulphates)$out
boxplot(winequality.red$alcohol)$out
# -----------------------------------------------------
plot(winequality.red$fixed.acidity, winequality.red$quality, type="p", main="fixed acidity-quality",xlab="fixed acidity", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~fixed.acidity,data=winequality.red),col="red")

plot(winequality.red$volatile.acidity, winequality.red$quality, type="p", main="volatile acidity-quality",xlab="volatile.acidity", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~volatile.acidity,data=winequality.red),col="red")

plot(winequality.red$citric.acid, winequality.red$quality, type="p", main="citric.acid-quality",xlab="citric.acid", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~citric.acid,data=winequality.red),col="red")

plot(winequality.red$residual.sugar, winequality.red$quality, type="p", main="residual.sugar-quality",xlab="residual.sugar", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~residual.sugar,data=winequality.red),col="red")

plot(winequality.red$chlorides, winequality.red$quality, type="p", main="chlorides-quality",xlab="chlorides", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~chlorides,data=winequality.red),col="red")

plot(winequality.red$free.sulfur.dioxide, winequality.red$quality, type="p", main="free.sulfur.dioxide-quality",xlab="free.sulfur.dioxide", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~free.sulfur.dioxide,data=winequality.red),col="red")

plot(winequality.red$total.sulfur.dioxide, winequality.red$quality, type="p", main="total.sulfur.dioxide-quality",xlab="total.sulfur.dioxide", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~total.sulfur.dioxide,data=winequality.red),col="red")

plot(winequality.red$density, winequality.red$quality, type="p", main="density-quality",xlab="density", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~density,data=winequality.red),col="red")

plot(winequality.red$pH, winequality.red$quality, type="p", main="pH-quality",xlab="pH", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~pH,data=winequality.red),col="red")

plot(winequality.red$sulphates, winequality.red$quality, type="p", main="sulphates-quality",xlab="sulphates", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~sulphates,data=winequality.red),col="red")

plot(winequality.red$alcohol, winequality.red$quality, type="p", main="alcohol-quality",xlab="alcohol", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~alcohol,data=winequality.red),col="red")

# ---------------------------------------------
GGally::ggpairs(winequality.red[,])
# 查看相關係數,分布圖,需先安裝GGally
RES_01=lm(quality~.,data=winequality.red)

RES_01

# Call:
#   lm(formula = quality ~ ., data = winequality.red)
# 
# Coefficients:
#   (Intercept)         fixed.acidity      volatile.acidity  
# 21.965208              0.024991             -1.083590  
# citric.acid        residual.sugar             chlorides  
# -0.182564              0.016331             -1.874225  
# free.sulfur.dioxide  total.sulfur.dioxide     density  
# 0.004361             -0.003265            -17.881164  
#      pH             sulphates               alcohol  
# -0.413653              0.916334              0.276198  

summary(RES_01)

# Call:
#   lm(formula = quality ~ ., data = winequality.red)
# 
# Residuals:
#   Min       1Q   Median       3Q      Max 
# -2.68911 -0.36652 -0.04699  0.45202  2.02498 
# 
# Coefficients:
#                          Estimate Std. Error t value Pr(>|t|)    
#   (Intercept)           2.197e+01  2.119e+01   1.036   0.3002    
#   fixed.acidity         2.499e-02  2.595e-02   0.963   0.3357    
#   volatile.acidity     -1.084e+00  1.211e-01  -8.948  < 2e-16 ***
#   citric.acid          -1.826e-01  1.472e-01  -1.240   0.2150    
#   residual.sugar        1.633e-02  1.500e-02   1.089   0.2765    
#   chlorides            -1.874e+00  4.193e-01  -4.470 8.37e-06 ***
#   free.sulfur.dioxide   4.361e-03  2.171e-03   2.009   0.0447 *  
#   total.sulfur.dioxide -3.265e-03  7.287e-04  -4.480 8.00e-06 ***
#   density              -1.788e+01  2.163e+01  -0.827   0.4086    
#   pH                   -4.137e-01  1.916e-01  -2.159   0.0310 *  
#   sulphates             9.163e-01  1.143e-01   8.014 2.13e-15 ***
#   alcohol               2.762e-01  2.648e-02  10.429  < 2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.648 on 1587 degrees of freedom
# Multiple R-squared:  0.3606,	Adjusted R-squared:  0.3561 
# F-statistic: 81.35 on 11 and 1587 DF,  p-value: < 2.2e-16

RES_011=lm(quality~volatile.acidity+chlorides+total.sulfur.dioxide+sulphates+alcohol,data=winequality.red)

summary(RES_011)
# Call:
#   lm(formula = quality ~ volatile.acidity + chlorides + total.sulfur.dioxide + 
#        sulphates + alcohol, data = winequality.red)
# 
# Residuals:
#   Min       1Q   Median       3Q      Max 
# -2.67443 -0.38254 -0.06368  0.44893  2.07310 
# 
# Coefficients:
#                           Estimate Std. Error t value Pr(>|t|)    
#   (Intercept)           3.0048920  0.2037663  14.747  < 2e-16 ***
#   volatile.acidity     -1.1419024  0.0969400 -11.779  < 2e-16 ***
#   chlorides            -1.7047871  0.3916886  -4.352 1.43e-05 ***
#   total.sulfur.dioxide -0.0023096  0.0005082  -4.544 5.92e-06 ***
#   sulphates             0.9148320  0.1102702   8.296 2.26e-16 ***
#   alcohol               0.2770979  0.0164836  16.811  < 2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.6514 on 1593 degrees of freedom
# Multiple R-squared:  0.3515,	Adjusted R-squared:  0.3495 
# F-statistic: 172.7 on 5 and 1593 DF,  p-value: < 2.2e-16

winequality.white <- read.csv("C:/Users/user/Desktop/OneDrive_1_2021-6-26/R/data/winequality-white.csv", sep=";")

View(winequality.white)

summary(winequality.white)

# fixed.acidity    volatile.acidity  citric.acid     residual.sugar  
# Min.   : 3.800   Min.   :0.0800   Min.   :0.0000   Min.   : 0.600  
# 1st Qu.: 6.300   1st Qu.:0.2100   1st Qu.:0.2700   1st Qu.: 1.700  
# Median : 6.800   Median :0.2600   Median :0.3200   Median : 5.200  
# Mean   : 6.855   Mean   :0.2782   Mean   :0.3342   Mean   : 6.391  
# 3rd Qu.: 7.300   3rd Qu.:0.3200   3rd Qu.:0.3900   3rd Qu.: 9.900  
# Max.   :14.200   Max.   :1.1000   Max.   :1.6600   Max.   :65.800  
#     chlorides       free.sulfur.dioxide total.sulfur.dioxide    density      
# Min.   :0.00900   Min.   :  2.00      Min.   :  9.0        Min.   :0.9871  
# 1st Qu.:0.03600   1st Qu.: 23.00      1st Qu.:108.0        1st Qu.:0.9917  
# Median :0.04300   Median : 34.00      Median :134.0        Median :0.9937  
# Mean   :0.04577   Mean   : 35.31      Mean   :138.4        Mean   :0.9940  
# 3rd Qu.:0.05000   3rd Qu.: 46.00      3rd Qu.:167.0        3rd Qu.:0.9961  
# Max.   :0.34600   Max.   :289.00      Max.   :440.0        Max.   :1.0390  
#          pH          sulphates         alcohol         quality     
# Min.   :2.720   Min.   :0.2200   Min.   : 8.00   Min.   :3.000  
# 1st Qu.:3.090   1st Qu.:0.4100   1st Qu.: 9.50   1st Qu.:5.000  
# Median :3.180   Median :0.4700   Median :10.40   Median :6.000  
# Mean   :3.188   Mean   :0.4898   Mean   :10.51   Mean   :5.878  
# 3rd Qu.:3.280   3rd Qu.:0.5500   3rd Qu.:11.40   3rd Qu.:6.000  
# Max.   :3.820   Max.   :1.0800   Max.   :14.20   Max.   :9.000 

par(mfrow=c(1,3))
boxplot(winequality.white$fixed.acidity)$out
boxplot(winequality.white$volatile.acidity)$out
boxplot(winequality.white$citric.acid)$out

par(mfrow=c(1,3))
boxplot(winequality.white$residual.sugar)$out
boxplot(winequality.white$chlorides)$out
boxplot(winequality.white$free.sulfur.dioxide)$out

par(mfrow=c(1,3))
boxplot(winequality.white$total.sulfur.dioxide)$out
boxplot(winequality.white$density)$out
boxplot(winequality.white$pH)$out

par(mfrow=c(1,2))
boxplot(winequality.white$sulphates)$out
boxplot(winequality.white$alcohol)$out
# -------------------------------------------------------------
plot(winequality.white$fixed.acidity, winequality.white$quality, type="p", main="fixed acidity-quality",xlab="fixed acidity", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~fixed.acidity,data=winequality.white),col="red")

plot(winequality.white$volatile.acidity, winequality.white$quality, type="p", main="volatile acidity-quality",xlab="volatile.acidity", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~volatile.acidity,data=winequality.white),col="red")

plot(winequality.white$citric.acid, winequality.white$quality, type="p", main="citric.acid-quality",xlab="citric.acid", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~citric.acid,data=winequality.white),col="red")

plot(winequality.white$residual.sugar, winequality.white$quality, type="p", main="residual.sugar-quality",xlab="residual.sugar", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~residual.sugar,data=winequality.white),col="red")

plot(winequality.white$chlorides, winequality.white$quality, type="p", main="chlorides-quality",xlab="chlorides", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~chlorides,data=winequality.white),col="red")

plot(winequality.white$free.sulfur.dioxide, winequality.white$quality, type="p", main="free.sulfur.dioxide-quality",xlab="free.sulfur.dioxide", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~free.sulfur.dioxide,data=winequality.white),col="red")

plot(winequality.white$total.sulfur.dioxide, winequality.white$quality, type="p", main="total.sulfur.dioxide-quality",xlab="total.sulfur.dioxide", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~total.sulfur.dioxide,data=winequality.white),col="red")

plot(winequality.white$density, winequality.white$quality, type="p", main="density-quality",xlab="density", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~density,data=winequality.white),col="red")

plot(winequality.white$pH, winequality.white$quality, type="p", main="pH-quality",xlab="pH", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~pH,data=winequality.white),col="red")

plot(winequality.white$sulphates, winequality.white$quality, type="p", main="sulphates-quality",xlab="sulphates", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~sulphates,data=winequality.white),col="red")

plot(winequality.white$alcohol, winequality.white$quality, type="p", main="alcohol-quality",xlab="alcohol", ylab="quality", col="dark blue", pch=16)
abline(lm(quality~alcohol,data=winequality.white),col="red")

# ------------------------------------------------------------
GGally::ggpairs(winequality.white[,])

RES_02=lm(quality~.,data=winequality.white)

RES_02


# Call:
#   lm(formula = quality ~ ., data = winequality.white)
# 
# Coefficients:
#   (Intercept)         fixed.acidity      volatile.acidity  
# 1.502e+02             6.552e-02            -1.863e+00  
# citric.acid        residual.sugar             chlorides  
# 2.209e-02             8.148e-02            -2.473e-01  
# free.sulfur.dioxide  total.sulfur.dioxide               density  
# 3.733e-03            -2.857e-04            -1.503e+02  
# pH             sulphates               alcohol  
# 6.863e-01             6.315e-01             1.935e-01  

summary(RES_02)
# Call:
#   lm(formula = quality ~ ., data = winequality.white)
# 
# Residuals:
#   Min      1Q  Median      3Q     Max 
# -3.8348 -0.4934 -0.0379  0.4637  3.1143 
# 
# Coefficients:
#                         Estimate Std. Error t value Pr(>|t|)    
#   (Intercept)           1.502e+02  1.880e+01   7.987 1.71e-15 ***
#   fixed.acidity         6.552e-02  2.087e-02   3.139  0.00171 ** 
#   volatile.acidity     -1.863e+00  1.138e-01 -16.373  < 2e-16 ***
#   citric.acid           2.209e-02  9.577e-02   0.231  0.81759    
#   residual.sugar        8.148e-02  7.527e-03  10.825  < 2e-16 ***
#   chlorides            -2.473e-01  5.465e-01  -0.452  0.65097    
#   free.sulfur.dioxide   3.733e-03  8.441e-04   4.422 9.99e-06 ***
#   total.sulfur.dioxide -2.857e-04  3.781e-04  -0.756  0.44979    
#   density              -1.503e+02  1.907e+01  -7.879 4.04e-15 ***
#   pH                    6.863e-01  1.054e-01   6.513 8.10e-11 ***
#   sulphates             6.315e-01  1.004e-01   6.291 3.44e-10 ***
#   alcohol               1.935e-01  2.422e-02   7.988 1.70e-15 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.7514 on 4886 degrees of freedom
# Multiple R-squared:  0.2819,	Adjusted R-squared:  0.2803 
# F-statistic: 174.3 on 11 and 4886 DF,  p-value: < 2.2e-16

RES_022=lm(quality~volatile.acidity+residual.sugar+free.sulfur.dioxide+density+pH+sulphates+alcohol,data=winequality.white)

summary(RES_022)
# Call:
#   lm(formula = quality ~ volatile.acidity + residual.sugar + free.sulfur.dioxide + 
#        density + pH + sulphates + alcohol, data = winequality.white)
# 
# Residuals:
#   Min      1Q  Median      3Q     Max 
# -3.8107 -0.4999 -0.0375  0.4636  3.2180 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
#   (Intercept)          1.112e+02  1.273e+01   8.734  < 2e-16 ***
#   volatile.acidity    -1.940e+00  1.085e-01 -17.872  < 2e-16 ***
#   residual.sugar       6.637e-02  5.358e-03  12.386  < 2e-16 ***
#   free.sulfur.dioxide  3.283e-03  6.770e-04   4.849 1.28e-06 ***
#   density             -1.103e+02  1.274e+01  -8.653  < 2e-16 ***
#   pH                   4.619e-01  7.638e-02   6.046 1.59e-09 ***
#   sulphates            5.708e-01  9.856e-02   5.791 7.42e-09 ***
#   alcohol              2.438e-01  1.870e-02  13.035  < 2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.752 on 4890 degrees of freedom
# Multiple R-squared:  0.2801,	Adjusted R-squared:  0.2791 
# F-statistic: 271.8 on 7 and 4890 DF,  p-value: < 2.2e-16