import pandas as pd
import os


def ct_measure_data_process(str_measure_data_path, str_mold):
    df_mold = pd.read_excel(str_measure_data_path, engine='openpyxl')

    each_nb = df_mold['시료수'].max()

    df_mold = df_mold.dropna(axis=1, how='all')

    series_lot_no = df_mold['LOT No']
    if str_mold == 'CT':
        del df_mold['LOT No']

    series_mold_no = df_mold['금형번호']
    del df_mold['검사자']
    del df_mold['열/개취']
    del df_mold['시료수']

    df_mold = df_mold.dropna(axis=0, how='all')

    if str_mold == 'CT':
        list_of_dfs = [df_mold.loc[i:i + each_nb - 1, :] for i in range(0, len(df_mold), each_nb)]

        df_processed = pd.DataFrame()
        for idx, df in enumerate(list_of_dfs):
            series_temp = pd.concat([df.mean(), df.min(), df.max(), df.std()])
            df_temp = pd.DataFrame(series_temp, columns=[idx])
            df_processed = pd.concat([df_processed, df_temp], axis=1)

        df_processed = df_processed.transpose()

        series_mold_no = series_mold_no.dropna().reset_index(drop=True)
        df_processed = pd.concat([series_mold_no, df_processed], axis=1)
        series_lot_no = series_lot_no.dropna().reset_index(drop=True)
        df_processed = pd.concat([series_lot_no, df_processed], axis=1)
    else:
        df_processed = df_mold

    return df_processed


def in_out_merge(str_error_data_path, str_output_path,
                 str_target_mold='CT', str_target_ng='핀함몰'):
    """
    불량률 데이터 파일과 치수 데이터 파일을 이용하여 batch 명에 따라 같은 행으로 배치하여 파일 생성.
    파일은 학습데이터 Input, Output과 분석을 위한 inout 3가지로 저장.
    str_name을 설정 할 경우 inout만 출력됨.
    inout은 분석 및 시각화를 위해 사용

    :param str_error_data_path: 불량률, 생산 공정 인자가 포함된 엑셀 파일 경로.
    :param str_output_path: 결과를 출력할 디렉터리 경로.
    :param str_target_mold: 대상 금형, 'CT' 또는 'HD'. default='CT'
    :param str_target_ng: 치수 데이터와 쌍을 이룰 불량 항목. default='핀함몰'
    :return: 결과 데이터 프레임.
    """

    df_data = pd.read_excel(str_error_data_path, engine='openpyxl')

    df_processed = ct_measure_data_process(f'D:\\Data\\GB305\\Measure\\{str_target_mold}.xlsx', str_target_mold)
    df_processed = df_processed.drop_duplicates(subset=['LOT No'])
    df_processed = df_processed.reset_index(drop=True)

    try:
        del(df_data['CT측정유무'])
    except KeyError:
        pass

    try:
        del(df_data['HD측정유무'])
    except KeyError:
        pass

    try:
        del(df_data['ERP 입력사항'])
    except KeyError:
        pass

    df_data = df_data.dropna(axis=1)
    # df_data = df_data.dropna(axis=1, how='all')
    df_data = df_data.dropna()

    list_temp = []
    for idx, batch in enumerate(df_processed['LOT No'].values):
        if batch in df_data[f'{str_target_mold}배치-L'].values:
            for value in df_data[df_data[f'{str_target_mold}배치-L'] == batch][str_target_ng].values:
                list_temp.append([batch, value])
        try:
            if batch in df_data[f'{str_target_mold}배치-R'].values:
                for value in df_data[df_data[f'{str_target_mold}배치-R'] == batch][str_target_ng].values:
                    list_temp.append([batch, value])
        except KeyError:
            pass

    df_result = pd.DataFrame(list_temp, columns=['LOT No', 'NG'])
    df_result = pd.merge(df_result, df_processed, how='inner')

    df_save = df_result

    list_mold_no = df_save['금형번호'].drop_duplicates().values

    if '금형번호' in df_save.columns:
        for str_mold in list_mold_no:
            # todo: get df according to mold no, and process beneath code.
            df_temp = df_save[df_save['금형번호'] == str_mold]
            df_temp.to_excel(os.path.join(str_output_path, f'measure/{str_target_mold}_inout_{str_target_ng}_{str_mold}.xlsx'))

            # df_save.to_excel(os.path.join(str_output_path, f'{str_target_mold}_inout_{str_target_ng}.xlsx'))
            str_output_dir = os.path.join(str_output_path, f'measure/{str_target_mold}_{str_target_ng}_{str_mold}')
            os.makedirs(str_output_dir, exist_ok=True)

            df_temp['NG'].to_excel(os.path.join(str_output_dir, 'Output.xlsx'), index=None, header=None)
            # excel_writer(str_output_path+f'{str_target_mold}_Output.xlsx', df_save['NG'])
            del df_temp['NG']
            del df_temp['LOT No']
            del df_temp['금형번호']

            df_temp.to_excel(os.path.join(str_output_dir, 'Input.xlsx'), index=None, header=None)

    else:
        df_save.to_excel(os.path.join(str_output_path, f'measure/{str_target_mold}_inout_{str_target_ng}.xlsx'))

        # df_save.to_excel(os.path.join(str_output_path, f'{str_target_mold}_inout_{str_target_ng}.xlsx'))
        str_output_dir = os.path.join(str_output_path, f'measure/{str_target_mold}_{str_target_ng}')
        os.makedirs(str_output_dir, exist_ok=True)

        df_save['NG'].to_excel(os.path.join(str_output_dir, 'Output.xlsx'), index=None, header=None)
        # excel_writer(str_output_path+f'{str_target_mold}_Output.xlsx', df_save['NG'])
        del df_save['NG']
        del df_save['LOT No']

        df_save.to_excel(os.path.join(str_output_dir, 'Input.xlsx'), index=None, header=None)

    return df_result


def excel_writer(str_path, df):
    writer = pd.ExcelWriter(str_path, engine='xlsxwriter')
    df.to_excel(writer, index=None, header=None)
    writer.save()


# if __name__ == '__main__':
#     in_out_merge('D:\\Data\\GB305\\Measure\\Data.xlsx',
#                  'D:\\Data\\GB305\\Measure\\',
#                  'HD',
#                  'HD내측플래쉬')

