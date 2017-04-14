import urllib2
from ressources import database

from ressources import titles
MAX_DEPTH = 3

class Investment:
    def __init__(self, title, date_start, date_end):
        self.amount = None
        self.profit = None
        self.date_start = date_start
        self.date_withdraw = date_end
        self.confirmation_start = False
        self.confirmation_withdraw = False
        self.title = title
        self.id = database.insert(title,date_start,date_end)

    def buy(self):
        self.amount = self.get_title_value()

        if self.amount != None:
            self.confirmation_start = True
            self.update_amount("amount")

    def get_title_value(self):
        return titles.getTitleValue(self.title)

    def sell(self):
        if self.confirmation_start == True:
            self.profit = self.get_title_value() - self.amount
            self.confirmation_withdraw = True
            self.update_amount("profit")
            return self.profit
        return None

    def update_amount(self, key):
        database.update(self, key)
