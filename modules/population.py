import array
from modules import individual

#TODO always sous classer Object
class Population(object):
    individuals = []

    def __init__(self, count, title, minInvest, maxInvest, minDelay, maxDelay):
        for x in xrange(count):
            self.individuals.append(individual.Individual(title,minInvest,maxInvest,minDelay,maxDelay))

    def get_pop(self):
        return self.individuals
