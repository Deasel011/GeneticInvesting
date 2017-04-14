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
    time.sleep(5)
    print "Net result is: ", dude.get_net_result()

def test_population():
    pop = population.Population('AAL',time.time(),time.time()+10)
    pop.generate()
    assert len(pop.individuals) > 0
    print "Created population without hitch"

def test_fitness():
    print "No Fitness test yet"

def test_grade():
    print "Testing grade of population."
    pop2 = population.Population('AAL',time.time(),time.time()+10)
    pop2.generate()
    time.sleep(10)
    print "Grade score:",fitness.grade(pop2.get_pop())
    for ind in pop2.get_pop():
        print ind.investment.profit,

def test_evolve():
    pop3 = population.Population('AAL',time.time(),time.time()+10)
    pop3.generate()
    time.sleep(10)
    print "Grade score:", fitness.grade(pop3.get_pop())
    pop4 = evolution.breed(pop3.get_pop(),pop3.date_start,pop3.date_end)
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
    test_update()

# test_new_investment()
all()
