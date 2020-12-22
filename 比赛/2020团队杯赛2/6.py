class BlackBox:

    def __init__(self, n: int, m: int):
        self.m = m
        self.n = n
        self.isopen = [False] * 2 * (self.m + self.n)
        self.map = {}
        pass

    def findx(self, index: int, direction: int):
        print(index)
        if direction == 2 or direction == -2:
            direction =direction /2
        else:
            if self.isopen[index]:
                return index, direction

        if index * direction in self.map:
            if self.map[index * direction] == [index * direction]:
                del self.map[index * direction]
            else:
                if self.map[index * direction] > 0:
                    return self.map[index * direction], 1
                else:
                    return -self.map[index * direction], 1
        if direction == 1:
            temp, direction = self.findx(2 * (self.m + self.n) - index, -1)
            self.map[index * direction] = temp * direction
        else:
            index = 2 * (self.m + self.n) - index
            if index > 2 * self.m + self.n:
                index = 2 * self.m + self.n - index
            else:
                index = 2 * (self.m + self.n) - index + 2 * self.m + self.n
            temp, direction = self.findx(index, 1)
            self.map[index * direction] = temp * direction
        return temp, direction

    def open(self, index: int, direction: int):
        a, b = index, direction
        self.isopen[index] = True
        index, direction = self.findx(index, direction * 2)
        while not self.isopen[index]:
            index, direction = self.findx(index, direction)
        index, direction = a, b
        while not self.isopen[index]:
            index, direction = self.findx(index, direction * -1)
        self.map[index * direction * -1] = a * b

        return index

    def close(self, index: int) -> None:
        self.isopen[index] = False


obj = BlackBox(3, 3)
print(obj.open(1, -1))
print(obj.open(5, 1))
print(obj.open(11, -1))
print(obj.open(11, 1))
obj.close(1)
print(obj.open(11, 1))
obj.close(5)
print(obj.open(11, -1))
