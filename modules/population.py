import array
from modules import individual
from ressources import database, config
import random
import sqlite3


# TODO always sous classer Object
class Population(object):
    def __init__(self, title, date_start, date_end,into_db = True):
        self.individuals = []  # Instance property
        self.title = title
        self.date_start = date_start
        self.date_end = date_end
        if into_db:
            self.id = database.insertPop(title, date_start, date_end)

    def generate(self):
        for x in xrange(config.population_size):
            start = random.randint(int(self.date_start), int(self.date_end))
            end = random.randint(start, int(self.date_end))
            indiv = individual.Individual(self.title, start, end, self.id)
            self.individuals.append(indiv)

    def load_from_db(self):
        self.individuals = database.getPopulation()

    def get_pop(self):
        return self.individuals

    def update_date_start(self):
        database.update_pop(self,"date_start")

    def update_date_end(self):
        database.update_pop(self,"date_end")


def load_all_populations():
    pops = []
    connection = sqlite3.connect(database.db_route)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM population")
    for row in cursor:
        id, title, date_start, date_end = row
        pop = Population(title, date_start, date_end,False)
        pop.id = id
        print "loaded pop", pop.id
        pops.append(pop)

    for pop in pops:
        cursor.execute("SELECT * FROM investment WHERE population_id = ?", (pop.id,))
        print "loading pop", pop.id,
        for row in cursor:
            id, title, amount, date_start, confirmation_of_start, date_end, profit, confirmation_of_withdrawal, population_id = row
            ind = individual.Individual(title, date_start, date_end, population_id,False)
            ind.investment.id = id
            ind.investment.confirmation_of_start = (confirmation_of_start == 1)
            ind.investment.confirmation_of_withdrawal = (confirmation_of_withdrawal == 1)
            ind.investment.amount = amount
            print ".",
            pop.individuals.append(ind)


        print ""
    connection.commit()
    connection.close()
    return pops
