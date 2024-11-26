class Unit:
    def __init__(self, health: float, firepower: float, armor: float):
        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError("Health, firepower, and armor must be non-negative.")
        self._health = health
        self._firepower = firepower
        self._armor = armor

    @property
    def health(self):
        return self._health

    @property
    def firepower(self):
        return self._firepower

    @property
    def armor(self):
        return self._armor

    def shot_by(self, other):
        damage = max(0, other.firepower - self._armor)
        self._health = max(0, self._health - damage)

