import sqlite3
import time

db_route = "/Users/pdesl/PycharmProjects/GeneticInvesting/GI.db"
timeout = 5

# def init():
#     connection = sqlite3.connect(db_route)
#     cursor = connection.cursor()
#     cursor.execute(
#         "CREATE TABLE investment("
#         "id INTEGER PRIMARY KEY,"
#         "title TEXT,"
#         "amountREAL,"
#         "date_start TIMESTAMP,"
#         "confirmation_of_start NUMERIC,"
#         "date_end TIMESTAMP,"
#         "profit REAL,"
#         "confirmation_of_withdrawal NUMERIC,"
#         "FOREIGN KEY (title) REFERENCES title (alias)"
#         ");"
#     )
#     cursor.execute("CREATE TABLE title("
#         "id INTEGER PRIMARY KEY,"
#         "name VARCHAR(50),"
#         "alias TEXT"
#         ")")
#     connection.close()


def populate_titles(titles):
    connection = sqlite3.connect(db_route)
    cursor = connection.cursor()

    for elem in titles:
        params = (elem["title"], elem["name"])
        cursor.execute(
            "INSERT INTO title(alias, name"
            ") VALUES(?, ?)", params)

    connection.commit()
    connection.close()
    return None

def insert(title, date_start, date_end, popid, amount=0, confirmation_of_start=False, confirmation_of_withdrawal=False,
           profit=0):
    params = (title, date_start, date_end, popid, amount,confirmation_of_start, confirmation_of_withdrawal, profit)
    connection = sqlite3.connect(db_route,100)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO investment(title, "
        "date_start, date_end, population_id, amount,"
        "confirmation_of_start, confirmation_of_withdrawal,"
        "profit) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", params)

    id = cursor.lastrowid
    connection.commit()
    connection.close()
    return id

def insertPop(title,date_start,date_end):
    params = (title, date_start, date_end)
    connection = sqlite3.connect(db_route)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO population(title,"
        "date_start, date_end) VALUES (?,?,?)", params)

    id = cursor.lastrowid
    connection.commit()
    connection.close()
    return id


def update(investment, key):
    connection = sqlite3.connect(db_route,100)
    cursor = connection.cursor()
    params = (getattr(investment, key), investment.id)
    query = "UPDATE investment set " + key + " = ? where id = ?"
    cursor.execute(query, params)
    connection.commit()
    connection.close()

def select_uninvested_investments():
    result = {}
    connection = sqlite3.connect(db_route)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM investment where confirmation_of_investment=0 and date_start >= " + time.time())  # todo:assert this works
    for row in cursor:
        id, title, amount, date_start, date_end, confirmation_of_investment, confirmation_of_withdrawal, profit = row
        result[id] = {}
        result[id]["title"] = title
        result[id]["amount"] = amount
        result[id]["date_start"] = date_start
        result[id]["date_end"] = date_end
        result[id]["confirmation_of_investment"] = confirmation_of_investment
        result[id]["confirmation_of_withdrawal"] = confirmation_of_withdrawal
        result[id]["profit"] = profit
    connection.close()
    return result


def select_unwithdrawed_investments():
    result = {}
    connection = sqlite3.connect(db_route)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM investment where confirmation_of_withdrawal=0 and date_end <= " + time.time())  # TODO: assert this works
    for row in cursor:
        id, title, amount, date_start, date_end, confirmation_of_investment, confirmation_of_withdrawal, profit = row
        result[id] = {}
        result[id]["title"] = title
        result[id]["amount"] = amount
        result[id]["date_start"] = date_start
        result[id]["date_end"] = date_end
        result[id]["confirmation_of_investment"] = confirmation_of_investment
        result[id]["confirmation_of_withdrawal"] = confirmation_of_withdrawal
        result[id]["profit"] = profit
    connection.close()
    return result

def dailyArchive():
    None
