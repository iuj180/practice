import pandas as pd

df = pd.read_csv("C:/Users/user/Desktop/GB305 조립기 검사실적 데이터/GB305-R_LOG_DATA/220823/log1/2208230658.csv", encoding='cp949', skiprows=1)
new_labels=['DATA No', 'DATE', 'TIME', 'OLD_BATCH_NO1', 'OLD_BATCH_NO2',
       '카메라 종합 결과', '인서트 NG 확인', '감합부 결과', '접촉부 갭_01', '접촉부 갭_02',
       '접촉부 갭_03', '접촉부 갭_04', '접촉부 갭_05', '접촉부 갭_06', '접촉부 갭_07', '접촉부 갭_08',
       '접촉부 갭_09', '접촉부 갭_10', '접촉부 갭_11', '접촉부 갭_12', '접촉부 갭_13', '접촉부 갭_14',
       '접촉부 갭_15', '접촉부 갭_16', '접촉부 갭_17', '접촉부 갭_18', '접촉부 갭_19', '접촉부 갭_20',
       '접촉부 갭_21', '접촉부 갭_22', '접촉부 갭_23', '접촉부 갭_24', '접촉부 갭_25', '접촉부 갭_26',
       '접촉부 갭_27', '접촉부 갭_28', '접촉부 갭_29', '접촉부 갭_30', '접촉부 갭_31', '접촉부 갭_32',
       '접촉부 갭_33', '접촉부 갭_34', '접촉부 갭_35', '접촉부 갭_36', '접촉부 갭_37', '접촉부 갭_38',
       '접촉부 갭_39', '접촉부 갭_40', '접촉부 갭_41', '접촉부 갭_42', '접촉부 갭_43', '접촉부 갭_44',
       '접촉부 갭_45', '접촉부 갭_46', '접촉부 갭_47', '접촉부 갭_48', '접촉부 갭_49', '접촉부 갭_50',
       '접촉부 갭_51', '접촉부 갭_52', '접촉부 갭_53', '접촉부 갭_54', '접촉부 갭_55', '접촉부 갭_56',
       '접촉부 갭_57', '접촉부 갭_58', '접촉부 갭_59', '접촉부 갭_60', '접촉부 갭_61', '접촉부 갭_62',
       '접촉부 갭_63', '접촉부 갭_64', '접촉부 갭_65', '접촉부 갭_66', '접촉부 갭_67', '접촉부 갭_68',
       '접촉부 갭_69', '접촉부 갭_70', '접촉부 갭_71', '접촉부 갭_72', '접촉부 갭_73', '접촉부 갭_74',
       '접촉부 갭_75', '접촉부 갭_76', '접촉부 갭_77', '접촉부 갭_78', '내외측 감합부_01',
       '내외측 감합부_02', '내외측 감합부_03', '내외측 감합부_04', '내외측 감합부_05', '내외측 감합부_06',
       '내외측 감합부_07', '내외측 감합부_08', '내외측 감합부_09', '내외측 감합부_10', '내외측 감합부_11',
       '내외측 감합부_12', '내외측 감합부_13', '내외측 감합부_14', '내외측 감합부_15', '내외측 감합부_16', '내외측 감합부_17', '내외측 감합부_18',
       '내외측 감합부_19', '내외측 감합부_20', '내외측 감합부_21', '내외측 감합부_22', '내외측 감합부_23',
       '내외측 감합부_24', '내외측 감합부_25', '내외측 감합부_26', '내외측 감합부_27', '내외측 감합부_28',
       '내외측 감합부_29', '내외측 감합부_30', '내외측 감합부_31', '내외측 감합부_32', '내외측 감합부_33',
       '내외측 감합부_34', '내외측 감합부_35', '내외측 감합부_36', '내외측 감합부_37', '내외측 감합부_38',
       '내외측 감합부_39', '내외측 감합부_40', '내외측 감합부_41', '내외측 감합부_42', '내외측 감합부_43',
       '내외측 감합부_44', '내외측 감합부_45', '내외측 감합부_46', '내외측 감합부_47', '내외측 감합부_48',
       '내외측 감합부_49', '내외측 감합부_50', '내외측 감합부_51', '내외측 감합부_52', '내외측 감합부_53',
       '내외측 감합부_54', '내외측 감합부_55', '내외측 감합부_56', '내외측 감합부_57', '내외측 감합부_58',
       '내외측 감합부_59', '내외측 감합부_60', '내외측 감합부_61', '내외측 감합부_62', '내외측 감합부_63',
       '내외측 감합부_64', '내외측 감합부_65', '내외측 감합부_66', '내외측 감합부_67', '내외측 감합부_68',
       '내외측 감합부_69', '내외측 감합부_70', '내외측 감합부_71', '내외측 감합부_72', '내외측 감합부_73',
       '내외측 감합부_74', '내외측 감합부_75', '내외측 감합부_76', '내외측 감합부_77', '내외측 감합부_78',
       '홀드다운 갭_01', '홀드다운 갭_02', 'DM60324', 'DM60326', 'DM60328', 'DM60330',
       'DM60332', 'DM60334', 'DM60336', 'DM60338', 'DM60340', 'DM60342',
       'DM60344', 'DM60346', 'DM60348', 'DM60350', 'DM60352', 'DM60354',
       'DM60356', 'DM60358', 'DM60360', 'DM60362', 'DM60364']

df1=df.set_axis(labels=new_labels,axis=1)
df1.drop(df1.iloc[:,166:173], axis=1, inplace=True)       
df1.drop(df1.iloc[:,167:171], axis=1, inplace=True)
df1.drop(df1.iloc[:,168:176], axis=1, inplace=True)
print(df1.rename(mapper={'DM60338':'캐비티명1', 'DM60348':"캐비티명2"}, axis=1).head(5))