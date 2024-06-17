from otoczka_wypukla_grahama import GetResult
from otoczka_wypukla_grahama import Point
from otoczka_wypukla_grahama import Graham

def ReadPointsFromFile(filename):
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
    filename = 'test1.txt'
    custom_points = ReadPointsFromFile(filename)

    result = GetResult(custom_points)

    print("Punkty otoczki:")
    for point in result:
        point.print()
