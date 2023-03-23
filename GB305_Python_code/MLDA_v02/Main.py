import Models
import Data
# import threading
import os
import GridSearch
from termcolor import colored
import time
# import sys
import joblib
import tensorflow as tf
import colorama
import warnings
from tensorflow.python.client import device_lib
from sklearn.model_selection import train_test_split
from pickle import dump, load

warnings.filterwarnings(action='ignore')
warnings.simplefilter(action='ignore', category=FutureWarning)  # FutureWarning 제거
colorama.init()

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']


try:
    list_gpus = get_available_gpus()
except Exception as e:
    print(e)
    list_gpus = []

if len(list_gpus) > 0:
    print(f"- GPU는 총 {colored(len(list_gpus), 'yellow')}개 입니다.")
    str_gpu_selection = f"'0': {colored('전체 GPU', 'yellow')}, "
    for idx, gpu_name in enumerate(list_gpus):
        str_gpu_selection += f"'{idx+1}': {colored(gpu_name, 'yellow')}, "
    str_gpu_selection += f"이 중에서 사용할 GPU를 선택하세요."
    print(f"- {str_gpu_selection}")
    # Todo : selection set to 2 for debug
    # selection = input(':>')
    selection = 2
    if selection != 0:
        os.environ["CUDA_VISIBLE_DEVICES"] = f'{int(selection)-1}'
    _config = tf.compat.v1.ConfigProto()
    # _config.gpu_options.per_process_gpu_memory_fraction = 0.5
    _config.gpu_options.allow_growth = True

    tf.compat.v1.InteractiveSession(config=_config)


