import os
import numpy as np
import pandas as pd
from keras.utils import to_categorical
from sklearn.preprocessing import MinMaxScaler


class cGetData:
    def __init__(self, **kwargs):
        self.str_data_path = kwargs['data_path']
        # self.batch_size = kwargs['batch_size']

        try:
            self.cls = kwargs['mode']
        except KeyError:
            self.cls = False

        self.str_train_test = kwargs['train_test']
        self.dict_data = {'input': {}, 'output': {}}

        self.check_path()

        self.input_no = None
        self.output_no = None
        self.output_dim = 1

        self.dict_index = {}

        if self.str_train_test == 'test':
            self.dict_index = kwargs['dict_index']

        self.scaler_x = None
        self.scaler_y = None

        self.set_data()

        self.data_len = len(self.dict_data['input']['data'])
        self.input_data = self.dict_data['input']['data']
        try:
            self.output_data = self.dict_data['output']['data']
        except KeyError:
            self.output_data = None

        if self.str_train_test == 'train':
            self.scaler_x, self.scaler_y = self.get_data_scaler(self.input_data, self.output_data, self.cls)
        # self.output_no = to_categorical(self.output_data).shape[1]

        # self.shape = [self.batch_size, self.output_no]
        #
        # self.iter_len = int(self.data_len / self.batch_size) + 1 if int(self.data_len % self.batch_size) != 0 else \
        #     int(self.data_len / self.batch_size)

        self.idx = 0

    def check_path(self):
        """
        Check data path folder to confirm data format.
        :return: File extension name. Such as csv, xlsx, txt...
        """
        list_contents = os.listdir(self.str_data_path)
        # if len(list_contents) != 2:
        #     print('Check number of data file.')
        #     return False

        list_check_ext = ['csv', 'xlsx', 'txt']
        list_file_reader = [self.get_csv_file, self.get_excel_file, self.get_text_file]

        for content in list_contents:
            file_name, file_ext = os.path.splitext(content)
            if file_name.lower() == 'input':
                if file_ext.strip('.') in list_check_ext:
                    self.dict_data['input'] = {
                        'file_name': content,
                        'reader': list_file_reader[list_check_ext.index(file_ext.strip('.'))]
                    }
            elif file_name.lower() == 'output':
                if file_ext.strip('.') in list_check_ext:
                    self.dict_data['output'] = {
                        'file_name': content,
                        'reader': list_file_reader[list_check_ext.index(file_ext.strip('.'))]
                    }

    def set_data(self):
        for key in self.dict_data.keys():
            try:
                self.dict_data[key]['data'] = self.dict_data[key]['reader'](key)
            except Exception as e:
                if self.str_train_test == 'test':
                    continue
                else:
                    print('- Error in Data.py - cGetData - set_data, #1 exception.', e)

        self.input_no = len(self.dict_data['input']['data'].columns)

        if self.cls == 'cls':
            # one hot encoding
            # self.dict_data['output']['data'] = pd.DataFrame(to_categorical(self.dict_data['output']['data']))
            try:
                if self.dict_data['output'] is not None:
                    assert len(self.dict_data['output']['data'].columns) == 1, '분류 모델은 output 파일의 열이 1개를 초과 할 수 없습니다.'
                    self.output_no = to_categorical(self.dict_data['output']['data']).shape[-1]
                    self.output_dim = len(self.dict_data['output']['data'].columns)
            except Exception as e:
                if self.str_train_test == 'test':
                    pass
                else:
                    print('- Error in Data.py - cGetData - set_data, #2 exception.', e)

        #     # assert len(self.dict_data['output']['data'].columns) == self.cls, \
        #     #     f'The number of classes {self.cls} must matches ' \
        #     #     f'with max label in output data {len(self.dict_data["output"]["data"].columns)-1} + 1.'
        else:
            try:
                if self.dict_data['output'] is not None:
                    self.output_no = len(self.dict_data['output']['data'].columns)
            except Exception as e:
                if self.str_train_test == 'test':
                    pass
                else:
                    print('- Error in Data.py - cGetData - set_data, #3 exception.', e)

        # self.output_no = len(self.dict_data['output']['data'].columns)
        # self.output_no = self.cls

        self.dict_data['input']['data'] = np.array(self.dict_data['input']['data'])
        try:
            self.dict_data['output']['data'] = np.array(self.dict_data['output']['data'].values.astype(float))
        except Exception as e:
            if self.str_train_test == 'test':
                pass
            else:
                print('- Error in Data.py - cGetData - set_data, #4 exception.', e)

        df_data = pd.DataFrame(self.dict_data['input']['data'], index=None)
        df_data = df_data.dropna(axis=1, how='all')
        df_data = df_data.dropna(axis=0, how='all')

        # self.dict_index = {}
        # for column in df_data.columns:
        #     if df_data[column].dtype == object:
        #         df_data[column], self.dict_index[column] = df_data[column].factorize()
        #
        # for key, value in self.dict_index.items():
        #     self.dict_index[key] = list(value)

        if self.str_train_test == 'train':
            self.dict_index = {}
            for column in df_data.columns:
                if df_data[column].dtype == object:
                    df_data[column], self.dict_index[column] = df_data[column].factorize()

            for key, value in self.dict_index.items():
                self.dict_index[key] = list(value)
        else:
            if self.dict_index is not None:
                df_data = df_data.apply(self.get_list_index)
            # for column in df_data.columns:
            #     if df_data[column].dtype == object:
            #         df_data[column]
            #         self.dict_index[column]

        self.dict_data['input']['original'] = self.dict_data['input']['data']
        self.dict_data['input']['data'] = df_data

    def get_index(self, x, name):
        return self.dict_index[str(name)].index(str(x))

    def get_list_index(self, series):
        return series.map(lambda x: self.get_index(x, series.name))
        # print(series == dict_index[str(series.name)])

    def get_excel_file(self, data):
        df_raw = pd.read_excel(os.path.join(self.str_data_path, self.dict_data[data]['file_name']),
                               header=None,
                               engine='openpyxl',
                               )
        return df_raw

    def get_csv_file(self, data):
        df_raw = pd.read_csv(os.path.join(self.str_data_path, self.dict_data[data]['file_name']),
                             header=None,
                             )
        return df_raw

    def get_text_file(self, data):
        df_raw = pd.read_table(os.path.join(self.str_data_path, self.dict_data[data]['file_name']),
                               header=None,
                               )
        return df_raw

    @staticmethod
    def get_data_scaler(train_x, train_y, mode):
        scaler_y = None

        scaler_x = MinMaxScaler()
        scaler_x.fit(train_x)

        if mode.lower() == 'reg':
            scaler_y = MinMaxScaler()
            scaler_y.fit(train_y)
            # y = np.array(y).reshape((-1, y.shape[-1]))
            # y = np.array(y)
        # elif mode.lower() == 'cls':
        #     scaler_x = MinMaxScaler()
        #     scaler_x.fit(train_x)
            # y = to_categorical(train_y)
        # elif mode.lower() == 'nlp_cls':
        #     y = to_categorical(y)

        return scaler_x, scaler_y

    @staticmethod
    def data_scale_for_train(train_x, train_y, scaler_x, scaler_y, mode):
        # if scaler_x is None:
        #     scaler_x = MinMaxScaler()

        x = scaler_x.transform(train_x)

        # if scaler_y is None:
        #     scaler_y = None
        #     if mode.lower() == 'reg':
        #         scaler_y = MinMaxScaler()

        if train_y is not None:
            if mode.lower() == 'reg':
                y = scaler_y.transform(train_y)
                y = np.array(y).reshape((-1, y.shape[-1]))
            else:
                y = to_categorical(train_y)
        else:
            y = None

        return x, y


