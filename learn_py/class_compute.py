class Point:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __repr__(self):
        return '<Point x:{0} y:{1}>'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __ge__(self, other):
        return self.x <= other.x and self.y <= other.y

p1 = Point(10, 20)
p2 = Point(5, 10)
print 'p1',p1
print 'p2',p2
print p1 + p2
print p1 - p2
p1 += p2
print p1

print p2 >= p1

