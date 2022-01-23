import csv
import os
import re

import requests
from lxml import etree


class BookInfo:
    def __init__(self, url, parentTag=None, tag=None, outfile=None):
        """
        爬取 Book 基本信息

        :param url: Book url 例如：'https://book.douban.com/subject/35534519/'
        :param parentTag: 父标签 例如：文学
        :param tag: 标签 例如：小说
        :param outfile: 文件路径
        """
        # self._url = 'https://book.douban.com/subject/35534519/'
        self._url = url
        self._method = 'GET'
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }
        if outfile is None:
            self._outfile = 'bookInfo.csv'
        else:
            self._outfile = outfile
        self.parentTag = parentTag
        self.tag = tag

    def crawl(self):
        resp = requests.request(method=self._method, url=self._url, headers=self._headers)
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

    def parse(self, content):
        # 这里注意要按照 列表顺序来
        _ans = [self.parentTag, self.tag, self._url]
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
        title = ['parentTag', 'tag', 'url', 'name', 'author', 'publisher', 'producer', 'originalName', 'translator',
                 'publicationYear', 'pages', 'price', 'bind', 'series', 'isbn', 'score', 'evaluator', 'content',
                 'introductionAuthor', 'menu', ]
        if not os.path.exists(self._outfile):
            with open(self._outfile, mode='w', newline="", encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(title)
        with open(self._outfile, mode='a', newline="", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    def run(self):
        content = self.crawl()
        data = self.parse(content)
        self.save(data)


if __name__ == '__main__':
    bookInfo = BookInfo(url='https://book.douban.com/subject/4913064/', parentTag='文学', tag='小说')
    bookInfo.run()
