import matplotlib.pyplot as plt
from otoczka_wypukla_grahama import Graham
from otoczka_wypukla_grahama import GeneratePoints


def Visualisation(points, hull):
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
    points, result=GetResult()

    print("Punkty otoczki:")
    for point in result:
        point.print()

    Visualisation(points, result)
