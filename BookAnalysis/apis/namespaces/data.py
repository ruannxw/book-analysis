from flask_restx import Namespace, Resource

ns = Namespace('data', description='Ajax Echarts data')

from ...analysis.commentCategories import Analysis as commentCategoriesAnalysis
from ...analysis.dynamicNumberOfPublisher import Analysis as dynamicNumberOfPublisherAnalysis
from ...analysis.everyMonthCommentNum import Analysis as everyMonthCommentNumAnalysis
from ...analysis.everyMonthPublishNum import Analysis as everyMonthPublishNumAnalysis
from ...analysis.proportionOfChineseAndForeignAuthors import Analysis as proportionOfChineseAndForeignAuthorsAnalysis
from ...analysis.top10Authors import Analysis as top10AuthorsAnalysis
from ...analysis.top10BookCategories import Analysis as top10BookCategoriesAnalysis
from ...analysis.top10Publisher import Analysis as top10PublisherAnalysis
from ...analysis.wordCloud import Analysis as wordCloudAnalysis
from ...extensions import redis_client


@ns.route('/commentCategories')
class commentCategories(Resource):
    def get(self):
        """ 情感分析 """
        data = redis_client.get('commentCategories')
        if data:
            return eval(data)
        else:
            data = {
                'errMsg': '',
                'status': True,
                'data': commentCategoriesAnalysis().getData()
            }
            redis_client.set('commentCategories', str(data))
            return data


@ns.route('/dynamicNumberOfPublisher')
class dynamicNumberOfPublisher(Resource):
    def get(self):
        """ 每年作者出版数量动态变化 """
        data = redis_client.get('dynamicNumberOfPublisher')
        if data:
            return eval(data)
        else:
            data = {
                'errMsg': '',
                'status': True,
                'data': dynamicNumberOfPublisherAnalysis().getData()
            }
            redis_client.set('dynamicNumberOfPublisher', str(data))
            return data


@ns.route('/everyMonthCommentNum')
class everyMonthCommentNum(Resource):
    def get(self):
        """ 各月评论数量 """
        data = redis_client.get('everyMonthCommentNum')
        if data:
            return eval(data)
        else:
            data = {
                'errMsg': '',
                'status': True,
                'data': everyMonthCommentNumAnalysis().getData()
            }
            redis_client.set('everyMonthCommentNum', str(data))
            return data


@ns.route('/everyMonthPublishNum')
class everyMonthPublishNum(Resource):
    def get(self):
        """ 各月出版数量 """
        data = redis_client.get('everyMonthPublishNum')
        if data:
            return eval(data)
        else:
            data = {
                'errMsg': '',
                'status': True,
                'data': everyMonthPublishNumAnalysis().getData()
            }
            redis_client.set('everyMonthPublishNum', str(data))
            return data


@ns.route('/proportionOfChineseAndForeignAuthors')
class proportionOfChineseAndForeignAuthors(Resource):
    def get(self):
        """ 中外作者占比 """
        data = redis_client.get('proportionOfChineseAndForeignAuthors')
        if data:
            return eval(data)
        else:
            data = {
                'errMsg': '',
                'status': True,
                'data': proportionOfChineseAndForeignAuthorsAnalysis().getData()
            }
            redis_client.set('proportionOfChineseAndForeignAuthors', str(data))
            return data


@ns.route('/top10Authors')
class top10Authors(Resource):
    def get(self):
        """ Top10 作者出版作品总数 """
        data = redis_client.get('top10Authors')
        if data:
            return eval(data)
        else:
            data = {
                'errMsg': '',
                'status': True,
                'data': top10AuthorsAnalysis().getData()
            }
            redis_client.set('top10Authors', str(data))
            return data


@ns.route('/top10BookCategories')
class top10BookCategories(Resource):
    def get(self):
        """ TOP10 图书分类 """
        data = redis_client.get('top10BookCategories')
        if data:
            return eval(data)
        else:
            data = {
                'errMsg': '',
                'status': True,
                'data': top10BookCategoriesAnalysis().getData()
            }
            redis_client.set('top10BookCategories', str(data))
            return data


@ns.route('/top10Publisher')
class top10Publisher(Resource):
    def get(self):
        """ TOP10 出版社 """
        data = redis_client.get('top10Publisher')
        if data:
            return eval(data)
        else:
            data = {
                'errMsg': '',
                'status': True,
                'data': top10PublisherAnalysis().getData()
            }
            redis_client.set('top10Publisher', str(data))
            return data


@ns.route('/wordCloud')
class wordCloud(Resource):
    def get(self):
        """ 图书评论 """
        data = redis_client.get('wordCloud')
        if data:
            return eval(data)
        else:
            data = {
                'errMsg': '',
                'status': True,
                'data': wordCloudAnalysis().getData()
            }
            redis_client.set('wordCloud', str(data))
            return data
