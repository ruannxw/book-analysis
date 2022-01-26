#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/25 23:16
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : wordCloud.py
# @Software: PyCharm
import jieba
import pandas as pd

from BookAnalysis.analysis.base import Base


class Analysis(Base):
    def __init__(self, filename=None):
        if filename is None:
            filename = 'bookComment.csv'
        super().__init__(filename)

    def getData(self):
        url = self.df['url'].value_counts().idxmax()
        df: pd.DataFrame = self.df.loc[self.df['url'] == url]
        # print(df.head())
        # print(df.shape)
        # print(df.columns)
        comments = df['comment'].astype(str).tolist()
        counts = {}
        for comment in comments:
            words = jieba.cut(comment, use_paddle=True)
            for word in words:
                if len(word) == 1:
                    continue
                else:
                    counts[word] = counts.get(word, 0) + 1
        # _ans = []
        # for key, value in counts.items():
        #     _ans.append({
        #         "name": key,
        #         "value": value
        #     })
        # print(counts)
        # print(_ans)
        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        _ans = []
        for key, value in counts:
            if len(_ans) > 200:
                break
            _ans.append({
                "name": key,
                "value": value
            })
        return _ans


if __name__ == '__main__':
    print(Analysis().getData())
