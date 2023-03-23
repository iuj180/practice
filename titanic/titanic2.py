

# 1. 데이터 불러오기
import pandas as pd                                                       # pandas 모듈 : 데이터 분석
import seaborn as sns                                                     # seaborn 모듈 : 시각화
import matplotlib as mlt                                                  # matplot 모듈 : 시각화

train=pd.read_csv('D:/blindcat/titanic/train.csv')

# 2. 데이터 전처리
train.head()                                                              # 데이터 처음 5행 조회
train.isnull().sum()                                                      # 결측치 개수 확인
train.info()                                                              # 데이터 타입 확인
train.describe()                                                          # 항목별 기본 통계량
train.hist()                                                              # 항목별 히스토그램

train['Survived'].value_counts()
train['Pclass'].value_counts()
train['Sex'].value_counts()
train['Embarked'].value_counts()

sns.heatmap(train.corr(), annot=True, linewidths=2)                       # 항목별 상관계수 확인
sns.barplot(x=train['Sex'], y=train['Survived'], hue=train['Sex'], dodge=False)
sns.barplot(x='Sex', y='Survived', hue='Sex', data=train, dodge=False)
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=train)
sns.barplot(x='AgeGroup', y='Survived', hue='Pclass', data=train)

train['Sex']=train['Sex'].map({'female':1, 'male':0})                     # 문자열 숫자로 변환

train['Age'].fillna(value=train['Age'].mean(), inplace=True)              # 결측치 채워주기

train['FirstClass']=train['Pclass'].apply(lambda x:1 if x==1 else 0)      # FirstClass 열 생성하기
train['SecondClass']=train['Pclass'].apply(lambda x:1 if x==2 else 0)     # SecondClass 열 생성하기
#DataFrame명.apply(lambda x: x['칼럼명']들의 조건식
#                          if x['칼럼명']들의 조건식
#                          elxe (x['칼럼명']들의 조건식 또는 값), axis=1)

features=train[['Sex', 'Age', 'FirstClass', 'SecondClass']]               # feature 분리하기
survival=train['Survived']

# 3. 학습세트/평가세트 분리하기
from sklearn.model_selection import train_test_split                      
train_features, test_features, train_labels, test_labels=train_test_split(features, survival)

# 4. 데이터 정규화 (스케일링) 하기
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
train_features=scaler.fit_transform(train_features)                       # train 데이터 정규화
test_features=scaler.transform(test_features)                             # test 데이터 정규화

# 5. 모델 생성 및 평가하기
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(train_features, train_labels)

print(model.score(train_features, train_labels))                          # 학습세트 정확도 확인
print(model.score(test_features, test_labels))

print(model.coef_)                                                        # 각 feature 계수 확인

# 6. 예측하기
import numpy as np                                                        # numpy 모듈 : 데이터 분석

Jack = np.array([0.0, 20.0, 0.0, 0.0])                                    # 배열 객체 만들기
Rose = np.array([1.0, 17.0, 1.0, 0.0])
JW = np.array([0.0, 45.0, 1.0, 0.0])
sample_train=np.array([Jack, Rose, JW])                                   # 배열 객체 합치기

sample_train=scaler.transform(sample_train)                               # 새로운 데이터 정규화

print(model.predict(sample_train))                                        # 예측 결과 확인 (suvival 결과)
print(model.predict_proba(sample_train))                                  # 예측 확률 확인
