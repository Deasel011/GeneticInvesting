from random import randint
from modules import investment
import sched,time, datetime
from datetime import timedelta
from threading import Timer
from pytz import utc

class Individual(object):
    """Representation of one investment"""
    netGains = None #None will give instanciated variable

    def __init__(self, title, date_start,date_end,popid,into_db=True):
        self.title = title
        self.delay = int(date_end - date_start)
        self.investment = investment.Investment(title,date_start,date_end,popid,into_db)
        # start timer with delay
        # when timer is done
        # startTimer(delay):
        #   self.netGains=price - investment.liquidateStock(title,self.amount)

        # delay = date_start - time.time()
        # Timer(delay, self.invest).start()#todo:thread to start investing at good time.

    def invest(self):
        self.investment.buy()
        # Timer(self.delay, self.gains).start()

    def get_net_result(self):
        return self.investment.profit

    def gains(self):
        self.netGains = self.investment.sell()
