from PrzynPunktDoOdc import *

def gift_wrapping(points):
    on_hull = min(points)
    hull = []
    while True:
        hull.append(on_hull)
        next_point = points[0]
        for point in points:
            o = detOfMatrix(on_hull, next_point, point)
            if next_point == on_hull or o > 0:
                next_point = point
        on_hull = next_point
        if on_hull == hull[0]:
            break
    return hull

if __name__ == "__main__":
        
    arr_points = []

    n = int(input())
    for i in range (n):
        print("x: ")
        x = int(input())
        print("y: ")
        y = int(input())
        point = Point(x, y)
        arr_points.append(point)

    arr_points.sort()

    hall = gift_wrapping(arr_points)
    for i in hall:
        print(i)

    # Протестировать, не уверен что до конца работает