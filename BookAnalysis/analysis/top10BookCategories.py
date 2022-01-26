#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/25 08:07
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : top10BookCategories.py
# @Software: PyCharm

import pandas as pd

from BookAnalysis.analysis.base import Base


class Analysis(Base):
    def __init__(self, filename=None):
        if filename is None:
            filename = 'categories.csv'
        super().__init__(filename)

    def getData(self):
        df: pd.DataFrame = self.df.loc[:, ['tag', 'num']]

        df = df.sort_values(by='num', ascending=False).head(10)
        return {
            'xAxis': df['tag'].tolist(),
            'yAxis': df['num'].tolist()
        }


if __name__ == '__main__':
    # data_file = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'data', 'categories.csv')
    analysis = Analysis('categories.csv')
    print(analysis.getData())
