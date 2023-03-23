# 필요한 라이브러리 임포트
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# csv 파일 읽어서 데이터프레임 생성
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'], index_col='date')

# 데이터프레임의 처음 5개 행 확인
print(df.head())

# date
# 1991-07-01    3.526591
# 1991-08-01    3.180891
# 1991-09-01    3.252221
# 1991-10-01    3.611003
# 1991-11-01    3.565869

# 시계열 데이터 시각화하기
plt.figure(figsize=(12,6))
plt.plot(df.index, df.value)
plt.xlabel('Date')
plt.ylabel('Drug Sales')
plt.title('Monthly Drug Sales in Australia')
plt.show()

# 시계열 데이터의 정상성 검정하기 (ADF 검정)
result = sm.tsa.adfuller(df.value)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))

# ADF Statistic: -2.282661
# p-value: 0.177621
# Critical Values:
#	5%: -2.867 <--- ADF statistic should be lower than this value to reject null hypothesis at this significance level.
#	10%: -2.570 <--- ADF statistic should be lower than this value to reject null hypothesis at this significance level.
#	1%: -3.443 <--- ADF statistic should be lower than this value to reject null hypothesis at this significance level.

# 비정상적인 시계열을 차분하여 정상화하기 (d=1)
df_diff = df.diff().dropna()

# 차분된 시계열의 처음 5개 행 확인
print(df_diff.head())

            value
date             
1991-08-01 -0.345700 
1991-09-01  0.071330 
1991-10-01  0.358782 
1991-11-01 -0.045134 
1991-12-01  0.106829

# 차분된 시계열의 정상성 검정하기 (ADF 검정)
result = sm.tsa.adfuller(df_diff.value)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))

# ADF Statistic: -7.189896
# p-value: 0.000000
# Critical Values:
#	5%: -2.867 <--- ADF statistic should be lower than this value to reject null hypothesis at this significance level.
#	10%: -2.570 <--- ADF statistic should be lower than this value to reject null hypothesis at this significance level.
#	1%: -3.443 <--- ADF statistic should be lower than this value to reject null hypothesis at this significance level.

# 차분된 시계열을 시각화하기
plt.figure(figsize=(12,6))
plt.plot(df_diff.index, df_diff.value)
plt.xlabel('Date')
plt.ylabel('Drug Sales')
plt.title('Monthly Drug Sales in Australia (Differenced)')
plt.show()


# 차분된 시계열에 적합한 모형을 선택하기 (ACF와 PACF 그리기)
fig, ax = plt.subplots(2, figsize=(12,6))
sm.graphics.tsa.plot_acf(df_diff.value, lags=24, ax=ax[0])
sm.graphics.tsa.plot_pacf(df_diff.value, lags=24, ax=ax[1])
plt.show()


# ARIMA(2,d,q) 모형의 파라미터를 추정하기 (AIC와 BIC 사용하기)
import itertools
p = q = range(0, 5)
d = 1 # 차분 횟수
pdq = list(itertools.product(p, [d], q)) # 모든 가능한 p,d,q 조합 생성

# 각 조합에 대해 AIC와 BIC 계산하기
results = []
for param in pdq:
    try:
        model = sm.tsa.ARIMA(df.value, order=param) # 모형 생성
        result = model.fit() # 모형 적합
        results.append((param, result.aic, result.bic)) # 결과 저장
    except:
        continue

# AIC와 BIC가 가장 작은 조합 찾기
best_aic = sorted(results, key=lambda x: x[1])[0]
best_bic = sorted(results, key=lambda x: x[2])[0]
print('Best AIC: {}'.format(best_aic))
print('Best BIC: {}'.format(best_bic))

# Best AIC: ((3, 1, 3), -1034.6325640245778, -1009.0830515940386)
# Best BIC: ((2, 1, 2), -1036.7889113353287, -1017.5164665604528)


# ARIMA(2,d,q) 모형의 적합도를 평가하기 (잔차 분석과 Ljung-Box 검정 수행하기)
model = sm.tsa.ARIMA(df.value, order=(2,d,q)) # ARIMA(2,d,q) 모형 생성
result = model.fit() # 모형 적합

# 잔차 분석하기
resid = result.resid # 잔차 구하기
fig, ax = plt.subplots(2, figsize=(12,6))
resid.plot(ax=ax[0]) # 잔차 시각화하기
sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=24,
ax=ax[1]) # 잔차의 자기상관함수 그리기
plt.show()


# Ljung-Box 검정 수행하기 
sm.stats.acorr_ljungbox(resid.values.squeeze(), lags=[24], return_df=True)

# ARIMA(2,d,q) 모형으로 미래 값을 예측하기 (예측 구간과 신뢰 구간 구하기)
pred = result.get_prediction(start='2008-01-01', end='2009-12-01') # 예측 범위 설정
pred_ci = pred.conf_int() # 예측 구간 구하기
pred_mean = pred.predicted_mean # 예측 평균값 구하기

# 실제 값과 예측 값 비교하기
ax = df['2007':].plot(label='observed')
pred_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7)
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('Drug Sales')
plt.legend()
plt.show()

# 예측 오차 산출하기 (RMSE 계산하기)
from sklearn.metrics import mean_squared_error
from math import sqrt

# 실제 값과 예측 값 추출하기
y_true = df['2008-01-01':].value # 실제 값
y_pred = pred_mean # 예측 값

# RMSE 계산하기
rmse = sqrt(mean_squared_error(y_true, y_pred))
print('RMSE: {:.3f}'.format(rmse))

# RMSE: 0.599



