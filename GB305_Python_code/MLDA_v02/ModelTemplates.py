from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import time
import math
import os
from sklearn.metrics import r2_score
from eli5.sklearn import PermutationImportance
import eli5

from Data import cGetData


class cModelTemplates:
    def __init__(self, **kwargs):
        self.input_dim = kwargs['input_dim']
        self.output_shape = kwargs['output_shape']
        self.model_type = ''
        self.mode = kwargs['mode']
        self.model = None
        self.search_model = None
        self.str_result_folder_path = kwargs['result_path']

    @staticmethod
    def get_time():
        tm_now = time.localtime()

        str_tm = f'{tm_now.tm_year:04d}{tm_now.tm_mon:02d}{tm_now.tm_mday:02d}_' \
                 f'{tm_now.tm_hour:02d}{tm_now.tm_min:02d}{tm_now.tm_sec:02d}'
        return str_tm

    def build_model(self, dict_params):
        print('override')

    def load_model(self, str_path):
        print('override')

    def search(self, list_dict_params, train_x, train_y, scaler_x, scaler_y, cv):
        print('override')

    def train(self, train_x, train_y, scaler_x=None, scaler_y=None, dict_params=None):
        print('override')

    def test(self, test_x, gt_y, scaler_x, scaler_y, name='', original_x=None):
        x, y = cGetData.data_scale_for_train(test_x, gt_y, scaler_x, scaler_y, self.mode)
        pred = self.model.predict(x)
        if scaler_y is not None:
            if len(pred.shape) < 2:
                pred = pred.reshape((pred.shape[0], 1))
            y_hat = scaler_y.inverse_transform(pred)
        else:
            y_hat = np.argmax(pred, axis=1)

        y_hat = np.array(y_hat)

        if gt_y is not None:
            def _scorer(model, _x, _y):
                return model.score(_x, _y)

            perm = PermutationImportance(self.model, scoring=_scorer).fit(x, y)
            p_importance = perm.feature_importances_
            df_pimportance = pd.DataFrame(p_importance, columns=['value'])
            df_pimportance['PImportance'] = df_pimportance['value'] / df_pimportance['value'].sum()

            y_hat = y_hat.reshape(gt_y.shape)
            mse = mean_squared_error(gt_y, y_hat)
            rmse = math.sqrt(mse)

            y_both = np.concatenate([gt_y, y_hat], axis=1)
            print('[True, Predict]\n', y_both)
            print('RMSE : ', rmse)

            df_result = pd.DataFrame(y_both)  #, columns=['True', 'Predict'])
            nb_columns = len(df_result.columns)
            r2 = []
            for idx in range(nb_columns//2):
                r2.append(np.corrcoef(df_result[idx], df_result[idx + nb_columns//2])[0, 1] ** 2)
            r2 = np.array(r2).reshape((1, -1))

            df_result = pd.concat([df_result, pd.DataFrame(r2)], axis=0)
            df_result = df_result.reset_index(drop=True)
            # df_result['Difference'] = abs(df_result['True'] - df_result['Predict'])
            # df_result['RelativeError'] = abs(df_result['True'] - df_result['Predict']) / df_result['True']
            try:
                df_importances = pd.DataFrame(self.model.feature_importances_, columns=['Importance'])
                df_result = pd.concat([df_result, df_importances], axis=1)
                df_result = pd.concat([df_result, df_pimportance['PImportance']], axis=1)

            except AttributeError:
                pass

            df_result = pd.concat([df_result, pd.DataFrame([rmse], columns=['RMSE'])], axis=1)
        else:
            df_result = pd.DataFrame(y_hat)
            if original_x is not None:
                original_x = pd.DataFrame(original_x)
                df_result = pd.concat([original_x, df_result], axis=1)

        if not os.path.exists(self.str_result_folder_path):
            os.makedirs(self.str_result_folder_path)

        df_result.to_excel(os.path.join(self.str_result_folder_path, f'{self.model_type}_results{name}.xlsx'))
        # print('pause')
