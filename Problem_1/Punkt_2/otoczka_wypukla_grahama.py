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
    
    def __repr__(self):
        return f"\n(x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"

def Det(p1,p2,p3):
    return p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.y * p3.x - p1.y * p2.x - p3.y * p1.x

def Angle(point0, p):
    return math.atan2(p.y - point0.y, p.x - point0.x)

def Graham(points):
    point0=min(points, key=lambda p:(p.y, p.x))
    points.remove(point0)

    points.sort(key=lambda p: (Angle(point0, p), point0.distance_between_2points(p)))

    stack=[point0, points[0]]

    for p in points[1:]:
        while len(stack)>1 and Det(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

def GeneratePoints(number, min_bound, max_bound):
    
    points = []
    for _ in range(number):
        x = random.randint(min_bound, max_bound)
        y = random.randint(min_bound, max_bound)
        points.append(Point(x, y))

    for i in points:
        print(i)
    return points


def GetResult():
    points = GeneratePoints(0, -100, 100)
    
    if len(points) == 0:
        print("Nie ma punktow")
        return []
    
    result = Graham(points)

   # print("Punkty otoczki:")
   # for point in result:
   #     point.print()

    return Graham(points)


if __name__ == "__main__":
    result = GetResult()

    if len(result)!=0:
        print("Punkty otoczki:")
        for point in result:
            point.print()




