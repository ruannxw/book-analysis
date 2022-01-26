#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/25 08:38
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : everyMonthPublishNum.py
# @Software: PyCharm
import pandas as pd

from BookAnalysis.analysis.base import Base


class Analysis(Base):
    def __init__(self, filename=None):
        if filename is None:
            filename = 'bookInfo.csv'
        super().__init__(filename)

    def getData(self):
        df: pd.DataFrame = self.df.copy()
        df['publicationYear'] = pd.to_datetime(df['publicationYear'], errors='coerce')
        df = df.dropna(subset=['publicationYear'])
        df['publicationMonth'] = df['publicationYear'].dt.month
        df = df['publicationMonth']
        data = df.value_counts(sort=False)
        # print(df.resample('1M').sum())
        return {
            'xAxis': data.index.tolist(),
            'yAxis': data.values.tolist()
        }


if __name__ == '__main__':
    print(Analysis().getData())
