#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @Time    : 2022/1/26 09:58
# @Author  : RuanXinWei (https://github.com/Ruan-XinWei/)
# @File    : goodComment.py
# @Software: PyCharm
from BookAnalysis.analysis.base import Base


class Analysis(Base):
    def __init__(self, filename=None):
        if filename is None:
            filename = 'bookCo'
        super().__init__(filename)

    def getData(self):
        pass