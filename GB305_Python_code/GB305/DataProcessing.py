import ExcelMerge
import os
import pandas as pd
import calendar


def measure_data_preprocessing(str_file_path):
    str_default_dir = 'D:\\Data\\GB305'

    list_ng = ['X_미사출', 'C_핀함몰', 'H_HD내측플래쉬']
    list_mold = ['CT', 'HD']

    for str_mold in list_mold:
        for str_ng in list_ng:
            ExcelMerge.in_out_merge(os.path.join(str_default_dir, str_file_path),
                                    str_default_dir,
                                    str_mold,
                                    str_ng)


def env_data_preprocessing(str_file_name):

    str_default_dir = 'D:\\Data\\GB305'

    list_env = ['I/M설비구분', 'I/M설비', '작업자', 'CT업체명', 'CT금형번호', 'HD금형번호']
    list_ng = ['X_미사출', 'C_핀함몰', 'H_HD내측플래쉬']

    str_start_ng = 'X_외측 핀사이 금속이물'
    str_end_ng = 'H_HD상면플래쉬'

    df_raw = pd.read_excel(f'{str_default_dir}\\{str_file_name}', engine='openpyxl')

    start_year = df_raw['검사일자'].min().year
    start_month = df_raw['검사일자'].min().month

    end_year = df_raw['검사일자'].max().year
    end_month = df_raw['검사일자'].max().month

    list_df = []
    list_str_date = []
    month = start_month
    for year in range(start_year, end_year + 1):
        while True:
            print(year, month)
            last_day = calendar.monthrange(year, month)[1]

            str_start_date = f'{year}-{month:02d}-01'
            str_end_date = f'{year}-{month:02d}-{last_day}'

            list_df.append(df_raw[(df_raw['검사일자'] >= str_start_date) & (df_raw['검사일자'] <= str_end_date)])
            list_str_date.append(f'{year}{month:02d}')

            if year == end_year and month == end_month:
                break

            month += 1
            if month > 12:
                month = 1
                break

    list_df.append(df_raw)
    list_str_date.append('total')

    for _df, str_date in zip(list_df, list_str_date):
        df_x = _df[list_env]

        n_start_ng = list(_df.columns).index(str_start_ng)
        n_end_ng = list(_df.columns).index(str_end_ng)
        idx_ng_rate = range(n_start_ng, n_end_ng + 1)

        df_y = _df[_df.columns[idx_ng_rate]]

        for str_ng in list_ng:
            str_folder_path = f'{str_default_dir}/{str_ng}_{str_date}'
            os.makedirs(str_folder_path, exist_ok=True)

            df_y[str_ng].to_excel(f'{str_folder_path}/Output.xlsx', header=None, index=False)
            df_x.to_excel(f'{str_folder_path}/Input.xlsx', header=None, index=False)


def post_train_processing():
    target_path = 'D:\\Projects\\ADA\\V02\\models\\target\\'
    list_dir = os.listdir(target_path)

    list_df = []
    for dir_name in list_dir:
        list_df.append(pd.read_excel(os.path.join(target_path, dir_name + '\\RF_results_train.xlsx'), engine='openpyxl',
                                     index_col=0))

    list_rsq = []
    list_pi = []
    list_rmse = []

    for df in list_df:
        series_0 = df[0].dropna()
        list_rsq.append(series_0.iloc[-1])

        series_pi = df['PImportance'].dropna()
        list_pi.append(series_pi)

        series_rmse = df['RMSE'].dropna()
        list_rmse.append(series_rmse.iloc[-1])

    df_ret = pd.DataFrame(list_rsq, columns=['R2'])
    df_ret = pd.concat([df_ret, pd.DataFrame(list_rmse, columns=['RMSE'])], axis=1)

    try:
        list_df = []
        for dir_name in list_dir:
            list_df.append(
                pd.read_excel(os.path.join(target_path, dir_name + '\\RF_results_test.xlsx'), engine='openpyxl',
                              index_col=0))

        list_rsq = []
        list_rmse = []

        for df in list_df:
            series_0 = df[0].dropna()
            list_rsq.append(series_0.iloc[-1])

            series_rmse = df['RMSE'].dropna()
            list_rmse.append(series_rmse.iloc[-1])

        df_ret = pd.concat([df_ret, pd.DataFrame(list_rsq, columns=['Test_R2'])], axis=1)
        df_ret = pd.concat([df_ret, pd.DataFrame(list_rmse, columns=['Test_RMSE'])], axis=1)
    except:
        pass

    df_ret = pd.concat([df_ret, pd.DataFrame(list_pi).reset_index(drop=True)], axis=1)

    df_ret = pd.concat([df_ret, pd.DataFrame(df_ret.mean()).transpose()]).reset_index(drop=True)
    df_ret = pd.concat([df_ret, pd.DataFrame(df_ret.min()).transpose()]).reset_index(drop=True)
    df_ret = pd.concat([df_ret, pd.DataFrame(df_ret.max()).transpose()]).reset_index(drop=True)

    df_ret.to_excel('D:\\Projects\\ADA\\V02\\models\\target\\result.xlsx')


if __name__ == '__main__':
    # env_data_preprocessing('RawData_20220316.xlsx')
    measure_data_preprocessing('RawData_20220316.xlsx')
