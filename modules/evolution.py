from random import randint, random
from modules import individual

mutate_chance = 0.01

#todo: update times for tomorow of parents!
#todo: update times for tomorow of date_min and date_max!

def breedPop(pop):
    pop.indivudials = breed(pop.get_pop(),pop.date_start,pop.date_end)


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

        father_title = parents[father].title
        father_min_date_invest = parents[father].investment.date_start
        mother_max_date_invest = parents[mother].investment.date_withdraw

        if father_min_date_invest < mother_max_date_invest:
            child = individual.Individual(father_title,
                                          father_min_date_invest,
                                          mother_max_date_invest)
            new_pop.append(child)

    for i in new_pop:
        if mutate_chance > random():
            start = random.randint(int(date_min), int(date_max))
            end = random.randint(start, int(date_max))
            i = individual.Individual(parents[0].title, start,end)

    return new_pop
