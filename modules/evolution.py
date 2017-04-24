from random import randint, random
from modules import individual, fitness
from ressources import database, config

mutate_chance = 0.01

#todo: update times for tomorow of parents!
#todo: update times for tomorow of date_min and date_max!

def breed_pop(pop):
    pop.indivudials = breed(fitness.get_best_quarter(pop),pop.date_start,pop.date_end,pop.id)
    # None

def breed(parents,date_min,date_max,popid):
    for par in parents:
        par.investment.date_start += 86000
        par.investment.date_withdraw += 86000
        par.investment.confirmation_of_start = False
        par.investment.confirmation_of_withdrawal = False
        par.investment.amount = 0
        par.investment.id = database.insert(par.investment.title,
                        par.investment.date_start,
                        par.investment.date_withdraw,
                        popid,
                        0,
                        False,
                        False,
                        par.investment.profit)

    new_pop = [] + parents
    print len(new_pop)

    while len(new_pop)< config.population_size:
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
                                          mother_max_date_invest,
                                          popid)
            new_pop.append(child)

    print len(new_pop)

    for i in new_pop:
        if mutate_chance > random():
            print "MUTATE"
            start = randint(int(date_min), int(date_max))
            end = randint(start, int(date_max))
            database.remove_ind(i.investment.id)
            i = individual.Individual(parents[0].title, start,end,popid)

    return new_pop
