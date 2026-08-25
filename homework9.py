#99:
k = int(input())
n = int(input())

page = (n - 1) // k + 1
line = (n - 1) % k + 1 

print (page, line)

#177:
n = input()
print(len(n) == len(set(n)))

#291:
n = input()
print(n[::-1])

#818:
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        self.coins += v

n = int(input())
box = MoneyBox(n)

m = int(input())
box.add(m)

k = int(input())
print(box.can_add(k))

#820:
import sys

class Buffer: 
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer.extend(a)

        while len(self.buffer) >= 5:
            print(sum(self.buffer[:5]))
            self.buffer = self.buffer[5:]

    def get_current_part(self):
        return self.buffer

buffer = Buffer()

for line in sys.stdin:
    buffer.add(*map(int, line.split()))
    print(buffer.get_current_part())
