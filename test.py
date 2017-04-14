from modules import population
from modules import individual
from modules import fitness, evolution, investment
from pytz import timezone, utc
from ressources import database
import time
import datetime

def test_individual():
    now = datetime.datetime.now(utc)
    dude = individual.Individual('AAL',time.time()
                                 ,time.time()+5
                                 )
    assert dude != None
    print "Created Individual successfully"
    wait(6,False)
    print "Profit: ", dude.investment.profit

def test_population():
    pop = population.Population('AAL',time.time(),time.time()+10)
    pop.generate()
    assert len(pop.individuals) > 0
    print "Created population without hitch"
    wait(10,False)
    print "We assume everythin' went just right..."

def test_fitness():
    print "No Fitness test yet"

def test_grade():
    print "Testing grade of population."
    pop2 = population.Population('AAL',time.time(),time.time()+10)
    pop2.generate()
    time.sleep(11)
    print "Grade score:",fitness.grade(pop2.get_pop())

def test_evolve():
    print "Testing evolution of a population"
    pop3 = population.Population('AAL',time.time(),time.time()+10)
    pop3.generate()
    time.sleep(11)
    print "Grade score:", fitness.grade(pop3.get_pop())
    pop4 = evolution.breed(pop3.get_pop(),pop3.date_start,pop3.date_end)
    time.sleep(11)
    print "Grade score:", fitness.grade(pop4)

def test_new_investment():
    invest = investment.Investment("AAL",time.time(),(time.time()+5))
    print "id of new investment:",invest.id

def test_update():
    invest = investment.Investment("AAL",time.time(),(time.time()+5))
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

def wait(seconds,quiet=True):
    for x in range(1,seconds+1):
        time.sleep(1)
        if not quiet:
            print x, "seconds elapsed"

def all():
    test_individual()
    test_population()
    test_fitness()
    test_grade()
    test_evolve()
    test_update()


# test_new_investment()
test_grade()