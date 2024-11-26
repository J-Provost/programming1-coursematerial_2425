class Averager:
    def __init__(self):
        self._sum = 0
        self._count = 0

    def add(self, value: float):
        self._sum += value
        self._count += 1

    def average(self) -> float:
        if self._count == 0:
            return 0
        return self._sum / self._count

    def reset(self):
        self._sum = 0
        self._count = 0
