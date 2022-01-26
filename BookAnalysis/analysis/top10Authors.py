#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/25 11:32
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : top10Authors.py
# @Software: PyCharm
import pandas as pd

from BookAnalysis.analysis.base import Base


class Analysis(Base):
    def __init__(self, filename=None):
        if filename is None:
            filename = 'bookInfo.csv'
        super().__init__(filename)

    def getData(self):
        df: pd.Series = self.df['author']

        s = df.value_counts().head(10)
        return {
            'xAxis': s.index.tolist(),
            'yAxis': s.values.tolist()
        }


if __name__ == '__main__':
    print(Analysis().getData())
