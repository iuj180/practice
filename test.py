import pandas as pd
df = pd.read_csv("C:/Users/user/Desktop/GB305 조립기 검사실적 데이터/GB305-R_LOG_DATA/220823/log1/2208230658.csv", encoding='cp949', skiprows=1)
type(df)
df.head()
df.columns[5]
df.describe()
df.loc[df['캐비티 결과']>0].describe()