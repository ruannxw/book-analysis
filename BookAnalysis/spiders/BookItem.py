import os.path
import time

import pandas as pd
import requests
from lxml import etree


class BookItem:
    """
    根据 tag url 爬取分类下的所有图书
    """

    def __init__(self, outfile=None):
        self._types = ['T', 'R', 'S']
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Cookie': 'bid=FhA-heh1N3I; douban-fav-remind=1; __gads=ID=87af6d311b514533-224652d64fc80038:T=1621224671:RT=1621224671:S=ALNI_MYMfbU3W-gYVpItI97n8_S5KkFAbg; gr_user_id=11ed6298-5be6-4f87-b0a1-832cbde4f058; _vwo_uuid_v2=DAFAA56C9C7EDAE380447F88D6B27E40E|c803f7fa217c77f7a701ad99d289b81c; __yadk_uid=IADjl51MmZq2apSWuIC1fLXIOLQOkoSy; ll="118254"; __utmz=30149280.1639653039.17.10.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); push_doumail_num=0; push_noty_num=0; _ga_RXNMP372GL=GS1.1.1642433464.3.1.1642433839.60; __utmv=30149280.25291; _ga=GA1.2.594493052.1621224670; viewed="4913064_35534519_1014278_30358507_30314829_3106534_35651849_23008813_3354490_1964334"; ct=y; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1642763100; __utmc=30149280; __utmz=81379588.1642988222.26.10.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=81379588; _gid=GA1.2.392283503.1642988281; dbcl2="252912989:up8UjoYf/X4"; ck=ssD5; ap_v=0,6.0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=b2459b96-e216-4aec-8cf4-fb8468a15557; gr_cs1_b2459b96-e216-4aec-8cf4-fb8468a15557=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_b2459b96-e216-4aec-8cf4-fb8468a15557=true; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1643008591%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; __utma=30149280.594493052.1621224670.1643005891.1643008591.38; __utmt_douban=1; __utma=81379588.245870019.1628382789.1643005891.1643008591.31; __utmt=1; __utmb=30149280.2.10.1643008591; __utmb=81379588.2.10.1643008591; _pk_id.100001.3ac3=d51cee9c57b59460.1628382788.31.1643008616.1643006314.',
            'Host': 'book.douban.com'
        }
        if outfile is None:
            outfile = 'bookItem.csv'
        self._outfile = outfile

    def crawl(self, tag, start, type_index):
        resp = requests.get(
            url=f'https://book.douban.com/tag/{tag}?start={start}&type={self._types[type_index]}',
            headers=self._headers,
            timeout=10
        )
        content = resp.content.decode(resp.encoding)
        return content

    def parse(self, html):
        root = etree.HTML(html)
        items = root.xpath('//*[@id="subject_list"]/ul/li[@class="subject-item"]')
        _ans = []
        for item in items:
            url = item.xpath('./div[2]/h2/a//@href')[0].strip()
            _ans.append(url)
        return _ans

    def save(self, tag, data: list):
        df = pd.DataFrame({'category': [tag] * len(data), 'url': data})
        if os.path.exists(self._outfile):
            df.to_csv(self._outfile, mode='a', index=False, header=False)
        else:
            df.to_csv(self._outfile, mode='w', index=False, header=True)

    def run(self, tag):
        stop = 0
        for type_index in range(len(self._types)):
            for start in range(0, 1000, 20):
                print(type_index, start, end='')
                try:
                    html = self.crawl(tag, start, type_index)
                    _ans = self.parse(html)
                    self.save(tag, _ans)
                    stop = 0
                    print(True)
                except requests.exceptions.ReadTimeout as e:
                    print(e)
                except IndexError as e:
                    stop += 1
                    print(e)
                time.sleep(3)
                if stop > 5:
                    stop = 0
                    time.sleep(100)


if __name__ == '__main__':
    # dir_ = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # data_file = os.path.join(dir_, 'data', 'bookItem.csv')
    # bookItem = BookItem(outfile=data_file)
    bookItem = BookItem()
    tags = ['小说', '文学', '外国文学', '经典', '中国文学', '随笔', '日本文学', '散文', '村上春树', '诗歌', '童话', '名著', '儿童文学', '古典文学', '余华', '王小波',
            '当代文学', '杂文', '张爱玲', '外国名著', '鲁迅', '钱钟书', '诗词', '茨威格', '米兰·昆德拉', '杜拉斯', '港台', '漫画', '推理', '绘本', '悬疑',
            '东野圭吾', '青春', '科幻', '言情', '推理小说', '奇幻', '武侠', '日本漫画', '耽美', '科幻小说', '网络小说', '三毛', '韩寒', '亦舒', '阿加莎·克里斯蒂',
            '金庸', '穿越', '安妮宝贝', '魔幻', '轻小说', '郭敬明', '青春文学', '几米', 'J.K.罗琳', '幾米', '张小娴', '校园', '古龙', '高木直子', '沧月',
            '余秋雨', '张悦然', '历史', '心理学', '哲学', '社会学', '传记', '文化', '艺术', '社会', '政治', '设计', '政治学', '宗教', '建筑', '电影', '中国历史',
            '数学', '回忆录', '思想', '人物传记', '艺术史', '国学', '人文', '音乐', '绘画', '西方哲学', '戏剧', '近代史', '二战', '军事', '佛教', '考古',
            '自由主义', '美术', '爱情', '成长', '生活', '心理', '女性', '旅行', '励志', '教育', '摄影', '职场', '美食', '游记', '灵修', '健康', '情感',
            '人际关系', '两性', '养生', '手工', '家居', '自助游', '经济学', '管理', '经济', '商业', '金融', '投资', '营销', '理财', '创业', '股票', '广告',
            '企业史', '策划', '科普', '互联网', '科学', '编程', '交互设计', '算法', '用户体验', '科技', 'web', '交互', '通信', 'UE', '神经网络', 'UCD',
            '程序']
    for tag in tags:
        bookItem.run(tag=tag)
