import os
import re
import time

import pandas as pd
import requests
from lxml import etree


class BookComment:
    def __init__(self, outfile=None):
        """
        初始化 爬虫
        :param outfile: 输出的文件路径
        """
        if outfile is None:
            outfile = 'bookComment.csv'
        self._outfile = outfile
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Cookie': 'bid=FhA-heh1N3I; douban-fav-remind=1; __gads=ID=87af6d311b514533-224652d64fc80038:T=1621224671:RT=1621224671:S=ALNI_MYMfbU3W-gYVpItI97n8_S5KkFAbg; gr_user_id=11ed6298-5be6-4f87-b0a1-832cbde4f058; _vwo_uuid_v2=DAFAA56C9C7EDAE380447F88D6B27E40E|c803f7fa217c77f7a701ad99d289b81c; __yadk_uid=IADjl51MmZq2apSWuIC1fLXIOLQOkoSy; ll="118254"; __utmz=30149280.1639653039.17.10.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); push_doumail_num=0; push_noty_num=0; _ga_RXNMP372GL=GS1.1.1642433464.3.1.1642433839.60; __utmv=30149280.25291; _ga=GA1.2.594493052.1621224670; viewed="4913064_35534519_1014278_30358507_30314829_3106534_35651849_23008813_3354490_1964334"; ct=y; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1642763100; __utmc=30149280; __utmz=81379588.1642988222.26.10.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=81379588; _gid=GA1.2.392283503.1642988281; dbcl2="252912989:up8UjoYf/X4"; ck=ssD5; ap_v=0,6.0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=b2459b96-e216-4aec-8cf4-fb8468a15557; gr_cs1_b2459b96-e216-4aec-8cf4-fb8468a15557=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_b2459b96-e216-4aec-8cf4-fb8468a15557=true; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1643008591%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; __utma=30149280.594493052.1621224670.1643005891.1643008591.38; __utmt_douban=1; __utma=81379588.245870019.1628382789.1643005891.1643008591.31; __utmt=1; __utmb=30149280.2.10.1643008591; __utmb=81379588.2.10.1643008591; _pk_id.100001.3ac3=d51cee9c57b59460.1628382788.31.1643008616.1643006314.',
            'Host': 'book.douban.com'
        }
        self._all = None

    def crawl(self, url):
        """
        爬取页面
        :param url: 页面 url
        :return: 返回页面内容
        """
        headers = self._headers
        headers['Referer'] = re.findall(r'https://book.douban.com/subject/\d+/', url)[0]
        resp = requests.get(url, headers=headers, timeout=10)
        content = resp.content.decode(resp.encoding)
        return content

    def parse(self, html):
        """
        解析页面
        :param html: 页面内容
        :return: 返回解析出来的数据
        """
        root = etree.HTML(html)
        if self._all is None:
            readers = root.xpath('//*[@id="content"]/div/div[1]/div/div[1]/ul/li[1]/span//text()')[0].strip()
            self._all = int(re.findall(r'\d+', readers)[0])
            if self._all > 480:
                self._all = 480
        comments = root.xpath('//*[@id="comments"]/div[1]/ul/li')
        _ans = []
        for comment in comments:
            person = comment.xpath('.//span[@class="comment-info"]/a//text()')[0].strip()
            stars = comment.xpath('.//span[@class="comment-info"]/span[1]//@class')[0].strip()
            try:
                star = re.findall(r'\d+', stars)[0]
            except IndexError:
                star = None
            time = comment.xpath('.//span[@class="comment-info"]/span[@class="comment-time"]//text()')[0].strip()
            score = comment.xpath('./div[2]/h3/span[1]/span[@class="vote-count"]//text()')[0].strip()
            com = comment.xpath('./div[2]/p/span')[-1].xpath('string(.)')
            _ans.append([person, star, time, score, com])
        return _ans

    def save(self, data, url):
        """
        保存数据到文件
        :param data: 需要保存的数据
        :param url: 需要单独填写的 页面url
        :return: None
        """
        df = pd.DataFrame(data, columns=['person', 'star', 'time', 'score', 'comment'])
        df['url'] = url
        if os.path.exists(self._outfile):
            df.to_csv(self._outfile, mode='a', index=False, header=False)
        else:
            df.to_csv(self._outfile, mode='a', index=False, header=True)

    def run(self, url, i):
        """
        运行爬虫
        :param url: 爬虫 url
        :param i: 遍历的序号
        :return: 无返回值
        """
        for sort in ['time', 'new_score']:
            start = 0
            while True:
                if self._all and start > self._all:
                    break
                _url = url + f'?start={start}&limit=20&status=P&sort={sort}'
                start += 20
                print(i, sort, start, _url, end=' ')
                try:
                    content = self.crawl(_url)
                    data = self.parse(content)
                    self.save(data, url)
                    time.sleep(3)
                    print(True)
                except requests.exceptions.ReadTimeout as e:
                    print(e)
                except IndexError as e:
                    print(e)
                except Exception as e:
                    return e
        self._all = None


if __name__ == '__main__':
    bc = BookComment()
    # bc.run('https://book.douban.com/subject/35315153/comments/')

    df = pd.read_csv('./bookItem.csv')
    length = len(df.index)
    index = 0  # 阮新伟：0 吴继文：1 刘景瑞：2 李云华：3 陈云涛：4
    # 步长
    step = length // 5
    # 起始 如果出现多次异常，把这个值设置为控制台中最后成功的数字
    # 例如： start = 900
    # start = index * step
    start = 10
    end = (index + 1) * step
    for i in range(start, end):
        tag = df.iloc[i, 0]
        url = df.iloc[i, 1]
        bc.run(url + 'comments/', i)