class cMain:
    def __init__(self):
        self.temp = ''
        self.str_mode = ''
        self.str_data_path = ''
        self.str_grid_data_path = 'D:\\Data\\GB305\\In_test_grid'

        self.str_model_path = ''

        self.test_ratio = 0.0
        self.train_x = None
        self.train_y = None
        self.test_x = None
        self.test_y = None
        self.str_time = None
        self.c_data = None
        self.f_train = False
        self.str_model_number = ''
        self.str_result_folder_path = ''
        self.str_result_file_path = ''
        self.str_model_type = 'all'
        self.str_train_test = 'train'
        self.ROOT_DIR = os.path.abspath(os.curdir)
        self.str_model_dir = f'{self.ROOT_DIR}/models/'

    def main(self):
        if not self.set_up():
            print("- 잘못된 입력으로 인하여 종료합니다.")
            return 0

        # if self.str_train_test == 'train':
        #     list_ratio = [0.05, 0.10, 0.15, 0.20, 0.25, 0.3]
        #     for f_ratio in list_ratio:
        #         self.test_ratio = f_ratio
        #         self.optimize()

        if self.test_ratio == 0.0:
            n_iter = 10
        else:
            n_iter = 1

        if self.str_train_test == 'train':
            for i in range(n_iter):
                self.optimize()

                # if self.test_ratio == 0.0:
                #     self.str_train_test = 'test'
                #     self.test(self.str_grid_data_path, self.str_result_folder_path)
                #
                # self.str_train_test = 'train'

            if n_iter == 10:
                # post processing
                cdp = Data.cDataProcessing()
                cdp.post_processing()

            # try:
            #     self.optimize()
            # except Exception as e:
            #     print('- Data.py - main - optimize error', e)
        else:
            self.test(self.str_data_path)
            # try:
            #     self.test()
            # except Exception as e:
            #     print('- Data.py - main - test error', e)

        print('- 작업이 완료 되었습니다.')
        print('- 엔터키를 누르시면 종료합니다.')
        # input(':>')

    def get_model_file_path(self):
        list_files = os.listdir(self.str_model_path)
        dict_config = None
        dict_index = None
        scaler_x = None
        scaler_y = None

        for file_name in list_files:
            if file_name == 'config.txt':
                dict_config = self.get_config(os.path.join(self.str_model_path, file_name))
            if file_name == 'index.txt':
                dict_index = self.get_index(os.path.join(self.str_model_path, file_name))

            if file_name == 'scaler_x.pkl':
                scaler_x = load(open(os.path.join(self.str_model_path, file_name), 'rb'))
            if file_name == 'scaler_y.pkl':
                scaler_y = load(open(os.path.join(self.str_model_path, file_name), 'rb'))

        if dict_config is None:
            print('config.txt file does not exists.')
            return False

        if dict_index is None:
            print('index.txt data does not exists.')

        for file_name in list_files:
            str_file_path = os.path.join(self.str_model_path, file_name)
            if os.path.isfile(str_file_path):
                if os.path.splitext(file_name)[-1] == '.joblib':
                    return os.path.join(self.str_model_path, file_name), dict_config, dict_index, scaler_x, scaler_y
                elif os.path.splitext(file_name)[-1] == '.hdf5':
                    return os.path.join(self.str_model_path, file_name), dict_config, dict_index, scaler_x, scaler_y

    @staticmethod
    def get_config(str_path):
        dict_ret = {}
        with open(str_path, 'r') as config:
            lines = config.readlines()
            for line in lines:
                key = line.split('=\t')[0]
                value = line.split('=\t')[-1].replace('\n', '')
                dict_ret[key] = value

        return dict_ret

    @staticmethod
    def get_index(str_path):

        dict_ret = {}
        with open(str_path, 'r') as config:
            lines = config.readlines()
            for line in lines:
                key = line.split('=\t')[0]
                value = line.split('=\t')[-1].replace('\n', '')
                value = value.replace('[', '').replace(']', '').replace(' ', '').replace('\'', '')
                dict_ret[key] = value.split(',')
        if len(dict_ret.keys()) != 0:
            return dict_ret
        else:
            return None

    def test(self, str_data_path, str_result_path=None):
        if str_result_path is None:
            self.set_model_path()

        str_path, dict_config, dict_index, scaler_x, scaler_y = self.get_model_file_path()
        if str_result_path is None:
            str_result_path = os.path.dirname(str_path)
        self.c_data = Data.cGetData(data_path=str_data_path, mode=dict_config['mode'],
                                    train_test=self.str_train_test, dict_index=dict_index)
        self.c_data.scaler_x = scaler_x
        self.c_data.scaler_y = scaler_y

        if dict_config['model_type'] == 'rf':
            c_model = Models.cRFModel(input_dim=dict_config['input_dim'], output_shape=dict_config['output_no'],
                                      mode=dict_config['mode'], result_path=str_result_path)
            c_model.load_model(str_path)
            c_model.test(self.c_data.input_data, self.c_data.output_data,
                         self.c_data.scaler_x, self.c_data.scaler_y,
                         name=f'_{c_model.get_time()}',
                         original_x=self.c_data.dict_data['input']['original'])

        elif dict_config['model_type'] == 'nn':
            #todo:
            print('not yet')

    def split_data(self, test_ratio=0.3):
        if test_ratio == 0.0:
            self.train_x = self.c_data.input_data
            self.train_y = self.c_data.output_data
            self.test_x = self.train_x
            self.test_y = self.train_y
        else:
            if self.str_mode == 'cls':
                self.train_x, self.test_x, self.train_y, self.test_y = \
                    train_test_split(self.c_data.input_data,
                                     self.c_data.output_data,
                                     stratify=self.c_data.output_data,
                                     test_size=test_ratio,
                                     shuffle=True)
            else:
                self.train_x, self.test_x, self.train_y, self.test_y = \
                    train_test_split(self.c_data.input_data,
                                     self.c_data.output_data,
                                     test_size=test_ratio,
                                     shuffle=True)

    def parameter_search(self, model_type):
        c_model, dict_params = self.get_model(model_type=model_type)
        list_dict_params = GridSearch.cGridSearch.get_grid(dict_params)
        min_loss = c_model.search(list_dict_params,
                                  self.train_x, self.train_y,
                                  self.c_data.scaler_x, self.c_data.scaler_y,
                                  cv=3)
        # min_loss, scaler_x, scaler_y = c_model.search(list_dict_params, self.c_data.input_data,
        #                                               self.c_data.output_data, cv=3)

        return min_loss, c_model

    def get_optimized(self, min_loss, c_model, model_type):
        dict_optimized = min_loss
        dict_optimized['model_type'] = model_type
        if model_type == 'nn':
            c_model.train(self.train_x, self.train_y, self.c_data.scaler_x, self.c_data.scaler_y)
            c_model.test(self.train_x, self.train_y, self.c_data.scaler_x, self.c_data.scaler_y, name='_train')
            if self.test_ratio != 0.0:
                c_model.test(self.test_x, self.test_y, self.c_data.scaler_x, self.c_data.scaler_y, name='_test')
            c_model.save_weights(f'{self.str_result_folder_path}/weights.hdf5')
        elif model_type == 'rf':
            joblib.dump(c_model.model, f'{self.str_result_folder_path}/rf_model.joblib')
            print(f"- Feature importance: {c_model.model.feature_importances_}")

        return dict_optimized

    def optimize(self):
        self.set_model_path()
        self.c_data = Data.cGetData(data_path=self.str_data_path, mode=self.str_mode, train_test=self.str_train_test)

        self.split_data(self.test_ratio)

        if self.str_mode.lower() == 'nlp_cls':
            # todo:
            dict_optimized = {}
            print('a')
        else:
            if self.str_model_type == 'all':
                min_nn_loss, c_nn_model = self.parameter_search('nn')
                min_rf_loss, c_rf_model = self.parameter_search('rf')
                print(f"- nn min loss : {min_nn_loss}")
                print(f"- rf min loss : {min_rf_loss}")
                if self.test_ratio != 0.0:
                    c_nn_model.test(self.test_x, self.test_y, self.c_data.scaler_x, self.c_data.scaler_y, name='_test')
                    c_rf_model.test(self.test_x, self.test_y, self.c_data.scaler_x, self.c_data.scaler_y, name='_test')

                if min_nn_loss['loss'] < min_rf_loss['loss']:
                    dict_optimized = self.get_optimized(min_nn_loss, c_nn_model, 'nn')
                else:
                    dict_optimized = self.get_optimized(min_rf_loss, c_rf_model, 'rf')
            else:
                min_loss, c_model = self.parameter_search(self.str_model_type)
                print(f"- {self.str_model_type} min loss : {min_loss}")
                c_model.test(self.train_x, self.train_y, self.c_data.scaler_x, self.c_data.scaler_y, name='_train')
                if self.test_ratio != 0.0:
                    c_model.test(self.test_x, self.test_y, self.c_data.scaler_x, self.c_data.scaler_y, name='_test')
                dict_optimized = self.get_optimized(min_loss, c_model, self.str_model_type)

        dict_optimized['data_path'] = self.str_data_path
        print(dict_optimized)

        dict_optimized['input_dim'] = self.c_data.input_no
        dict_optimized['output_no'] = self.c_data.output_no
        dict_optimized['mode'] = self.str_mode
        dict_optimized['test_ratio'] = self.test_ratio

        self.save_dict(dict_optimized)
        self.save_dict(self.c_data.dict_index, 'index.txt')

        self.save_scaler()
        # c_model = self.train_model(min_loss, self.c_data.input_data, self.c_data.output_data, scaler_x, scaler_y)
        # print(min_loss)

    def save_scaler(self):
        dump(self.c_data.scaler_x, open(f'{self.str_result_folder_path}/scaler_x.pkl', 'wb'))
        dump(self.c_data.scaler_y, open(f'{self.str_result_folder_path}/scaler_y.pkl', 'wb'))

    def save_dict(self, dict_optimized, file_name='config.txt'):
        try:
            with open(f'{self.str_result_folder_path}/{file_name}', 'w') as f:
                for key in dict_optimized.keys():
                    f.write(f'{key}=\t{dict_optimized[key]}\n')
        except Exception as e:
            print('- save dict error', e)

    # def train_model(self, dict_optimized, train_x, train_y, scaler_x, scaler_y):
    #     # self.set_model_path(dict_optimized)
    #     c_model, _ = self.get_model(model_type=dict_optimized['model_type'])
    #     # c_model.str_result_file_path = self.str_result_file_path
    #     # c_model.str_result_folder_path = self.str_result_folder_path
    #     c_model.train(dict_optimized['params'], train_x, train_y, scaler_x, scaler_y)
    #     return c_model

    @staticmethod
    def get_time():
        tm_now = time.localtime()
        _str_time = f'{tm_now.tm_year:04d}{tm_now.tm_mon:02d}{tm_now.tm_mday:02d}' \
                    f'{tm_now.tm_hour:02d}{tm_now.tm_min:02d}{tm_now.tm_sec:02d}'

        return _str_time

    def get_model_type(self):
        while True:
            print(f"- 모델은 '{colored('인공신경망/랜덤포레스트', 'yellow')}' 2가지로 생성 할 수 있습니다.")
            # print(f"- 모델은 '{colored('회귀/분류/자연어 분류', 'yellow')}' 3가지로 생성 할 수 있습니다.")
            list_selection = ['인공신경망', '랜덤포레스트', '인공신경망과 랜덤포레스트']
            # list_selection = ['회귀', '분류', '자연어 분류']
            ret = self.get_selection_from_input(list_selection)
            str_selection = list_selection[ret]
            print(f"- '{colored(str_selection, 'yellow')}' 모델을 생성 하시겠습니까?")
            if self.get_yn_from_input():
                print(f"- '{colored(str_selection, 'yellow')}' 모델을 생성 하겠습니다.")
                if ret == 0:
                    return 'nn'
                elif ret == 1:
                    return 'rf'
                elif ret == 2:
                    return 'all'
                else:
                    return False

    def get_train_test(self):
        while True:
            print(f"- '{colored('학습/검사', 'yellow')}' 중 어떤 작업을 하시겠습니까?")
            # print(f"- 모델은 '{colored('회귀/분류/자연어 분류', 'yellow')}' 3가지로 생성 할 수 있습니다.")
            list_selection = ['학습', '검사']
            # list_selection = ['회귀', '분류', '자연어 분류']
            ret = self.get_selection_from_input(list_selection)
            str_selection = list_selection[ret]
            print(f"- '{colored(str_selection, 'yellow')}'을(를) 수행 하시겠습니까?")
            if self.get_yn_from_input():
                print(f"- '{colored(str_selection, 'yellow')}'을(를) 수행 하겠습니다.")
                if ret == 0:
                    return 'train'
                elif ret == 1:
                    return 'test'
                else:
                    return False

    def get_setup(self):
        while True:
            print(f"- '{colored('설정 파일', 'yellow')}'이 있으면 '{colored('학습 1, 검사 2', 'yellow')}'. "
                  f"없으면 '{colored('N', 'yellow')}'을 입력하세요.")
            # str_path = self.get_string_from_input(f_yn=False)
            # str_path = str_path.strip(' ')
            str_input = self.get_string_from_input(f_yn=False)
            if str_input == '1':
                str_path = f'{self.ROOT_DIR}\\train_setup.txt'
            elif str_input == '2':
                str_path = f'{self.ROOT_DIR}\\test_setup.txt'
            elif str_input.lower() == 'n':
                print('- 설정 파일이 없습니다. 설정을 시작합니다.')
                return False

            if os.path.exists(str_path):
                dict_ret = self.get_config(str_path)
                self.str_train_test = dict_ret['str_train_test']
                self.str_data_path = dict_ret['str_data_path']
                if self.str_train_test == 'train':
                    self.str_model_type = dict_ret['str_model_type']
                    self.str_mode = dict_ret['str_mode']
                    self.set_model_path()
                else:
                    while True:
                        self.str_model_path = self.get_model_path(f_yn=False)
                        if os.path.exists(self.str_model_path):
                            break
                        else:
                            print('- 모델 폴더 경로에 이상이 있습니다. 다시 입력하세요.')
                return True
            else:
                print('- 설정 파일 경로에 이상이 있습니다. 다시 입력하세요.')

    def set_up(self):
        if self.get_setup():
            return True

        self.str_train_test = self.get_train_test()

        if self.str_train_test == 'train':
            self.str_model_type = self.get_model_type()

            while True:
                self.str_mode = self.get_mode()
                if not self.str_mode:
                    return False
                self.str_data_path = self.get_data_folder_path()

                if self.check_selection():
                    self.set_model_path()
                    return True
        else:
            while True:
                self.str_model_path = self.get_model_path()
                self.str_data_path = self.get_data_folder_path()
                return True

    def get_model_path(self, f_yn=True):
        while True:
            print("- 모델 폴더 경로를 입력하세요.")
            str_path = self.get_string_from_input(f_yn)
            str_path = str_path.strip(' ')
            if os.path.exists(str_path):
                return str_path
            else:
                print('- 모델 폴더 경로에 이상이 있습니다.')

    def check_selection(self):
        if self.str_mode == 'cls':
            str_model = '분류'
        elif self.str_mode == 'reg':
            str_model = '예측(회귀)'
        else:
            str_model = '자연어 분류'

        if self.str_model_type == 'nn':
            str_model_type = '인공신경망'
        elif self.str_model_type == 'rf':
            str_model_type = '랜덤포레스트'
        else:
            str_model_type = '인공신경망과 랜덤포레스트'

        print(f"- 선택하신 모델은 '{colored(str_model_type, 'yellow')}' 기반의 '{colored(str_model, 'yellow')}' 분석이며,")
        print(f"- 데이터 폴더 경로는 '{colored(self.str_data_path, 'yellow')}'이/가 맞습니까?")

        if self.get_yn_from_input():
            return True
        else:
            return False

    def _get_model(self, model_type):
        if model_type == 'nn':
            dict_params = {'units': [16],
                           'nb_layers': [1],
                           'optimizer': ['sgd'],
                           }
            if self.str_mode == 'reg':
                dict_params['last_activation'] = ['sigmoid']
                dict_params['loss'] = ['mse']
            else:
                dict_params['last_activation'] = ['softmax']
                dict_params['loss'] = ['categorical_crossentropy']

            return Models.cNNModel(input_dim=self.c_data.input_no, output_shape=self.c_data.output_no, mode=self.str_mode,
                                   result_path=self.str_result_folder_path), dict_params
        elif model_type == 'rf':
            dict_params = {'n_estimators': [1],
                           'max_features': [0.1]}
            if self.str_mode == 'reg':
                dict_params['criterion'] = ['mse']
            elif self.str_mode == 'cls':
                dict_params['criterion'] = ['gini']
            return Models.cRFModel(input_dim=self.c_data.input_no, output_shape=self.c_data.output_no, mode=self.str_mode,
                                   result_path=self.str_result_folder_path), dict_params

    def get_model(self, model_type):
        if model_type == 'nn':
            dict_params = {'units': [64, 128, 256],
                           'nb_layers': [1, 2, 3],
                           'optimizer': ['sgd', 'adam', 'rmsprop'],
                           }
            if self.str_mode == 'reg':
                dict_params['last_activation'] = ['sigmoid', 'tanh']
                dict_params['loss'] = ['mse', 'mae']
            else:
                dict_params['last_activation'] = ['softmax']
                dict_params['loss'] = ['categorical_crossentropy']

            return Models.cNNModel(input_dim=self.c_data.input_no, output_shape=self.c_data.output_no, mode=self.str_mode,
                                   result_path=self.str_result_folder_path), dict_params
        elif model_type == 'rf':
            dict_params = {'n_estimators': [1, 3, 5, 10],
                           'max_features': [0.1, 0.5, 1, 2, None]}
            if self.str_mode == 'reg':
                dict_params['criterion'] = ['mse', 'mae']
            elif self.str_mode == 'cls':
                dict_params['criterion'] = ['gini', 'entropy']
            return Models.cRFModel(input_dim=self.c_data.input_no, output_shape=self.c_data.output_no, mode=self.str_mode,
                                   result_path=self.str_result_folder_path), dict_params

    def get_mode(self):
        while True:
            print(f"- 분석은 '{colored('예측(회귀)/분류', 'yellow')}'를 수행 할 수 있습니다.")
            # print(f"- 모델은 '{colored('회귀/분류/자연어 분류', 'yellow')}' 3가지로 생성 할 수 있습니다.")
            list_selection = ['예측(회귀)', '분류']
            # list_selection = ['회귀', '분류', '자연어 분류']
            ret = self.get_selection_from_input(list_selection)
            str_selection = list_selection[ret]
            print(f"- '{colored(str_selection, 'yellow')}' 분석을 수행 하시겠습니까?")
            if self.get_yn_from_input():
                print(f"- '{colored(str_selection, 'yellow')}' 분석을 수행 하겠습니다.")
                if ret == 0:
                    return 'reg'
                elif ret == 1:
                    return 'cls'
                else:
                    return False
                # else:
                #     return 'nlp_cls'

    def get_data_folder_path(self):
        while True:
            print("- 데이터 폴더 경로를 입력하세요.")
            str_path = self.get_string_from_input()
            str_path = str_path.strip(' ')
            if os.path.exists(str_path):
                return str_path
            else:
                print('- 데이터 폴더 경로에 이상이 있습니다.')

    @staticmethod
    def get_yn_from_input():
        while True:
            key_in = input("Y/N 입력 :>")
            if key_in == 'y' or key_in == 'Y':
                return True
            elif key_in == 'n' or key_in == 'N':
                return False
            else:
                print('- 다른 문자가 입력되었습니다. 다시 입력 바랍니다.')

    @staticmethod
    def get_selection_from_input(list_selection):
        while True:
            list_idx = []
            str_print = ""
            for idx, selection in enumerate(list_selection):
                str_print += f"{idx+1}: {selection} "
                list_idx.append(idx+1)

            print(f"- {colored(str_print, 'yellow')}에서 선택하세요.")
            key_in = input(f"선택 :>")
            if int(key_in) in list_idx:
                return int(key_in) - 1
            else:
                print('- 다른 문자가 입력되었습니다. 다시 입력 바랍니다.')

    def get_string_from_input(self, f_yn=True):
        while True:
            str_in = input("문자열 입력 :>")
            if f_yn:
                print(f"- '{colored(str_in, 'yellow')}'이/가 맞습니까?")
                if self.get_yn_from_input():
                    return str_in
                else:
                    print('- 다시 입력 바랍니다.')
                    continue
            else:
                return str_in

    def set_model_path(self, dict_data=None):
        self.str_time = self.get_time()
        self.str_model_number = f'models_{self.str_time}'

        try:
            dir_name = self.str_data_path.split('\\')[-1]
        except Exception as e:
            print(e)
            dir_name = self.str_data_path.split('/')[-1]

        self.str_result_folder_path = os.path.join(self.str_model_dir, self.str_model_number + f'_{dir_name}')
        self.str_model_path = self.str_result_folder_path
        print(f'- Model path : {self.str_result_folder_path}')
        # os.makedirs(self.str_result_folder_path)

        self.str_result_file_path = f'{self.str_result_folder_path}/weights.ckpt'

        if dict_data is not None:
            with open(f'{self.str_result_folder_path}/config.txt', 'w') as f:
                for key in dict_data.keys():
                    f.write(f'{key}=\t{dict_data[key]}\n')


if __name__ == '__main__':
    c_main = cMain()
    c_main.main()
