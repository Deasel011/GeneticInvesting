from modules import population
from modules import individual
from modules import fitness, evolution, investment
from ressources import database
import time

def test_individual():
    dude = individual.Individual('AAL',3,6,3,10)
    print "Called successfully, awaiting Liquidating call."
    time.sleep(10)
    print "Liquidating call should be received."
    print "Net result is: ", dude.get_net_result()

def test_population():
    pop = population.Population(10,'AAL',3,6,3,10)
    print "Called successfully, awaiting 10 Liquidating calls."
    time.sleep(10)
    print "All Liquidating calls should be received."

def test_fitness():
    print "No Fitness test yet"

def test_grade():
    print "Testing grade of population."
    pop2 = population.Population(10, 'AAL', 3, 6, 3, 10)
    time.sleep(10)
    print "Grade score:",fitness.grade(pop2.get_pop())
    for ind in pop2.get_pop():
        print ind.getNetResult(),

def test_evolve():
    pop3 = population.Population(10, 'AAL', 3, 6, 3, 10)
    time.sleep(10)
    print "Grade score:", fitness.grade(pop3.get_pop())
    pop4 = evolution.breed(pop3.get_pop())
    time.sleep(10)
    print "Grade score:", fitness.grade(pop4)

def test_new_investment():
    invest = investment.Investment("AAL",1,time.time(),(time.time()+5000))
    print "id of new investment:",invest.id

def init_db():
    database.init()
    database.populate_titles([{u"name", u""}])

def all():
    test_individual()
    test_population()
    test_fitness()
    test_grade()
    test_evolve()

test_new_investment()