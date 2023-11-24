import pandas as pd 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/churnk/X_test.csv")

print(x_train.head())
print(y_train.head())
print(x_test.head())

print(x_train.isnull().sum())
print(x_test.isnull().sum())

print(x_train.info())
print(x_train.nunique())

print(x_train['Gender'].unique())
print(x_test['Gender'].unique())

x_train['Gender'] = x_train['Gender'].map(lambda x: 'Male' if x in ['male', 'Male'] else 'Female')
x_test['Gender'] = x_test['Gender'].map(lambda x: 'Male' if x in ['male', 'Male'] else 'Female')
# x_train.loc[x_train.Gender==' male', 'Gender'] = 'Male'
# x_train.loc[x_train.Gender=='female', 'Gender'] ='Female'
# x_test.loc[x_test.Gender==' male', 'Gender'] = 'Male'
# x_test.loc[x_test.Gender=='female', 'Gender'] ='Female'

print(x_train['Gender'].unique())
print(x_test['Gender'].unique())

drop_col = ['CustomerId', 'Surname']
x_train_drop = x_train.drop(columns = drop_col)
x_test_drop = x_test.drop(columns = drop_col)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
x_train_dummies = pd.get_dummies(x_train_drop)
y = y_train['Exited']

print(x_train_dummies)

x_test_dummies = pd.get_dummies(x_test_drop)

print(x_test_dummies)

X_train, X_validation, Y_train, Y_validation = train_test_split(x_train_dummies, y, test_size=0.33, random_state=42)
rf = RandomForestClassifier(random_state=23, max_depth=10, n_estimators=500)
rf.fit(X_train, Y_train)

from sklearn.metrics import accuracy_score , f1_score, recall_score, roc_auc_score ,precision_score
predict_train_label = rf.predict(X_train)
predict_train_proba = rf.predict_proba(X_train)[:,1]

predict_validation_label = rf.predict(X_validation)
predict_validation_proba = rf.predict_proba(X_validation)[:,1]

print('train accuracy :', accuracy_score(Y_train, predict_train_label))
print('validation accuracy :', accuracy_score(Y_validation, predict_validation_label))
print('train f1_score :', f1_score(Y_train, predict_train_label))
print('validation f1_score :', f1_score(Y_validation, predict_validation_label))
print('train recall_score :', recall_score(Y_train, predict_train_label))
print('validation recall_score :', recall_score(Y_validation, predict_validation_label))
print('train roc_auc_score :', roc_auc_score(Y_train, predict_train_label))
print('validation roc_auc_score :', roc_auc_score(Y_validation, predict_validation_label))
print('train precision_score :', precision_score(Y_train, predict_train_label))
print('validation precision_score :', precision_score(Y_validation, predict_validation_label))

predict_test_label = rf.predict(x_test_dummies)
predict_test_proba = rf.predict_proba(x_test_dummies)[:,1]

print(x_test)

print(predict_test_label)
print(predict_test_proba)

df = pd.DataFrame({'CustomerId': x_test.CustomerId, 'Exited': predict_test_label})
print(df.head(10))

print(df.loc[df.Exited==1].value_counts('Exited'))

# pd.DataFrame({'CustomerId': x_test.CustomerId, 'Exited': predict_test_label}).to_csv('2222222.csv', index=False)