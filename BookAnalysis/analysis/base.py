#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/25 08:14
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : base.py
# @Software: PyCharm
import os

import pandas as pd


class Base:
    def __init__(self, filename):
        data_file = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'data', filename)
        df = pd.read_csv(data_file).drop_duplicates()
        if filename == 'bookInfo.csv':
            df['author'] = df['author'].str.replace(r'\s+', '', regex=True)
        self.df = df

    def getData(self):
        raise NotImplementedError


if __name__ == '__main__':
    data1 = pd.read_csv('./bookComment1.csv')
    data2 = pd.read_csv('./bookComment2.csv')
    data3 = pd.read_csv('./bookComment3.csv')
    data4 = pd.read_csv('./bookComment4.csv')
    data5 = pd.read_csv('./bookComment5.csv')
    pd.concat([data1, data2, data3, data4, data5]).to_csv('./bookComment.csv', index=False)
    data = pd.read_csv('./bookInfo.csv')
    print(data.info())
    print(data.shape)
    # data.iloc[:, 1:].to_csv('./bookInfo.csv', index=False)
    print(data.drop_duplicates().shape)
