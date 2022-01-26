from snownlp import SnowNLP
import pandas as pd
from collections import defaultdict
import os
import re
import jieba
import codecs

#读取评论内容的.txt文件
txt = open('./data/ceshi.txt',encoding='utf-8')
text = txt.readlines()
print(text)

#确认读取文件成功，并关闭文件节省资源
print('读入成功')
txt.close()

#遍历每一条评论，得到每条评论是positive文本的概率，每条评论计算完成后输出ok确认执行成功
comments = []
comments_score = []
for i in text:
    a1 = SnowNLP(i)
    a2 = a1.sentiments
    comments.append(i)
    comments_score.append(a2)
    print('ok')

#将结果数据框存为.xlsx表格，查看结果及分布
table = pd.DataFrame(comments, comments_score)
print(table)
table.to_excel('./data/ceshi.xlsx', sheet_name='result')
#打分范围是[0-1]，此次定义[0,0.5]为负向评论，(0.5,1]为正向评论，观察其分布。


#基于波森情感词典计算情感值
def getscore(text):
    df = pd.read_table(r"./data/BosonNLP_sentiment_score.txt", sep=" ", names=['key', 'score'])
    key = df['key'].values.tolist()
    score = df['score'].values.tolist()
    # jieba分词
    segs = jieba.lcut(text,cut_all = False) #返回list
    # 计算得分
    score_list = [score[key.index(x)] for x in segs if(x in key)]
    return sum(score_list)

#读取文件
def read_txt(filename):
    with open(filename,'r',encoding='utf-8')as f:
        txt = f.read()
    return txt
#写入文件
def write_data(filename,data):
    with open(filename,'a',encoding='utf-8')as f:
        f.write(data)

if __name__=='__main__':
    text = read_txt('./data/ceshi.txt')
    lists  = text.split('\n')
    i = 0
    for list in lists:
        if list  != '':
            sentiments = round(getscore(list),2)
            #情感值为正数，表示积极；为负数表示消极
            print(list)
            print("情感值：",sentiments)
            if (-1<=sentiments < -0.2):
                print("机器标注情感倾向：一塌糊涂\n")
                s = "机器判断情感倾向：一塌糊涂\n"
            elif(-0.2<=sentiments < 0.2):
                print('机器标注情感倾向：味同嚼蜡\n')
                s = "机器判断情感倾向：味同嚼蜡"+'\n'
            elif (0.2 <= sentiments < 0.6):
                print('机器标注情感倾向：差强人意\n')
                s = "机器判断情感倾向：差强人意" + '\n'
            elif (0.6 <= sentiments < 0.8):
                print('机器标注情感倾向：瑕不掩瑜\n')
                s = "机器判断情感倾向：瑕不掩瑜" + '\n'
            elif (0.8 <= sentiments <= 1):
                print('机器标注情感倾向：一致好评\n')
                s = "机器判断情感倾向：一致好评" + '\n'
            sentiment = '情感值：'+str(sentiments)+'\n'
            #文件写入
            filename = 'BosonNLP情感分析结果.txt'
            write_data(filename,'情感分析文本：')
            write_data(filename,list+'\n') #写入待处理文本
            write_data(filename,sentiment) #写入情感值
            #write_data(filename,al_sentiment) #写入机器判断情感倾向
            write_data(filename,s+'\n') #写入人工标注情感
            i = i+1
