from ModelTemplates import cModelTemplates
from keras.layers import Bidirectional, LSTM, Dense, Input
from keras.models import Model
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from FixedBatchNormalization import FixedBatchNormalization
from Data import cGetData



class cNNModel(cModelTemplates):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.monitoring_target = 'val_accuracy'
        self.patience = 10
        self.model_type = 'NN'

    def build_model(self, dict_params):
        units = dict_params['units']
        last_activation = dict_params['last_activation']
        nb_layers = dict_params['nb_layers']
        optimizer = dict_params['optimizer']
        loss = dict_params['loss']

        input_layer = Input(shape=(self.input_dim,))
        layer = Dense(units, activation='relu')(input_layer)
        layer = FixedBatchNormalization()(layer)

        for i in range(nb_layers):
            layer = Dense(units, activation='relu')(layer)
            layer = FixedBatchNormalization()(layer)

        layer = Dense(self.output_shape, activation=last_activation)(layer)

        model = Model(inputs=input_layer, outputs=layer)

        model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])

        return model

    def search(self, list_dict_params, train_x, train_y, scaler_x, scaler_y, cv=1, epochs=10):
        # super().search(list_dict_params, train_x, train_y)
        # x, y, scaler_x, scaler_y = cGetData.data_scale_for_search(train_x, train_y, self.mode)
        x, y = cGetData.data_scale_for_train(train_x, train_y, scaler_x, scaler_y, self.mode)

        # list_result = []
        min_loss = 10e10
        dict_result = {}
        best_model = None
        for itr, dict_params in enumerate(list_dict_params):
            print(f"{itr+1}/{len(list_dict_params)}")
            for n_cv in range(cv):
                self.model = self.build_model(dict_params)

                hist = self.model.fit(x, y, epochs=epochs, verbose=0)
                loss = min(hist.history['loss'])
                # acc = max(hist.history['accuracy'])

                # dict_result = {'params': dict_params, 'loss': loss, 'acc': acc}
                # list_result.append(dict_result)

                str_tm = self.get_time()
                print(f"loss : {loss}\t{str_tm}")
                # print(f"loss : {loss}, accuracy : {acc}")

                if min_loss > loss:
                    min_loss = loss
                    dict_result['params'] = dict_params
                    dict_result['loss'] = loss
                    best_model = self.model

        self.model = best_model

        return dict_result

    def train(self, train_x, train_y, scaler_x=None, scaler_y=None, dict_params=None, epochs=1000):
        x, y = cGetData.data_scale_for_train(train_x, train_y, scaler_x, scaler_y, self.mode)

        if dict_params is not None:
            self.model = self.build_model(dict_params)
        # cb_mc = ModelCheckpoint(
        #     self.str_result_file_path.replace('.ckpt', '_{epoch:04d}_{val_accuracy:0.4f}_{val_loss:0.4f}.ckpt'),
        #     monitor=f'{self.monitoring_target}',
        #     save_best_only=True,
        #     save_weights_only=True)
        # cb_es = EarlyStopping(monitor=f'{self.monitoring_target}', patience=self.patience, restore_best_weights=True)
        # cb_tm = PrintTime()
        # cb_tb = TensorBoard(self.str_result_folder_path)

        self.model.fit(x, y, epochs=epochs, validation_split=0.3, verbose=1)


class cRFModel(cModelTemplates):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_type = 'RF'

    def load_model(self, str_path):
        self.model = joblib.load(str_path)

    def build_model(self, dict_param=None):
        model = None
        if self.mode.lower() in ['cls', 'classifier']:
            if dict_param is not None:
                model = RandomForestClassifier(n_estimators=dict_param['n_estimators'],
                                               criterion=dict_param['criterion'],
                                               max_features=dict_param['max_features'])
            else:
                model = RandomForestClassifier()
        elif self.mode.lower() in ['reg', 'regressor']:
            if dict_param is not None:
                model = RandomForestRegressor(n_estimators=dict_param['n_estimators'],
                                              criterion=dict_param['criterion'],
                                              max_features=dict_param['max_features'])
            else:
                model = RandomForestRegressor()

        return model

    def search(self, list_dict_params, train_x, train_y, scaler_x, scaler_y, cv=3):
        x, y = cGetData.data_scale_for_train(train_x, train_y, scaler_x, scaler_y, self.mode)
        # x, y, scaler_x, scaler_y = cGetData.data_scale_for_search(train_x, train_y, self.mode)

        min_loss = 10e10
        dict_result = {}
        best_model = None
        for itr, dict_params in enumerate(list_dict_params):
            print(f"{itr + 1}/{len(list_dict_params)}")
            for n_cv in range(cv):
                self.model = self.build_model(dict_params)
                self.model.fit(x, y)

                # acc = self.model.oob_score_

                pred = self.model.predict(x)
                loss = mean_squared_error(y, pred)
                # dict_result = {'params': dict_params, 'loss': loss, 'acc': acc}
                # list_result.append(dict_result)

                str_tm = self.get_time()

                print(f"loss : {loss}\t{str_tm}")
                # print(f"loss : {loss}, acc: {acc}")
                if min_loss > loss:
                    min_loss = loss
                    dict_result['params'] = dict_params
                    dict_result['loss'] = loss
                    best_model = self.model

        self.model = best_model
        # # max_acc = 0
        # min_loss = 10e10
        # # dict_max_acc = {}
        # dict_min_loss = {}
        # for result in list_result:
        #     # if max_acc < result['acc']:
        #     #     if max_acc == 0:
        #     #         max_acc = result['acc']
        #     #         dict_max_acc = result
        #     #     else:
        #     #         if dict_max_acc['loss'] > result['loss']:
        #     #             max_acc = result['acc']
        #     #             dict_max_acc = result
        #     if min_loss > result['loss']:
        #         min_loss = result['loss']
        #         dict_min_loss = result

        return dict_result

    def train(self, train_x, train_y, scaler_x=None, scaler_y=None, dict_params=None):
        x, y = cGetData.data_scale_for_train(train_x, train_y, scaler_x, scaler_y, self.mode)

        if dict_params is not None:
            self.model = self.build_model(dict_params)

        self.model.fit(x, y)
