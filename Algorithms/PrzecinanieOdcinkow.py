from PrzynPunktDoOdc import *

def PrzecinanieOdcinkow(p1,p2,p3,p4):
    k = False
    det1 = detOfMatrix(p1,p2,p3)
    det2 = detOfMatrix(p1,p2,p4)
    det3 = detOfMatrix(p3,p4,p1)
    det4 = detOfMatrix(p3,p4,p2)

    print(det1, det2, det3, det4)

    if det1 * det2 < 0 and det3 * det4 < 0:
        k = True
    if det3 * det4 < 0 and det1 * det2 < 0:
        k = True
    
    if det1 == 0 or det2 == 0 or det3 == 0 or det4 ==0:
        if det1 == 0 or det2 == 0:
            if CzynalezyDoOdcinka(p1,p2,p3, False) or CzynalezyDoOdcinka(p1,p2,p4,False):
                k = True
        if det3 == 0 or det4 == 0:
            if CzynalezyDoOdcinka(p3,p4,p1, False) or CzynalezyDoOdcinka(p3,p4,p2,False):
                k = True
    return k


if __name__ == "__main__":
    points = []
    # for i in range(4):
    #     print("x" + str(i+1) + ":")
    #     x = int(input())
    #     print("y" + str(i+1) + ":")
    #     y = int(input())
    #     points.append(Point(x,y))
    

    # Testy #
    p1 = PrzecinanieOdcinkow(Point(1,2), Point(7,6),Point(7,3),Point(9,1)) #nie
    p2 = PrzecinanieOdcinkow(Point(1,1), Point(5,5),Point(3,3),Point(6,6)) #tak
    p3 = PrzecinanieOdcinkow(Point(1,1), Point(5,5),Point(3,3),Point(5,2)) #tak
    p4 = PrzecinanieOdcinkow(Point(1,1), Point(5,5),Point(3,3),Point(4,4)) #tak
    p5 = PrzecinanieOdcinkow(Point(1,1), Point(5,5),Point(6,6),Point(7,7)) #nie
    
    if p1:
        print("1: przecinaja sie")
    else:
        print("1: nie przecinaja sie")

    if p2:
        print("2: przecinaja sie")
    else:
        print("2: nie przecinaja sie")

    if p3:
        print("3: przecinaja sie")
    else:
        print("3: nie przecinaja sie")
    if p4:
        print("4: przecinaja sie")
    else:
        print("4: nie przecinaja sie") 
    if p5:
        print("5: przecinaja sie")
    else:
        print("5: nie przecinaja sie")
