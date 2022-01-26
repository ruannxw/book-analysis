#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/26 10:02
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : base.py
# @Software: PyCharm
import os

import pandas as pd


class Util:
    @classmethod
    def readCsv(cls, filename) -> pd.DataFrame:
        data_file = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'data', filename)
        return pd.read_csv(data_file).drop_duplicates()

    @classmethod
    def getCommentUrlByName(cls, name=None) -> str:
        """
        通过书籍名字 获取评论链接
        :param name: 书籍名字
        :return: str 评论链接
        """
        util = cls()
        if name:
            df = util.readCsv('bookInfo.csv')
            df = df.loc[:, ['url', 'name']]
            df = df[df['name'] == name]['url']
            if len(df.values) > 1:
                subject_url = df.values[0]
                return subject_url + 'comments/'
        df = util.readCsv('bookComment.csv')

        return df.groupby('url')['comment'].count().idxmax()


if __name__ == '__main__':
    # print(Util.getCommentUrlByName('摩登时代'))
    print(Util.getCommentUrlByName())
