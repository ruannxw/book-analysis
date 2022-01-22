import os

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix


def register_extensions(app: Flask):
    pass


def register_blueprints(app: Flask):
    """
    注册蓝图
    :param app: Flask app
    :return: 无返回值

    example:
    # 注册 bp 蓝图
    # app.register_blueprint(bp)

    # 注册 apis 蓝图
    # from .apis import apis
    # app.register_blueprint(apis)
    """

    from .views.index import index_bp
    app.register_blueprint(index_bp)
    from .apis import apis
    app.register_blueprint(apis)


def register_commands(app: Flask):
    """
    注册命令行
    :param app: Flask app
    :return: 无返回值

    example:
    @app.cli.command()
    @click.option('--params', default=10, help='The default parameter is 10')
    def init(params:int):
        click.echo(params)
        click.echo('success')
    """
    pass


def register_shell_context(app: Flask):
    """
    注册 flask shell 上下文
    :param app: Flask app
    :return: 无返回值

    example:
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User)
    """

    pass


def register_errors(app: Flask):
    """
    自定义错误处理
    :param app: Flask app
    :return: 无返回值

    example:
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400
    """
    pass


def create_app(config_name=None):
    """
    根据配置，生成 wsgi app
    :param config_name: 配置名称
    :return: 返回 wsgi app
    """
    # 默认配置为开发环境
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')

    # 配置 logging
    # if not os.path.exists(os.path.join(get_main_dir(), 'logs')):
    #     os.makedirs(os.path.join(get_main_dir(), 'logs'))
    #
    # with open(os.path.join(get_main_dir(), 'configs', 'logConfig.yml'), mode='r') as f:
    #     dictConfig(dict(yaml.load(f.read(), Loader=Loader)))

    # 初始化 Flask app
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_port=1, x_proto=1, x_prefix=1)
    # 导入配置
    from .settings import Config
    app.config.from_object(Config.getConfig(config_name))

    # 注册扩展、蓝本、命令等
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_shell_context(app)
    register_errors(app)

    return app
