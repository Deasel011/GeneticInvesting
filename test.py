from modules import population
from modules import individual
from modules import fitness, evolution, investment
from pytz import timezone, utc
from ressources import database
import time
import datetime

def test_individual():
    now = datetime.datetime.now(utc)
    dude = individual.Individual('AAL',time.mktime(now.timetuple())
                                 ,time.mktime((now+datetime.timedelta(0,5)).timetuple()
                                              )
                                 )
    print "Called successfully, awaiting Liquidating call."
    print "Liquidating call should be received."
    print "Net result is: ", dude.get_net_result()

def test_population():
    pop = population.Population('AAL',time.time(),time.time()+10)
    print "Called successfully, awaiting 10 Liquidating calls."
    print "All Liquidating calls should be received."

def test_fitness():
    print "No Fitness test yet"

def test_grade():
    print "Testing grade of population."
    pop2 = population.Population('AAL',time.time(),time.time()+10)
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
    invest = investment.Investment("AAL",time.time(),(time.time()+5000))
    print "id of new investment:",invest.id

def test_update():
    invest = investment.Investment("AAL",time.time(),(time.time()+5000))
    invest.get_title_value = mock_up_title_value
    invest.buy()
    invest.get_title_value = mock_up_title_value2
    invest.sell()

def init_db():
    database.init()
    database.populate_titles([{u"name", u""}])

def mock_up_title_value():
    return 10

def mock_up_title_value2():
    return 33

def all():
    test_individual()
    test_population()
    test_fitness()
    test_grade()
    test_evolve()

# test_new_investment()
test_update()
