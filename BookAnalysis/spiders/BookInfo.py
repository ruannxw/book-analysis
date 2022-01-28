import csv
import datetime
import os
import re

import pandas as pd
import requests
from lxml import etree


class BookInfo:
    def __init__(self, outfile=None):
        """
        爬取 Book 基本信息

        :param url: Book url 例如：'https://book.douban.com/subject/35534519/'
        :param parentTag: 父标签 例如：文学
        :param tag: 标签 例如：小说
        :param outfile: 文件路径
        """
        # self._url = 'https://book.douban.com/subject/35534519/'
        # self._url = url
        self._method = 'GET'
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Cookie': 'bid=FhA-heh1N3I; douban-fav-remind=1; __gads=ID=87af6d311b514533-224652d64fc80038:T=1621224671:RT=1621224671:S=ALNI_MYMfbU3W-gYVpItI97n8_S5KkFAbg; gr_user_id=11ed6298-5be6-4f87-b0a1-832cbde4f058; _vwo_uuid_v2=DAFAA56C9C7EDAE380447F88D6B27E40E|c803f7fa217c77f7a701ad99d289b81c; __yadk_uid=IADjl51MmZq2apSWuIC1fLXIOLQOkoSy; ll="118254"; __utmz=30149280.1639653039.17.10.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); push_doumail_num=0; push_noty_num=0; _ga_RXNMP372GL=GS1.1.1642433464.3.1.1642433839.60; __utmv=30149280.25291; _ga=GA1.2.594493052.1621224670; viewed="4913064_35534519_1014278_30358507_30314829_3106534_35651849_23008813_3354490_1964334"; ct=y; __utmc=30149280; __utmz=81379588.1642988222.26.10.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=81379588; _gid=GA1.2.392283503.1642988281; dbcl2="252912989:up8UjoYf/X4"; ck=ssD5; __utma=30149280.594493052.1621224670.1643008591.1643012023.39; __utma=81379588.245870019.1628382789.1643008591.1643012023.32; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1643012023%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1642763100,1643012028; Hm_lpvt_16a14f3002af32bf3a75dfe352478639=1643012028; ap_v=0,6.0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=4b39a224-076b-4795-b3c4-931f0c8239b5; gr_cs1_4b39a224-076b-4795-b3c4-931f0c8239b5=user_id%3A1; __utmt_douban=1; __utmt=1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_4b39a224-076b-4795-b3c4-931f0c8239b5=true; __utmb=30149280.12.10.1643012023; __utmb=81379588.12.10.1643012023; _pk_id.100001.3ac3=d51cee9c57b59460.1628382788.32.1643014581.1643008916.',
            'Host': 'book.douban.com'
        }
        if outfile is None:
            self._outfile = 'bookInfo.csv'
        else:
            self._outfile = outfile

    def crawl(self, url):
        start_time = datetime.datetime.now()
        resp = requests.request(method=self._method, url=url, headers=self._headers, timeout=10)
        end_time = datetime.datetime.now()
        print('req: %sms ' % ((end_time - start_time).microseconds // 1000), end='')
        content = resp.content.decode(resp.encoding)
        return content

    def parseDetailInfo(self, root) -> list:
        """
        解析 细节信息：作者，出版社，出品方，作者，出版社，出品方，原作名，译者，出版年，页数，定价，装帧，丛书，ISBN

        :param root: 根节点
        :return: list
        """
        info = root.xpath('//*[@id="info"]')[0]
        span_titles = [
            "作者:",
            "出版社:",
            "出品方:",
            "原作名:",
            "译者:",
            "出版年:",
            "页数:",
            "定价:",
            "装帧:",
            "丛书:",
            "ISBN:",
        ]
        spans = info.xpath('./span[@class="pl"]')
        span_info_dict = {}
        for span in spans:
            key = span.xpath('string(.)')
            span_info_dict[key] = span.tail.strip()
            if span_info_dict[key] == '':
                span_info_dict[key] = span.xpath('./following-sibling::a[1]//text()')[0].strip()

        spans = info.xpath('./span/span[@class="pl"]')
        for span in spans:
            key = span.xpath('string(.)').strip() + ':'
            span_info_dict[key] = span.xpath('./following-sibling::a[1]//text()')[0].strip()

        _info = []
        for title in span_titles:
            _info.append(span_info_dict.get(title, None))
        return _info

    def parseRelatedInfo(self, root) -> list:
        """
        解析 内容简介,作者简介,目录,
        :param root: 根路径
        :return: 对应的 list
        """
        ralated_info_h2 = root.xpath('//*[@id="content"]/div/div[1]/div[3]/h2')
        ralated_info_dict = {}
        for h2 in ralated_info_h2:
            ralated_title = h2.xpath('./span//text()')[0].strip()
            content = h2.xpath('./following-sibling::div[1]')[0]
            try:
                content = content.xpath('.//div[@class="intro"]')[-1].xpath('string(.)').strip()
            except IndexError:
                content = content.xpath('string(.)').strip()
            ralated_info_dict[ralated_title] = re.sub(' +|\n', ' ', content)
        ralated_info_list = [
            '内容简介',
            '作者简介',
            '目录',
        ]
        _ans = []
        for key in ralated_info_list:
            _ans.append(ralated_info_dict.get(key, None))
        return _ans

    def parse(self, content, tag, url):
        # 这里注意要按照 列表顺序来
        _ans = [tag, url]
        root = etree.HTML(content)
        name = root.xpath('//*[@id="wrapper"]/h1/span//text()')[0].strip()
        _ans.append(name)
        _ans += self.parseDetailInfo(root)
        score = root.xpath('//*[@id="interest_sectl"]/div/div[2]/strong//text()')[0].strip()
        evaluator = root.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span//text()')[0].strip()
        _ans += [score, evaluator]
        _ans += self.parseRelatedInfo(root)

        # content = root.xpath()[0].strip()
        # introductionAuthor = root.xpath()[0].strip()
        # menu = root.xpath()[0].strip()
        return _ans

    def save(self, data):
        title = ['tag', 'url', 'name', 'author', 'publisher', 'producer', 'originalName', 'translator',
                 'publicationYear', 'pages', 'price', 'bind', 'series', 'isbn', 'score', 'evaluator', 'content',
                 'introductionAuthor', 'menu', ]
        if not os.path.exists(self._outfile):
            with open(self._outfile, mode='w', newline="", encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(title)
        with open(self._outfile, mode='a', newline="", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    def run(self, url, tag):
        try:
            content = self.crawl(url)
            data = self.parse(content, url=url, tag=tag)
            self.save(data)
            return True
        except requests.exceptions.ReadTimeout as e:
            return e
        except IndexError as e:
            return e
        except Exception as e:
            return e


if __name__ == '__main__':
    # 1...1000
    # 1000 / 4 = 250
    bookInfo = BookInfo()
    # bookInfo.run(url='https://book.douban.com/subject/34949694/', tag='小说')
    df = pd.read_csv('./bookItem.csv')
    length = len(df.index)
    index = 0  # 0 - 3
    # 步长
    step = length // 4
    # 起始 如果出现多次异常，把这个值设置为控制台中最后成功的数字
    # 例如： start = 900
    start = index * step
    end = (index + 1) * step
    for i in range(start, end):
        tag = df.iloc[i, 0]
        url = df.iloc[i, 1]
        start_time = datetime.datetime.now()
        _ans = bookInfo.run(url=url, tag=tag)
        import time

        time.sleep(1)
        end_time = datetime.datetime.now()
        print(i, tag, url, i, length, _ans, ((end_time - start_time).microseconds // 1000), 'ms')
