from random import randint
from modules import investment
import sched,time, threading

class Individual(object):
    """Representation of one investment"""
    netGains = None #None will give instanciated variable

    def __init__(self, title, date_start,date_end):
        self.title = title
        self.investment = investment.Investment(title,self.price,date_start,date_end)
        # start timer with delay
        # when timer is done
        # startTimer(delay):
        #   self.netGains=price - investment.liquidateStock(title,self.amount)
        threading.Timer(date_start - time.time(), self.invest).start()#todo:thread to start investing at good time.

    @classmethod
    def random(cls, title, date,max_start_range,max_end_delay):
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
        threading.Timer(self.delay, self.gains).start()

    def get_net_result(self):
        return self.netGains

    def get_amount(self):
        return self.amount

    def get_min_delay(self):
        return self.min_delay

    def gains(self):
        self.netGains = self.price - investment.liquidate_stock(self.title, self.amount)
