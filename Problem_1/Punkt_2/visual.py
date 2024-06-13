import math
import random
import matplotlib.pyplot as plt

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
    return points

def plot_convex_hull(points, hull):
    x_points = [p.x for p in points]
    y_points = [p.y for p in points]
    
    hull_x = [p.x for p in hull] + [hull[0].x]
    hull_y = [p.y for p in hull] + [hull[0].y]
    
    plt.scatter(x_points, y_points, color='blue')
    plt.plot(hull_x, hull_y, color='red')
    plt.fill(hull_x, hull_y, color='yellow', alpha=0.3)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Otoczka wypukla')
    plt.grid(True)
    plt.show()

def GetResult():
    points = GeneratePoints(100, -100, 100)

    if len(points) == 0:
        print("Nie ma punktow")
        return []

    result = Graham(points)

    return points, result

if __name__ == "__main__":
    points, result = GetResult()

    print("Punkty otoczki:")
    for point in result:
        point.print()

    plot_convex_hull(points, result)
