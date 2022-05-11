# -*- coding:utf-8 -*-
# Some code from https://saladtomatonion.com/blog/2014/12/16/mesurer-le-temps-dexecution-de-code-en-python/
import time


class Timer(object):
    def __init__(self):
        self.start_time = None
        self.interval = None

    def start(self):
        if hasattr(self, 'interval'):
            del self.interval
        self.start_time = time.time()

    def get_current_time(self):
        self.interval = time.time() - self.start_time
        return self.interval