class cDataProcessing:
    def __init__(self):
        self.target_path = 'D:\\Projects\\ADA\\V02\\models\\'

    def post_processing(self):
        list_dir = os.listdir(self.target_path)
        new_list_dir = []
        for idx, str_dir in enumerate(list_dir):
            if os.path.isdir(os.path.join(self.target_path, str_dir)):
                new_list_dir.append(str_dir)

        list_dir = new_list_dir[-10:]

        str_tail_0 = list_dir[0].replace(f'{list_dir[0].split("_")[0]}_{list_dir[0].split("_")[1]}_', '')
        for str_dir in list_dir:
            list_str_dir = str_dir.split('_')
            str_tail = str_dir.replace(f'{list_str_dir[0]}_{list_str_dir[1]}_', '')
            if str_tail != str_tail_0:
                print('> Error.')
                print(str_tail, str_tail_0)

        measure_data_check = False
        measure_mold = ''
        list_mold = ['CT', 'HD']
        for str_mold in list_mold:
            if str_tail_0.split('_')[0] == str_mold:
                measure_mold = str_mold
                measure_data_check = True

        list_df = []
        for dir_name in list_dir:
            list_df.append(
                pd.read_excel(os.path.join(self.target_path, dir_name + '\\RF_results_train.xlsx'), engine='openpyxl',
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
                    pd.read_excel(os.path.join(self.target_path, dir_name + '\\RF_results_test.xlsx'), engine='openpyxl',
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

        df_ret = pd.concat([pd.DataFrame(list_pi).reset_index(drop=True), df_ret], axis=1)

        df_ret = pd.concat([df_ret, pd.DataFrame(df_ret.mean()).transpose()]).reset_index(drop=True)
        df_ret = pd.concat([df_ret, pd.DataFrame(df_ret.min()).transpose()]).reset_index(drop=True)
        df_ret = pd.concat([df_ret, pd.DataFrame(df_ret.max()).transpose()]).reset_index(drop=True)

        df_ret = df_ret.transpose()
        columns = list(df_ret.columns)
        columns[-3:] = ['Avg', 'Min', 'Max']
        df_ret.columns = columns

        if measure_data_check:
            df_measure = pd.read_excel(os.path.join(f'D:\\Data\\GB305\\Measure\\{measure_mold}.xlsx'),
                                       engine='openpyxl')
            columns = df_measure.columns[5:]

            if measure_mold == 'CT':
                list_stat = ['avg', 'min', 'max', 'std']
                list_columns = []
                for str_stat in list_stat:
                    for str_column in columns:
                        list_columns.append(str(str_column) + '_' + str_stat)

                columns = list_columns

            df_ret = df_ret.transpose()
            columns = list(columns) + list(df_ret.columns)[-2:]
            df_ret.columns = columns
            df_ret = df_ret.transpose()
            df_ret = df_ret.reset_index()

            df_rank = pd.DataFrame()
            for column in list(df_ret.columns)[1:11]:
                list_rank = []
                for idx in list(df_ret[column].sort_values(ascending=False).index):
                    str_pos = df_ret[list(df_ret.columns)[0]].loc[idx]
                    if str_pos not in ['R2', 'RMSE']:
                        list_rank.append(str_pos)

                    if len(list_rank) == 10:
                        break

                df_rank = pd.concat([df_rank, pd.DataFrame(list_rank, columns=['rank'])], axis=0).reset_index(drop=True)
            df_pos = df_rank.drop_duplicates().reset_index(drop=True)

            dict_rank = {}
            for i in df_pos.index:
                dict_rank[i] = df_rank[df_rank == df_pos.loc[i]].count().values[0]

            dict_rank = dict(sorted(dict_rank.items(), reverse=True, key=lambda item: item[1]))

            list_rank = []
            list_count = []
            for key in dict_rank.keys():
                list_rank.append(df_pos.loc[key].values[0])
                list_count.append(dict_rank[key])

            df_rank = pd.concat(
                [pd.DataFrame(list_rank, columns=['Rank']), pd.DataFrame(list_count, columns=['Count'])], axis=1)

            df_ret = pd.concat([df_ret, df_rank], axis=1)

            df_ret.to_excel(f'D:\\Projects\\ADA\\V02\\models\\{list_dir[-1]}_result.xlsx')
        else:
            list_env = ['I/M형태', 'I/M설비', '작업자', 'CT업체', 'CT금형', 'HD금형']

            list_env_count = [2, 6, 13, 3, 4, 2]
            list_env_weight = []
            for env_count in list_env_count:
                list_env_weight.append(env_count / sum(list_env_count))

            df_ret = pd.concat([df_ret, pd.DataFrame(list_env_weight, columns=['Weight'])], axis=1)

            df_ret = df_ret.transpose()
            columns = list(df_ret.columns)

            columns[:6] = list_env
            df_ret.columns = columns

            def set_color_cell(s):
                # color = 'white' if val < thresh else 'black'
                # return f'color: {color}'
                is_over = s > s['Weight']
                return ['color: white' if v else '' for v in is_over]

            df_ret.style.apply(set_color_cell).to_excel(f'D:\\Projects\\ADA\\V02\\models\\{list_dir[-1]}_result.xlsx')


if __name__ == '__main__':
    cdp = cDataProcessing()
    cdp.post_processing()
