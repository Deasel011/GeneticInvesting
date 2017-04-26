from modules import population
from modules import individual
from modules import fitness, evolution, investment
from ressources import database
import time
import datetime
import sched

def checkTransaction(pop):
    for ind in pop.individuals:
        if time.time() >= ind.investment.date_start and not ind.investment.confirmation_of_start:
            print "Time to buy", datetime.datetime.fromtimestamp(int(ind.investment.date_start)).strftime('%Y-%m-%d %H:%M:%S')
            ind.investment.buy()
        if time.time() >= ind.investment.date_withdraw and not ind.investment.confirmation_of_withdrawal:
            print "Time to sell", datetime.datetime.fromtimestamp(int(ind.investment.date_withdraw)).strftime('%Y-%m-%d %H:%M:%S')
            ind.investment.sell()


def initPopulation(title,start,end):
    pop = population.Population(title, start, end)
    pop.generate()
    return pop

def end_of_day_tasks(populations):
    database.daily_archive()
    for pop in populations:
        database.renew_population(pop.id)
        pop.date_start = pop.date_start + 86000
        pop.update_date_start()
        pop.date_end = pop.date_end + 86000
        pop.update_date_end()
        pop = evolution.breed_pop(pop)


def run():
    print "Loading populations"
    all_populations = population.load_all_populations()
    print "Populations loaded"
    while(True):
        if time.time() % 86400 > 72000: # 16h
        # if time.time() % 86400 > 67200: #14h40
        # if time.time() % 86400 > 61200:  # 13h00
        # if time.time() % 86400 > 58800:  # 14h40
            print "END OF DAY",int(time.time())
            end_of_day_tasks(all_populations)
            print "Daily run over"
            break
        else:
            try:
                print "Checking Transactions..."
                time.sleep(1)
                for pop in all_populations:
                    checkTransaction(pop)
            except Exception:
                print Exception.message

    tomorow = sched.scheduler(time.time,time.sleep)
    tomorow.enter(63000,1,run,())
    tomorow.run()
