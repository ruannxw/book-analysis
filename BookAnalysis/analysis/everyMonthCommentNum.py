#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/25 10:31
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : everyMonthCommentNum.py
# @Software: PyCharm
import pandas as pd

from BookAnalysis.analysis.base import Base


class Analysis(Base):
    def __init__(self, filename=None):
        if filename is None:
            filename = 'bookComment.csv'
        super().__init__(filename)

    def getData(self):
        df: pd.DataFrame = self.df.copy()
        df['time'] = pd.to_datetime(df['time'], errors='coerce')
        df = df.dropna(subset=['time'])
        df['Month'] = df['time'].dt.month
        df = df['Month']
        data = df.value_counts(sort=False)
        # print(df.resample('1M').sum())
        return {
            'xAxis': data.index.tolist(),
            'yAxis': data.values.tolist()
        }


if __name__ == '__main__':
    print(Analysis().getData())