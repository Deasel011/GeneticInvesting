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
        self.amount = titles.getTitleValue(self.title)
        if self.amount != None:
            self.confirmation_start = True

    def sell(self):
        if self.confirmation_start == True:
            self.profit = titles.getTitleValue(self.title) - self.amount
            self.confirmation_withdraw = True


# def buy_stock(title,amount):
#     try:
#         self.amount = titles.getTitleValue(title) * amount
#     except urllib2.URLError:
#         return buy_stock_recursive(title,amount,MAX_DEPTH)
#     return price_of_transaction

def buy_stock_recursive(title,amount,depth):
    print "Trying http call, ", depth, " to go."
    if depth == 0:
        raise Exception("Maximum tries for http call reached.")
    try:
        price_of_transaction = titles.getTitleValue(title) * amount
    except urllib2.URLError:
        depth = depth - 1
        return buy_stock_recursive(title,amount,depth)
    return price_of_transaction

def sellStock():
    gains_of_transaction = None
    return gains_of_transaction

def liquidate_stock(title,amount):
    try:
        gains_of_transaction = titles.getTitleValue(title) * amount
    except urllib2.URLError:
        return liquidate_stock_recursive(title,amount,MAX_DEPTH)
    return gains_of_transaction

def liquidate_stock_recursive(title,amount, depth):
    print "Trying http call, ", depth, " to go."
    if depth == 0:
        raise Exception("Maximum tries for http call reached.")
    try:
        gains_of_transaction = titles.getTitleValue(title) * amount
    except urllib2.URLError:
        depth = depth -1
        return liquidate_stock_recursive(title, amount, depth)
    return gains_of_transaction