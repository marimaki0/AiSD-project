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

def Det(p1, p2, p3):
    return p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.y * p3.x - p1.y * p2.x - p3.y * p1.x

def Angle(point0, p):
    return math.atan2(p.y - point0.y, p.x - point0.x)

def Graham(points):
    point0 = min(points, key=lambda p: (p.y, p.x))
    points.remove(point0)

    points.sort(key=lambda p: (Angle(point0, p), point0.distance_between_2points(p)))

    stack = [point0, points[0]]

    for p in points[1:]:
        while len(stack) > 1 and Det(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.split())
            points.append(Point(x, y))
    return points

def GetResult(custom_points):
    result = Graham(custom_points)
    return result

if __name__ == "__main__":
    # Read points from file
    filename = 'test1.txt'
    custom_points = read_points_from_file(filename)

    result = GetResult(custom_points)

    print("Punkty otoczki:")
    for point in result:
        point.print()
