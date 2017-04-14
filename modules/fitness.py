import sched,time

s = sched.scheduler(time.time, time.sleep)

class Fitness:
    def __init__(self, individual):
        self.result = individual.get_net_result()
        self.individual = individual
        count = 3
        while self.result is None and count > 0:
            count -= 1
            time.sleep(3)
            self.check_fitness()

    def check_fitness(self):
        self.result == self.individual.get_net_result()
        if self.result == None:
            self.result = 0

    def get_fitness(self):
        return self.result

def grade(population):
    sum = 0
    for individual in population:
        fitness_of_individual = Fitness(individual)
        sum = sum + fitness_of_individual.get_fitness()

    return sum / len(population)

def get_best_quarter(population):
    sortedPop = sorted(population.get_pop(), key=lambda individual:individual.get_net_result())
    size = len(sortedPop)
    cutoff = sortedPop[0:(size/4)]
    return cutoff