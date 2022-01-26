#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/25 10:57
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : ProportionOfChineseAndForeignAuthors.py
# @Software: PyCharm
import pandas as pd

from BookAnalysis.analysis.base import Base


# 饼状图，中外作者占比
class Analysis(Base):
    def __init__(self, filename=None):
        if filename is None:
            filename = 'bookInfo.csv'
        super().__init__(filename)

    def getData(self):
        s: pd.Series = self.df['translator'].isna().value_counts()
        return {
            '中文书籍': int(s[False]),
            '外文书籍': int(s[True])
        }


if __name__ == '__main__':
    print(Analysis().getData())
