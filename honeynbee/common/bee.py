import random

class   Bee:

    def __init__(self, id, flowerList, empty = False) -> None:
        self.score = 0
        if not empty:
            self._chz = flowerList.copy()
            random.shuffle(self._chz)
        else:
            self._chz = []
        self._id = id
        self._rank = 0

    def __eq__(self, __o: object) -> bool:
        return self._score == __o.score
    
    def __lt__(self, __o: object) -> bool:
        return self._score < __o.score
    
    def __gt__(self, __o: object) -> bool:
        return self.score > __o.score

    def __str__(self) -> str:
        return f"=== Bee n°{self._id} ===\nscore : {self.score}\nrank : {self._rank}\nchromosome :\n{self._chz}"