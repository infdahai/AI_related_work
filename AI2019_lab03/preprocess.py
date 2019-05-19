import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
import random


# import pysnooper

# @pysnooper.snoop()
def load_data(filename: str, data: list):  # train_data: list, test_data: list, ratio=0.8):
    ends = '.txt'
    with open(filename + ends) as txtData:
        lines = txtData.readlines()
        index = 0
        if filename.endswith('EEG_feature'):
            for line in lines:
                lineData = line.strip().split('\t')
                lineData = list(map(float, lineData))
                dict_temp = {}
                dict_temp['id'] = index
                dict_temp['theta'] = lineData[0:31]
                dict_temp['slow_alpha'] = lineData[32:63]
                dict_temp['alpha'] = lineData[64:95]
                dict_temp['beta'] = lineData[96:127]
                dict_temp['gamma'] = lineData[128:-1]
                index += 1
                data.append(dict_temp)
                """
                          if random.random() < ratio:
                              train_data.append(lineData)
                          else:
                              test_data.append(lineData)
                          """
        elif filename.endswith('subject_video'):
            for line in lines:
                line = line.strip().split('\t')
                line = list(map(int, line))
                data[index]['pp_num'] = line[0]
                data[index]['vi_num'] = line[1]
                index += 1
        elif filename.endswith('valence_arousal_label'):
            for line in lines:
                line = line.strip().split('\t')
                line = list(map(int, line))
                data[index]['happy'] = line[0] - 1
                data[index]['wake'] = line[1] - 1
                index += 1
        elif filename.endswith('category'):
            for line in lines:
                line = line.strip().split('\t')
                line = list(map(int, line))
                data[index]['emotion'] = line[0]
                index += 1
        else:
            raise ValueError("pass wrong file name")

    return data



def split_data(dataSet):
    character = []
    label = []
    for i in range(len(dataSet)):
        character.append([int(temp) for temp in dataSet[i][:-1]])
    return np.array(character), np.array(label)


data_list = []
import os

dir_pre = os.getcwd() + '/Data/DEAP/'
data1_1 = dir_pre + 'EEG_feature'
data1_2 = dir_pre + 'subject_video'
data1_3 = dir_pre + 'valence_arousal_label'

data_list = load_data(data1_1, data_list)
data_list = load_data(data1_2, data_list)
data_list = load_data(data1_3, data_list)
# print(data_list)

dir_pre_2 = os.getcwd() + '/Data/MAHNOB-HCI/'
data2_1 = dir_pre_2 + 'EEG_emotion_category'
data2_2 = dir_pre_2 + 'EEG_feature'
data2_3 = dir_pre_2 + 'subject_video'
data2_4 = dir_pre_2 + 'valence_arousal_label'

data_list_2 = load_data(data2_2, [])
data_list_2 = load_data(data2_1, data_list_2)
data_list_2 = load_data(data2_3, data_list_2)
data_list_2 = load_data(data2_4, data_list_2)

