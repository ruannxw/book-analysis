import random

from flask_restx import Namespace, Resource

ns = Namespace('data', description='Ajax Echarts data')


@ns.route('/top10BookCategories')
class Top10BookCategories(Resource):
    def get(self):
        """ Top 10 书籍分类 """
        return {
            'errMsg': '',
            'status': True,
            'data': {
                'xAxis': [i for i in range(10)],
                'yAxis': [i + random.randint(0, 1000) for i in range(10)]

            }
        }
