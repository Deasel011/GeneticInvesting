from random import randint
from modules import investment
import sched,time, datetime
from datetime import timedelta
from threading import Timer
from pytz import utc

class Individual(object):
    """Representation of one investment"""
    netGains = None #None will give instanciated variable

    def __init__(self, title, date_start,date_end):
        self.title = title
        self.delay = date_end - date_start
        self.investment = investment.Investment(title,date_start,date_end)
        # start timer with delay
        # when timer is done
        # startTimer(delay):
        #   self.netGains=price - investment.liquidateStock(title,self.amount)
        Timer(date_start - time.time(), self.invest).start()#todo:thread to start investing at good time.

    @classmethod
    def random(cls, date_min, date_max):
        start_delay = randint(0,max_start_range)
        end_delay = randint(0,max_end_delay)
        date_start = date + start_delay
        date_end = date_start + end_delay
        return cls(title,date_start,date_end)

    @classmethod
    def defined(cls, title, date_start,end_delay):
        date_end = date_start + end_delay
        return cls(title, date_start, date_end)

    def invest(self):
        self.investment.buy()
        Timer(self.delay, self.gains).start()

    def get_net_result(self):
        return self.netGains

    def gains(self):
        self.netGains = self.investment.sell()
