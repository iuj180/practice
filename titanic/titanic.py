

#### 1. 데이터 준비 ####




## csv 파일 불러오기 ##
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('D:/blindcat/titanic/train.csv')
test = pd.read_csv('D:/blindcat/titanic/test.csv')







#### 2. EDA ####





train.head()                             # 데이터 셋의 상위 5개 항목 출력

## 결측치 확인 ##                         --> 결측치는 별도 할당을 해주어야 함
train.isnull().sum()
train.isna().sum()
train.isna().sum().sum()

## 데이터 자료형 확인##
train.info()
train.dtypes

## 데이터 분포 ##
train.describe()

## Cabin, Embarked 필드 값확인 ##
train.Cabin.unique()
train.Embarked.unique()

## 생존한 사람, 사망한 사람수 확인 ##
survival=train.Survived.sum()
n_survival=train.shape[0]-survival      # shape[0] : 데이터 행의수

## Pclass 별 탑승객 분포 확인 ##
train['Pclass'].value_counts()

## Sex 별 탑승객 분포 확인 ##
train['Sex'].value_counts()

## Embarked 별 탑승객 분포 확인 ##
train['Embarked'].value_counts()

## Embarked 필드 결측치 할당 ##
train['Embarked']=train['Embarked'].fillna('S')     # S로 할당

## Age 필드 결측치 할당
train['Age']=train['Age'].fillna(train['Age'].median())    # Age필드 중간값 할당

## Name 필드 문자열 추출, Title 필드 할당 ##
train['Title']=train['Name'].str.extract('([a-zA-Z]+)\.', expand=False)           # 대문자로 시작하여 소문자로 나열 .을 만나면 추출

## Title 필드 카테고리 항목 변경 ##
train['Title']=train['Title'].replace(['Capt', 'Col', 'Major', 'Dr', 'Rev'], 'Officer')
train['Title']=train['Title'].replace(['Jonkheer', 'Master'], 'Master')
train['Title']=train['Title'].replace(['Don', 'Sir', 'the Countess', 'Lady', 'Dona'], 'Royalty')
train['Title']=train['Title'].replace(['Mme', 'Ms', 'Mrs'], 'Mrs')
train['Title']=train['Title'].replace(['Mlle', 'Miss'], 'Miss')
train['Title']=train['Title'].replace(['Mr'],'Mr')

## 변수 y 선언, 학습할 목표변수(종속변수) Survived 필드 담기 ##
y=train.Survived

## Age 필드 그룹핑, AgeGroup 필등 생성 ##
bin=[0, 18, 25, 35, 60, 100]
group_names=['Baby', 'Youth', 'YoungAdult', 'MiddleAged', 'Senior']
train['AgeGroup']=pd.cut(train['Age'], bins=bin, labels=group_names)
train['AgeGroup'].value_counts()






##### 데이터 시각화 실습 #####






## 학습 데이터셋(train) 데이터 분포 확인 ##
train.hist(['Age', 'Fare', 'Parch', 'PassengerId', 'Pclass', 'SibSp', 'Survived'])

## 성별 생존여부 데이터 분포 확인 ##
sns.barplot(x=train['Sex'], y=train['Survived'], hue=train['Sex'], dodge=False)
sns.barplot(x='Sex', y='Survived', hue='Sex', data=train, dodge=False)

## 탑승 클래스 (Pclass)별, 성별 (Sex) 생존여부 (Survived) 데이터 분포확인 ##
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=train)

## 전체 변수의 correlation 히트맵 그리기 ##
sns.heatmap(train.corr(), annot=True, linewidths=2)

## 연령분포 (AgeGropu)별, 클래스(Pclass)별 생존여부(Survived) 데이터 분포 ##
sns.barplot(x='AgeGroup', y='Survived', hue='Pclass', data=train)

## 형제/자매(SibSp)별, 클래스(Pclass)별 생존여부(Survived) 데이터 분포 ##
sns.barplot(x='SibSp', y='Survived', hue='Pclass', data=train, dodge=False)





##### 모델 생성 #####



## scikit-learn의 LabelEncoder 모듈 임포트
from sklearn.preprocessing import LabelEncoder

## 학습을 위한 데이터 준비
train=train.drop(['Name', 'Ticket', 'SibSp', 'Parch', 'Cabin'], axis=1)    # drop 메소드 ; 컬럼 삭제

## 변수 타입 변경
train['Sex'].dtypes
train['Sex']=train['Sex'].astype(str)

label=LabelEncoder()
for col in ['Sex', 'Embarked', 'Title', 'AgeGroup']:
    train[col]=label.fit_transform(train[col])

## 학습시킬 변수와 Label 변수 분리
x_train=train[['PassengerId', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Title', 'AgeGroup']]
Y_train=train[['Survived']]

## train dataset의 Survived 컬럼과 다른 변수들간 상관관계 확인
x_train.corr()['Survived']



#### Logistic Regression ####

## 01 필요한 라이브러리 임포트
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()

## 02 Test 데이터셋 로드 
test = pd.read_csv('D:/blindcat/titanic/test.csv')

## 03 Test 데이터셋 null값 확인
test.isnull().sum()

## 04Test 데이터셋 null값 처리
test['Age']=test['Age'].fillna(test['Age'].median())
test['Fare']=test['Fare'].fillna(test['Fare'].mean())

## 05 train 데이터셋과 차원 맞춰주기
test=test.drop(['Age', 'PassengerId', 'Name', 'Ticket', 'SibSp', 'Parch', 'Cabin', 'Embarked'], axis=1)

## 06 Sex 컬럼 자료형 objet--> Int 변환
test['Sex']=label.fit_transform(test['Sex'])

## 07 test 데이터셋 Null 값 확인


## 08 Logistic Regression 모델 예측
pred=lr.predict(test)







# ## 변수별 생존수 시각화 확인 ##
# train[train['Survived']==1]['Sex'].value_counts()   # count 확인
# train[train['Survived']==0]['Sex'].value_counts()   # count 확인

# ## 시각화 함수 만들기 ##
# def bar_chart(feature):
#     survived=train[train['Survived']==1][feature].value_counts()   # 생존자를 카운트
#     dead=train[train['Survived']==0][feature].value_counts()       # 사망자를 카운트

#     df=pd.DataFrame([survived, dead])                              # [생존자, 사망자]를 dataFrame, 행렬구조로 하기 위해서
#     df.index=['Survived', 'Dead']                                  # Index화
#     df.plot(kind='bar', stacked=True, figsize=(10,5))              # 그림을 그림

# bar_chart('Sex')                                                   # 무슨 이류로 남자들이 죽었을까?
# bar_chart('SibSp')                                                 # 함께 탑승한 형제, 배우자 수에 따라서 생존이 왜 다를까?

