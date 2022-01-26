#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/25 17:16
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : dynamicNumberOfPublisher.py
# @Software: PyCharm
import numpy as np
import pandas as pd

from BookAnalysis.analysis.base import Base


class Analysis(Base):
    def __init__(self, filename=None):
        if filename is None:
            filename = 'bookInfo.csv'
        super().__init__(filename)

    def getData(self):
        """
        1900, author1, 1
        1900, author2, 3
        1900, author3, 3
        """
        df: pd.DataFrame = self.df.copy()
        df['publicationYear'] = pd.to_datetime(df['publicationYear'], errors='coerce')
        df = df.dropna(subset=['publicationYear'])
        df['publicationYear'] = df['publicationYear'].dt.year
        df = df.loc[:, ['publicationYear', 'author', 'url']]

        # s: pd.Series = df.groupby(['publicationYear', 'author'])['url'].value_counts()

        # df = df.set_index(['publicationMonth', 'author'])

        # df.insert(0, 'num', s)
        years = list(np.sort(df['publicationYear'].unique()))
        # print(len(years), df['author'].unique().size)
        # df_year = pd.DataFrame(data=np.sort(df['publicationYear'].unique()), columns=['year'])
        # df_author = pd.DataFrame(data=df['author'].unique(), columns=['author'])
        #
        # print(df_year.head())
        # print(df_author.head())
        # print(pd.concat([df_year, df_author], axis=1))
        # print(df.set_index('author'))
        # print(df['author'].unique().size)
        df_ans = pd.DataFrame()
        # print(df_ans)
        _ans = {
            'years': [str(year) for year in years],
            'data': {}
        }
        # 累计！！
        for year in years:
            df_ = df[df['publicationYear'] == year]
            s: pd.Series = df_['author'].value_counts(sort=False)
            s.name = year
            # print(s.head(8))
            # print(s.index)
            # # print(s.values)
            # pd_s = pd.Series(data=s.values, index=s.index, name=year)
            # print(pd.concat([df_ans, pd_s], axis=1))
            df_ans = df_ans.join(s, how='outer')
            # print(pd.DataFrame(data=s, columns=df_.columns))
            # _ans[year] = {
            #     'author': s.index.tolist(),
            #     'num': s.values.tolist()
            # }
            # break

        df_ans: pd.DataFrame = df_ans.T.fillna(0).cumsum()
        # df_ans.group_by('')
        # print(df_ans.head())
        # print(df_ans.index, df_ans.columns,df_ans.describe())
        # print('End')
        for index in range(len(years)):
            s_: pd.Series = df_ans.iloc[index].sort_values(ascending=False).head(10)
            # print(s_)
            _ans['data'][int(years[index])] = {
                'xAxis': s_.index.tolist(),
                'yAxis': s_.values.tolist()
            }
        return _ans


if __name__ == '__main__':
    print(Analysis().getData())
