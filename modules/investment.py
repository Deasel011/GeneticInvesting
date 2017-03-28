import urllib2
from ressources import database

from ressources import titles
MAX_DEPTH = 3

class Investment:
    def __init__(self, title, amount, date_start, date_end):
        self.amount = None
        self.profit = None
        self.date_start = None
        self.date_withdraw = None
        self.confirmation_start = False
        self.confirmation_withdraw = False
        self.title = title
        self.id = database.insert(title,amount,date_start,date_end)


def buy_stock(title,amount):
    try:
        price_of_transaction = titles.getTitleValue(title) * amount
    except urllib2.URLError:
        return buy_stock_recursive(title,amount,MAX_DEPTH)
    return price_of_transaction

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

def coverStock():
    return None

def shortStock():
    return None