import array
from modules import individual
from ressources import database
import random

#TODO always sous classer Object
class Population(object):

    def __init__(self,title,date_start,date_end):
        self.individuals = [] #Instance property
        self.title=title
        self.date_start = date_start
        self.date_end=date_end
        self.id = database.insertPop(title,date_start,date_end)


    def generate(self):
        for x in xrange(100):
            start = random.randint(int(self.date_start), int(self.date_end))
            end = random.randint(start,int(self.date_end))
            indiv = individual.Individual(self.title,start,end)
            self.individuals.append(indiv)


    def load_from_db(self):
        self.individuals = database.getPopulation()

    def get_pop(self):
        return self.individuals
