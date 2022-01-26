# -*- coding: utf-8 -*-
"""
  File Name：       01-lxml解析html类型的网页数据
  Description :
  Author :          Nick
  date：            2022/1/14
  Change Activity:  2022/1/14:
"""
import csv
import re

from bs4 import BeautifulSoup

import requests as req
from lxml import etree

class douban_book(object):


    def __init__(self):
        self.url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'cookie':'bid=8VCu41ZQMMo; douban-fav-remind=1; __gads=ID=de37cda864995fe6-22e8304ca2cb00a0:T=1631717131:RT=1631717131:S=ALNI_MZjXIbdfEkt_Fj1bVDfoxYm7C7fPQ; __utmz=30149280.1631717153.1.1.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; ll="118196"; __utmz=81379588.1642732823.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ct=y; gr_user_id=a370231d-0ec0-4380-96df-deab89a5c804; _vwo_uuid_v2=D28DC766E0E8543401F20AA041D785C94|c60b20a81f64427e334b9f4a6f9d5d03; __yadk_uid=o4WiBaqshyMjWPypg1VvmS31qCQcb1oP; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1642749577; viewed="35268281_35534519_4913064"; dbcl2="253041130:Slf6/LDpRbQ"; push_noty_num=0; push_doumail_num=0; ck=5vto; __utmc=30149280; __utmc=81379588; __utmv=30149280.25304; __utma=30149280.876215542.1631717153.1642762417.1642765842.14; __utma=81379588.99363961.1642732823.1642762417.1642765842.9; _pk_ses.100001.3ac3=*; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=b308dd97-a6f5-47a9-806b-8500668a6984; gr_cs1_b308dd97-a6f5-47a9-806b-8500668a6984=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_b308dd97-a6f5-47a9-806b-8500668a6984=true; __utmt_douban=1; __utmt=1; _pk_id.100001.3ac3=a2e4d27bb14aaf5b.1642732823.9.1642767362.1642763465.; __utmb=30149280.22.10.1642765842; __utmb=81379588.20.10.1642765842'
        }


    # 1.爬取数据
    def crawl(self):
        resp = req.get(self.url, headers = self.headers)
        html = resp.content.decode("utf-8")
        return html



    # 2.解析数据
    def parse(self, html):
        root = etree.HTML(html)
        url2 = "https://book.douban.com"
        parentTag= root.xpath("//*[@id='content']/div/div[1]/div[2]/div[@class]")

        books = [['书名','作者', '出版社', '原作名', '译者', '出版年', '页数', '价格','装帧', 'isbn', '分数', '评价人数', '内容简介', '作者简介', '目录']]
        #books = [['父标签','标签']]
        #books = [['父标签']]

        for c in parentTag:
            tag1 = c.xpath("./a/h2/text()")[0].strip()  # 父标签
            tag2 = tag1[::-1]
            tag3 = tag2[12:]
            #list1.append(tag3[::-1])
            tags_tr =c.xpath("./table/tbody/tr")
            for d in tags_tr:
                for e in d:
                    #list1.append( e.xpath("./a/text()")[0].strip())  # 标签
                    url1 = e.xpath("./a//@href")[0].strip()  # 网址
                for i in range(0,200,20):
                    list1 = []
                    url5 ='?start=%s&type=T'%i
                    url3=url2+url1+url5
                    #list1.append(url3)
                    headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
                            'cookie': 'bid=8VCu41ZQMMo; douban-fav-remind=1; __gads=ID=de37cda864995fe6-22e8304ca2cb00a0:T=1631717131:RT=1631717131:S=ALNI_MZjXIbdfEkt_Fj1bVDfoxYm7C7fPQ; __utmz=30149280.1631717153.1.1.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; ll="118196"; __utmz=81379588.1642732823.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ct=y; gr_user_id=a370231d-0ec0-4380-96df-deab89a5c804; _vwo_uuid_v2=D28DC766E0E8543401F20AA041D785C94|c60b20a81f64427e334b9f4a6f9d5d03; __yadk_uid=o4WiBaqshyMjWPypg1VvmS31qCQcb1oP; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1642749577; viewed="35268281_35534519_4913064"; dbcl2="253041130:Slf6/LDpRbQ"; push_noty_num=0; push_doumail_num=0; ck=5vto; __utmc=30149280; __utmc=81379588; __utmv=30149280.25304; __utma=30149280.876215542.1631717153.1642762417.1642765842.14; __utma=81379588.99363961.1642732823.1642762417.1642765842.9; _pk_ses.100001.3ac3=*; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=b308dd97-a6f5-47a9-806b-8500668a6984; gr_cs1_b308dd97-a6f5-47a9-806b-8500668a6984=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_b308dd97-a6f5-47a9-806b-8500668a6984=true; __utmt_douban=1; __utmt=1; _pk_id.100001.3ac3=a2e4d27bb14aaf5b.1642732823.9.1642767362.1642763465.; __utmb=30149280.22.10.1642765842; __utmb=81379588.20.10.1642765842'
                    }
                    respe = req.get(url3, headers=headers)
                    html1 = respe.content.decode("utf-8")
                    root1 = etree.HTML(html1)
                    names=root1.xpath("//*[@id='subject_list']/ul/li[@class='subject-item']")
                    try:
                        for c in names:
                            url4=c.xpath("./div[2]/h2/a//@href")[0].strip()
                            name=c.xpath("./div[2]/h2/a/text()")[0].strip()
                            list1.append(name)
                            print(name)
                            headers = {
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
                                    'cookie': 'bid=8VCu41ZQMMo; douban-fav-remind=1; __gads=ID=de37cda864995fe6-22e8304ca2cb00a0:T=1631717131:RT=1631717131:S=ALNI_MZjXIbdfEkt_Fj1bVDfoxYm7C7fPQ; __utmz=30149280.1631717153.1.1.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; ll="118196"; __utmz=81379588.1642732823.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ct=y; gr_user_id=a370231d-0ec0-4380-96df-deab89a5c804; _vwo_uuid_v2=D28DC766E0E8543401F20AA041D785C94|c60b20a81f64427e334b9f4a6f9d5d03; __yadk_uid=o4WiBaqshyMjWPypg1VvmS31qCQcb1oP; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1642749577; viewed="35268281_35534519_4913064"; dbcl2="253041130:Slf6/LDpRbQ"; push_noty_num=0; push_doumail_num=0; ck=5vto; __utmc=30149280; __utmc=81379588; __utmv=30149280.25304; __utma=30149280.876215542.1631717153.1642762417.1642765842.14; __utma=81379588.99363961.1642732823.1642762417.1642765842.9; _pk_ses.100001.3ac3=*; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=b308dd97-a6f5-47a9-806b-8500668a6984; gr_cs1_b308dd97-a6f5-47a9-806b-8500668a6984=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_b308dd97-a6f5-47a9-806b-8500668a6984=true; __utmt_douban=1; __utmt=1; _pk_id.100001.3ac3=a2e4d27bb14aaf5b.1642732823.9.1642767362.1642763465.; __utmb=30149280.22.10.1642765842; __utmb=81379588.20.10.1642765842'
                            }
                            respe = req.get(url4, headers=headers)
                            html1 = respe.content.decode("utf-8")
                            root2 = etree.HTML(html1)

                            infos = root2.xpath("//*[@id='info']")[0]
                            #print(len(infos.xpath("./span[1]/span")))
                            if len(infos.xpath("./span[1]/span"))==1:
                                author = infos.xpath("./span[1]/a/text()")[0].strip()
                            else :
                                author = infos.xpath("./a[1]/text()")[0].strip()
                            #print(author)
                            list1.append(author)
                            sect = root2.xpath("//*[@id='interest_sectl']")
                            spans = infos.xpath('./span[@class="pl"]')
                            list2 = []
                            list3 = []
                            list4 = ['出版社:', '原作名:', '译者:', '出版年:', '页数:', '定价:', '装帧:', 'ISBN:']
                            for d in spans:
                                list2.append(d.xpath('string(.)'))
                                list3.append(d.tail.strip())
                            for i in range(8):
                                k = 0
                                for j in range(len(list2)):
                                    if list2[j] == list4[i]:
                                        list1.append(list3[j])
                                        k = k + 1
                                if k == 0:
                                    list1.append('')


                            for e in sect:
                                score = e.xpath("./div/div[2]/strong/text()")[0].strip()
                                evaluator = e.xpath("./div/div[2]/div/div[2]/span/a/span/text()")[0].strip()

                            list1.append(score)
                            list1.append(evaluator)
                            content = ''
                            introductionAuthor = ''
                            menu = ''
                            root3 = root2.xpath(
                                    "//*[@id='content']/div/div[1]/div[3]/h2[1]/following-sibling::div[1]/div/div/p")
                            for i in root3:
                                content = content + i.xpath("string(.)")
                            list1.append(content)
                            root4 = root2.xpath(
                                    "//*[@id='content']/div/div[1]/div[3]/h2[2]/following-sibling::div[1]/div/div/p")

                            for i in root4:
                                introductionAuthor = introductionAuthor + i.xpath("string(.)")
                            list1.append(introductionAuthor)
                            # introductionAuthor = d.xpath("")[0].strip()
                            #print(len(root2.xpath("//*[@id='content']/div/div[1]/div[3]/h2")))
                            if len(root2.xpath("//*[@id='content']/div/div[1]/div[3]/h2")) == 3:
                                root5 = root2.xpath("//*[@id='content']/div/div[1]/div[3]/h2[3]/following-sibling::div[1]")
                                for i in root5:
                                    menu = menu + i.xpath("string(.)")
                            else:
                                menu = ''
                            list1.append(menu)
                            # menu = d.xpath("")[0].strip()
                            # books.append([ author, publisher,producer, originalName, translator, publicationYear, pages, price, bind,series, isbn, score, evaluator, content, introductionAuthor, menu])
                            books.append(list1)
                    except:
                        pass



        return books

    def save_2_book(self, list_):

        '''3.存储数据到dounan_book_rank文件中'''

        with open(r"../shixunsheji/data/book.csv", 'a', encoding="utf-8-sig") as fd:
            writer = csv.writer(fd)
            writer.writerows(list_)

def main():
    spider = douban_book()
    content = spider.crawl()
    movies = spider.parse(content)
    spider.save_2_book(movies)


if __name__ == '__main__':
    main()
