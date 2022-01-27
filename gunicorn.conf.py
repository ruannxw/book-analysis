import multiprocessing

bind = '0.0.0.0:5000'
# workers = multiprocessing.cpu_count() * 2
workers = 1
preload_app = True
worker_class = 'gevent'
