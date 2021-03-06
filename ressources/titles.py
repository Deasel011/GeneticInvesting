from urllib2 import URLError
from rtstock.stock import Stock
from yahoo_finance import Share

# titles = {u'SOUL': u'Soul and Vibe Interactive', u'PTOG': u'Petrotech Oil and Gas'}
titles = [
    "AAL",
    "AAPL",
    "ADBE",
    "ADI",
    "ADP",
    "ADSK",
    "AKAM",
    "ALXN",
    "AMAT",
    "AMGN",
    "AMZN",
    "ATVI",
    "AVGO",
    "BIDU",
    "BIIB",
    "BMRN",
    "CA",
    "CELG",
    "CERN",
    "CHKP",
    "CHTR",
    "CTRP",
    "CTAS",
    "CSCO",
    "CTXS",
    "CMCSA",
    "COST",
    "CSX",
    "CTSH",
    "DISCA",
    "DISCK",
    "DISH",
    "DLTR",
    "EA",
    "EBAY",
    "ESRX",
    "EXPE",
    "FAST",
    "FB",
    "FISV",
    "FOX",
    "FOXA",
    "GILD",
    "GOOG",
    "GOOGL",
    "HAS",
    "HSIC",
    "HOLX",
    "ILMN",
    "INCY",
    "INTC",
    "INTU",
    "ISRG",
    "JBHT",
    "JD",
    "KLAC",
    "KHC",
    "LBTYA",
    "LBTYK",
    "LILA",
    "LILAK",
    "LRCX",
    "QVCA",
    "LVNTA",
    "MAR",
    "MAT",
    "MCHP",
    "MDLZ",
    "MNST",
    "MSFT",
    "MU",
    "MXIM",
    "MYL",
    "NCLH",
    "NFLX",
    "NTES",
    "NVDA",
    "ORLY",
    "PAYX",
    "PCAR",
    "PCLN",
    "PYPL",
    "QCOM",
    "REGN",
    "ROST",
    "SBAC",
    "STX",
    "SHPG",
    "SIRI",
    "SWKS",
    "SBUX",
    "SYMC",
    "TMUS",
    "TRIP",
    "TSCO",
    "TSLA",
    "TXN",
    "ULTA",
    "VIAB",
    "VOD",
    "VRSK",
    "VRTX",
    "WBA",
    "WDC",
    "XLNX",
    "XRAY",
    "YHOO"]


def getTitles():
    return titles


def getTitleValue(title):
    stock = Share(title)
    try:
        return float(stock.get_price())
    except TypeError:
        return None

def get_time_of_transaction(title):
    stock = Share(title)
    return stock.get_trade_datetime()

def getTitleInfo(title):
    stock = Stock(title)
    return stock.get_info()
