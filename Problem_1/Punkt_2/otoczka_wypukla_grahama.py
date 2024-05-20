import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print("point" + "(x" + ":" , self.x, " , y" + ":", self.y, ")")

    def distance_between_2points(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

def det(p1,p2,p3):
    return p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.y * p3.x - p1.y * p2.x - p3.y * p1.x

def angle(point0, p):
    return math.atan2(p.y - point0.y, p.x - point0.x)

def graham(points):
    point0=min(points, key=lambda p:(p.y, p.x))
    points.remove(point0)

    points.sort(key=lambda p: (angle(point0, p), point0.distance_between_2points(p)))

    stack=[point0, points[0]]

    for p in points[1:]:
        while len(stack)>1 and det(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

def generate_points(number, x_min, x_max, y_min, y_max):
    points = []
    for _ in range(number):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        points.append(Point(x, y))
    return points

if __name__ == "__main__":
    points=generate_points(10, 0, 10, 0, 10)
    for point in points:
        point.print()

    print("***********")
    result=graham(points)

    for point in result:
        point.print()
   


