#klass punkta
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def print(self, i):
        print("point" + str(i) + "(x" + str(i) + ":" , self.x, "y" + str(i) + ":", self.y, ")")

    def __gt__(self, other):
        return other.x < self.x

    def __str__(self) -> str:
        return ("(x: " + str(self.x) + ", y:" + str(self.y) + ")")

    

#wyznacznik macierzy
def detOfMatrix(p1,p2,p3) -> int:
    return p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.y * p3.x - p1.y * p2.x - p3.y * p1.x

#czy punkt p3 nalezy do odcinka p1p2
def CzynalezyDoOdcinka(p1,p2,p3, czywypis) -> bool:
    wspoliniowe = detOfMatrix(p1,p2,p3)

    if czywypis: 
        print("Wyznacznik wspoliniowosci: " + str(wspoliniowe))

    nalezy = False

    if wspoliniowe == 0:
        nalezy = True
        if p3.x < min(p1.x, p2.x):
            nalezy = False
        if p3.x > max(p1.x, p2.x):
            nalezy = False
        if p3.y > max(p1.y, p2.y):
            nalezy = False
        if p3.y < min(p1.y, p2.y):
            nalezy = False

    if czywypis:
        print("czy punkt " + str(p3) + "\nnalezy do prostej wyznaczonej przez punkty:\n" + str(p1) + "\n" + str(p2) + "\n: " + str(nalezy))

    return nalezy


if __name__ == "__main__":
        
    points = []

    for i in range(3):
        print("x" + str(i+1) + ": ")
        x = int(input())
        print("y" + str(i+1) + ": ")
        y = int(input())
        points.append(Point(x,y))

    CzynalezyDoOdcinka(points[0], points[1], points[2], True)