from modules import fitness, population, evolution
from ressources import database
import time

def checkTransaction(pop):
    for ind in pop.individuals:
        if time.time() >= ind.investment.date_start and not ind.investment.confirmation_start:
            ind.investment.buy()
        if time.time() >= ind.investment.date_end and not ind.investment.confirmation_withdraw:
            ind.investment.sell()


def initPopulation(title,start,end):
    return population.Population(title,start,end)

allPopulations = database.loadActivePopulations()

while(True):
    time.sleep(1)
    for pop in allPopulations:
        checkTransaction(pop)