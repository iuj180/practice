class cGridSearch:
    @staticmethod
    def get_grid(dict_params):
        total_nb = 1
        list_len = []

        # get total number of combination
        for key in dict_params.keys():
            total_nb *= len(dict_params[key])
            list_len += [len(dict_params[key])]

        # make a list with each columns length
        list_each_length = [1] * len(list_len)

        for idx, i in enumerate(range(len(list_len) - 1, 0, -1)):
            for j in range(len(list_each_length) - idx - 1):
                list_each_length[j] *= list_len[i]

        list_pre_grid = []
        for key_idx, key in enumerate(dict_params.keys()):
            idx = 0
            list_temp = []
            while idx < total_nb:
                for value in dict_params[key]:
                    for i in range(list_each_length[key_idx]):
                        list_temp.append(value)
                        idx += 1
            list_pre_grid.append(list_temp)

        list_grid = []
        for i in range(total_nb):
            dict_grid = {}
            for idx, key in enumerate(dict_params.keys()):
                dict_grid[key] = list_pre_grid[idx][i]
            list_grid.append(dict_grid)

        return list_grid

    # @staticmethod
    # def get_grid(dict_params):
    #     list_grid = []
    #     total_nb = 1
    #     list_len = []
    #     for key in dict_params.keys():
    #         total_nb *= len(dict_params[key])
    #         list_len += [len(dict_params[key])]
    #
    #     for idx in range(total_nb):
    #         dict_grid = {}
    #         for key in dict_params.keys():
    #             item_idx = idx % len(dict_params[key])
    #             dict_grid[key] = dict_params[key][item_idx]
    #         list_grid.append(dict_grid)
    #
    #     return list_grid
