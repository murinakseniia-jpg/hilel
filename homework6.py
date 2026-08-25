class CandyStash:
    MAX_CAPACITY = 50

    def __init__(self, count):
        self.count = count


    @staticmethod
    def validate_amount(value):
        if not isinstance(value, int):
            raise ValueError
        if value < 0:
            raise ValueError

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self.validate_amount(value)
        self._count = min(value, self.MAX_CAPACITY)

    def __str__(self):
        return f"CandyStash ({self.count}/{self.MAX_CAPACITY})"

    def __repr__(self):
        return str(self)

    def __add__(self, value):
        return CandyStash(self.count + value)

    def __sub__(self, value):
        return CandyStash(max(0, self.count - value))

    def __eq__(self, other):
        if isinstance(other, CandyStash):
            return self.count == other.count
    
        if isinstance(other, int):
            return self.count == other
        
        return NotImplemented

stash = CandyStash(12)

