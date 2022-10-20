import imp
from honeynbee.common import bee
from honeynbee.common import hive
from honeynbee.common import utils

def run():
    pop, flowercount, gen = utils.takeInput()
    my_hive = hive.Hive(popSize= pop, mapSize= 1000, flowers= flowercount)
    for gen in range(10000):
        my_hive.fitness()
        my_hive.rank()
        if gen == 0:
            print(my_hive)
            print("\n-----------------------------------------------------------------------------------\n")
        my_hive.repopulate()
    my_hive.fitness()
    my_hive.rank()
    print(my_hive)