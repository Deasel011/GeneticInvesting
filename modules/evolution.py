from random import randint, random
from modules import individual

mutate_chance = 0.01

def breed(parents,date_min,date_max):
    new_pop = []
    new_pop.append(parents)
    while len(new_pop)<len(parents):
        father = randint(0,len(parents)-1)
        mother = randint(0, len(parents)-1)
        if mother == father:
            mother -= 1
            if mother == -1:
                mother = 1
        child = individual.Individual(parents[father].title,parents[father].min_invest,parents[mother].max_invest,parents[mother].min_delay,parents[father].max_delay)
        new_pop.append(child)

    for i in new_pop:
        if mutate_chance > random():
            start = random.randint(int(date_min), int(date_max))
            end = random.randint(start, int(date_max))
            i = individual.Individual(parents[0].title, start,end)

    return new_pop