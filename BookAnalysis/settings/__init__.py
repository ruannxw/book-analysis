import os
import sys

from dotenv import load_dotenv, find_dotenv

# from . import DevelopmentConfig, ProductionConfig, TestConfig

basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

load_dotenv(find_dotenv())
# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

from . import DevelopmentConfig, ProductionConfig, TestConfig


class Config:
    _config = {
        'development': DevelopmentConfig.DevelopmentConfig,
        'testing': TestConfig.TestConfig,
        'production': ProductionConfig.ProductionConfig
    }
    DevelopmentConfig = DevelopmentConfig.DevelopmentConfig
    TestConfig = TestConfig.TestConfig
    ProductionConfig = ProductionConfig.ProductionConfig

    @classmethod
    def getConfig(cls, config=None):
        if config is None:
            config = 'development'
        return cls()._config[config]
