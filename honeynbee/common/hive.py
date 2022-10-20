from operator import index
from honeynbee.common import bee
import random

class   Hive:

    def __init__(self, popSize = 100, mapSize = 1000, flowers = 100) -> None:
        self.crossoverRate = int(popSize * 0.50)
        self._pos = (500, 500)
        self._mapSize = mapSize
        self._popSize = popSize
        self._flowersCount = flowers
        self._flowers = self.createField(flowers)
        self.bees = [bee.Bee(x, self._flowers) for x in range(popSize)]

    def createField(self, flowersCount):
        flowers = []
        for x in range(flowersCount):
            coord = (random.randint(0, self._mapSize - 1), random.randint(0, self._mapSize - 1))
            if coord != (500, 500):
                try: 
                    flowers.index(coord)
                except ValueError:
                    flowers.append(coord)
                    continue
                x -= 1
            x -= 1
        return flowers

    def fitness(self):
        x, y = self._pos
        for abee in self.bees:
            moves = 0
            for flower in abee._chz:
                nx, ny = flower
                moves += abs(x - nx) + abs(y - ny)
                x , y = nx, ny
            abee.score = moves

    def rank(self):
        self.bees.sort(key=lambda abee: abee.score)
        for x, abee in enumerate(self.bees):
            abee._rank = x + 1

    def killerBee(self):
        idList = []
        for i in range(self._popSize - 1, self._popSize - self.crossoverRate - 1, -1):
            idList.append(self.bees[i]._id)
            self.bees.pop(i)
        return idList

    def crossover(self, bestBee, otherBee, idList, childs):
        c1 = bee.Bee(random.choice(idList), self._flowers, True)
        idList.remove(c1._id)
        c2 = bee.Bee(random.choice(idList), self._flowers, True)
        idList.remove(c2._id)
        for gene in range(self._flowersCount):
            n = random.randrange(0, 100)
            if n >= 50:
                if bestBee._chz[gene] in c1._chz or otherBee._chz[gene] in c2._chz:
                    c1._chz.append(otherBee._chz[gene])
                    c2._chz.append(bestBee._chz[gene])
                else:
                    c1._chz.append(bestBee._chz[gene])
                    c2._chz.append(otherBee._chz[gene])
            else:
                if bestBee._chz[gene] in c2._chz or otherBee._chz[gene] in c1._chz:
                    c1._chz.append(bestBee._chz[gene])
                    c2._chz.append(otherBee._chz[gene])
                else:
                    c1._chz.append(otherBee._chz[gene])
                    c2._chz.append(bestBee._chz[gene])
        childs.append(c1)
        childs.append(c2)

    def mutate(self, childList):
        for abee in childList:
            n = random.randrange(0, 100)
            if n >= 90:
                g1 = random.choice(abee._chz)
                g2 = g1
                while g2 == g1:
                    g2 = random.choice(abee._chz)
                g1, g2 = g2, g1
            else:
                continue

    def repopulate(self):
        y = int(self.crossoverRate / 2)
        idList = self.killerBee()
        childs = []
        for x in range(y):
            if self.bees[x].score > self.bees[y + x].score:
                self.crossover(self.bees[x], self.bees[y + x], idList, childs)
            else:
                self.crossover(self.bees[y + x], self.bees[x], idList, childs)
        self.mutate(childs)
        self.bees += childs

    
    def __str__(self) -> str:
        return "\n\n".join(abee.__str__() for abee in self.bees)