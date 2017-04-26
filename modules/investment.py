import urllib2
from ressources import database

from ressources import titles
MAX_DEPTH = 3

class Investment:
    def __init__(self, title, date_start, date_end,popid,into_db):
        self.amount = None
        self.profit = None
        self.date_start = date_start
        self.date_withdraw = date_end
        self.confirmation_of_start = False
        self.confirmation_of_withdrawal = False
        self.title = title
        if into_db:
            self.id = database.insert(title,date_start,date_end,popid)

    def buy(self):
        try:
            self.amount = self.get_title_value()
            print "Buying", self.title, "at", self.amount
        except urllib2.URLError:
            print "Could not retrieve price"

        if self.amount != None:
            self.confirmation_of_start = True
            database.set_confirmation_start_true(self.id)
            self.update_amount("amount")

    def get_title_value(self):
        return titles.getTitleValue(self.title)

    def sell(self):
        if self.confirmation_of_start == True:
            try:
                val = self.get_title_value()
                if val == None:
                    print "Value not set, passing"
                    return None
                self.profit = self.get_title_value() - self.amount
                print "Selling", self.title, "with profit of", self.profit
                self.confirmation_of_withdrawal = True
                database.set_confirmation_withdrawal_true(self.id)
                self.update_amount("profit")
                return self.profit
            except urllib2.URLError:
                print "Could not retrieve price"
        return None

    def update_amount(self, key):
        database.update(self, key)
