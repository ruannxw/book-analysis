#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/25 23:50
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : commentCategories.py
# @Software: PyCharm
import jieba
import pandas as pd
from snownlp import SnowNLP
from BookAnalysis.utils.base import Util

from BookAnalysis.analysis.base import Base


class Analysis(Base):
    def __init__(self, filename=None):
        if filename is None:
            filename = 'bookComment.csv'
        super().__init__(filename)

    def getScore(self, score):
        if 0 <= score < 0.2:
            return '一塌糊涂'
        elif 0.2 <= score < 0.4:
            return '味同嚼蜡'
        elif 0.4 <= score < 0.6:
            return '差强人意'
        elif 0.6 <= score < 0.8:
            return '瑕不掩瑜'
        elif 0.8 <= score <= 1:
            return '一致好评'

    def getData(self, name=None):
        # print(self.df.columns)
        # Index(['person', 'star', 'time', 'score', 'comment', 'url'], dtype='object')
        # 一塌糊涂[0  , 0.2)
        # 味同嚼蜡[0.2, 0.4)
        # 差强人意[0.4, 0.6)
        # 瑕不掩瑜[0.6, 0.8)
        # 一致好评[0.8, 1  ]
        comment_url = Util.getCommentUrlByName(name)
        df = self.df[self.df['url'] == comment_url]
        comments = df['comment'].astype(str).tolist()
        _ans = {}
        for comment in comments:
            words = jieba.cut(comment, use_paddle=True)
            scores = 0
            number = 0
            for word in words:
                if number > 20:
                    break
                if len(word) == 1:
                    continue
                else:
                    sn = SnowNLP(word)
                    scores += sn.sentiments
                    number += 1
                    # print(word, scores)
            if number > 0:
                scores /= number
            key = self.getScore(scores)
            _ans[key] = _ans.get(key, 0) + 1
        print(_ans)
        return _ans


if __name__ == '__main__':
    Analysis().getData()
