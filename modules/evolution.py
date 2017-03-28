from random import randint, random
from modules import individual

mutate_chance = 0.01

def breed(parents):
    new_pop = []
    new_pop.append(parents)
    while len(new_pop)<len(parents):
        father = randint(0,len(parents)-1)
        mother = randint(0, len(parents)-1)
        if mother == father:
            mother -= 1
            if mother == -1:
                mother = 2
        child = individual.Individual(parents[father].title,parents[father].min_invest,parents[mother].max_invest,parents[mother].min_delay,parents[father].max_delay)
        new_pop.append(child)

    for i in new_pop:
        if mutate_chance > random():
            i = individual.Individual(parents[0].title, 1,10,1,10)

    return new_pop