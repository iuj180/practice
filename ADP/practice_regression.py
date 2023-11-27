#빅데이터 분석기사 5회 실기 기출 유형
# [가격 예측] 중고 자동차
# 자동차 가격을 예측해주세요!
# 예측할 값(y): price
# 평가: RMSE (Root Mean Squared Error)
# data: train.csv, test.csv
# [컴피티션 제출 양식] 리더보드 제출용
# 제출 형식: submission.csv파일을 아래와 같은 형식(수치형)으로 제출
# (id는 test의 index임)
# id,price
# 0,11000
# 1,20500
# 2,19610
# ...    
# 1616,11995

import pandas as pd
train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p2_train_.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p2_test_.csv')
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

########## EDA ##########

# # 데이터 기본 형태 확인 shape, info()
# print(train.shape, test.shape)

# # 데이터 기초 통계량 확인. describe(), 범주형만 보려면 describe(include='O')
# print(train.describe())
# print(train.describe(include='O'))
# print(test.describe())
# print(test.describe(include='O'))

# # 범주형 column은 mmodel,transmission,fuelType.
# # model의 unique는 19개로 drop하는 것이 좋겠다. transmission, fuelType은 원핫 인코딩 사용예정
# # 데이터에 결측치가 있는지 확인하자 isnull().sum()
# print(train.isnull().sum())
# print(test.isnull().sum())
# # 결측치가 없는 걸 확인하였다.

########## 데이터 전처리 ##########

# model column은 범주형 데이터의 unique가 19이므로 삭제해주자. drop()
train = train.drop(['model'], axis=1)
test = test.drop(['model'], axis=1)

# 종속변수인 price column을 따로 분리해놓자. pop()
y = train.pop('price')

# print(y)
# print(train)

# 수치형, 범주형 col을 따로 list해서 모아놓기 select_dtypes(include='O'), select_dtypes(exclude='O')
num_cols = train.select_dtypes(exclude='O').columns.to_list()
cat_cols = train.select_dtypes(include='O').columns.to_list()

# print(num_cols, cat_cols)

# 수치형 column의 크기가 달라 스케일링을 진행해주자.
# 이상치에 덜 민감한 RobustScaler를 해보자

from sklearn.preprocessing import RobustScaler
scale = RobustScaler()

# 스케일링 할 때, train은 fit_transform, test는 transform
# 스케일링 한 데이터는 pd.DataFrame 형태로 다시 만들어주자

train[num_cols] = pd.DataFrame(scale.fit_transform(train[num_cols]))
# 또는 train[['year', 'mileage', 'tax', 'mpg', 'engineSize']] = pd.DataFrame(scale.fit_transform(train[['year', 'mileage', 'tax', 'mpg', 'engineSize']]))

test[num_cols] = pd.DataFrame(scale.transform(test[num_cols]))
# 또는 test[['year', 'mileage', 'tax', 'mpg', 'engineSize']] = pd.DataFrame(scale.transform(test[['year', 'mileage', 'tax', 'mpg', 'engineSize']]))

# print(train, test)


# 범주형 데이터를 인코딩 해주자 pd.get_dummies()
train = pd.get_dummies(train)
test = pd.get_dummies(test)
test = test.reindex(columns = train.columns, fill_value=0)
print(train)
print("")
print(test)


########## 학습 ##########

# train으로 바로 학습해도 되지만, train_test_split을 사용해보자
# test_size = 0.2 정도로 해보자
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train, y, test_size=0.2, random_state=2023)
# print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# 간단하고 성능이 좋은 RandomForest를 사용하자. 회귀이므로 RandomForestRegressor 사용
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(random_state=2023)
model.fit(X_train, y_train)
pred = model.predict(X_test)


# rmse로 평가
# rmse는 따로 없으니, sqrt(mse)를 해주자.
from sklearn.metrics import mean_squared_error
import numpy as np

print(np.sqrt(mean_squared_error(y_test, pred)))

# 기본 학습은 3022.912475514873가 나왔다.
# rmse는 값이 적을수록 평가가 좋다.


########## 하이퍼파라미터 튜닝 ##########

# CV는 1분안에 코드 실행이 어렵다고 하니, max_depth = 5~10, n_estimators=500 정도만 해보자

model = RandomForestRegressor(max_depth=10, n_estimators=500, random_state=2023)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print(np.sqrt(mean_squared_error(y_test, pred)))

# RandomForestRegressor(): 3022.912475514873
# RandomForestRegressor(max_depth=10, n_estimators=500) : 3194.0085502871857
# 두번째 평가가 더 좋았다. 두번째 기준으로 최종 test를 학습시키자.

pred = model.predict(test)
print(test)


########## 제출 ##########
submission = pd.DataFrame({'ID':test['ID'],'price':pred}).to_csv('20031107.csv', index=False)
check = pd.read_csv('20031107.csv')
print(check)