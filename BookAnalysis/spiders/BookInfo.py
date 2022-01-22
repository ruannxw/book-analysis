import requests
from lxml import etree


class BookInfo:
    def __init__(self):
        self._url = 'https://book.douban.com/subject/35534519/'
        self._method = 'GET'
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }

    def crawl(self):
        resp = requests.request(method=self._method, url=self._url, headers=self._headers)
        content = resp.content.decode(resp.encoding)
        return content

    def parse(self, content):
        # 这里注意要按照 列表顺序来
        _ans = []
        root = etree.HTML(content)
        info = root.xpath('//*[@id="info"]')[0]
        spans = info.xpath('./span[@class="pl"]')
        for span in spans:
            print(span.xpath('string(.)'), span.tail.strip())
            if span.xpath('string(.)') == '出版社:':
                _ans.append(span.tail.strip())
        print(_ans)

    def run(self):
        content = self.crawl()
        self.parse(content)

        # //*[@id="info"]


if __name__ == '__main__':
    bookInfo = BookInfo()
    bookInfo.run()

    for start in range(0, 500, 20):
        url = 'https://book.douban.com/subject/35534519/comments/?start=%s&limit=20&status=P&sort=new_score' % start
