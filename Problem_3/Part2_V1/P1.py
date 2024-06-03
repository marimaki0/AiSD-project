# На входе - otoczka (1-2-3-4-5-...-n)
#           - челик с его зарядом энергии

# На выходе - самый оптимальный проход (точки остановки и кол-во кругов)

# Соотношение otoczka - яркость



# Алгоритм:

# На прохождение одного пункта (от одного к другому)
# тратится 1 единица энергии

# Нам нужно определить паттерн

# 1 идея - считать следующий оптимальный пункт отсановки
# на каждом пункте

# У нас есть определенное кол-во энергии (допустим максимум 10)

# 1. Чувак начинает с пронумированного пункта под номером 1
# 2. Алгоритм
#   а) Он берет пункты в досягаемости энергии челика (окно/итерация)
#   б) Он берет пункт который МЕНЬШЕ чем начальный (по яркости), и самый большой среди оставшихся и
#     добавляет его в массив
#   с) Переходит в этот пункт, удаляет предыдущий(в котором он был) и повторяет пункты а)б)с)
# 3. Возвращает массив без первого элемента (это и будет наш паттерн остановок)
# 4.END


### Algorithm:
import random
from collections import deque

# Max brightness
MAX_RANDOM_BRIGHTNESS = 20
MIN_RANDOM_BRIGHTNESS = 2

# Robimy losowy slownik jasnosci
def MakeRandomBrightness(otoczka: int) -> dict:
    otoczkaBrightness = {}

    for i in range (1, otoczka+1):
        otoczkaBrightness[i] = random.randint(MIN_RANDOM_BRIGHTNESS, MAX_RANDOM_BRIGHTNESS)
    return otoczkaBrightness


# Znalezc maksymalna liczbe, mniejsza niz podana
def FindMaxLessThan(numbers: list[int], threshold: int) -> int:
    max_number = None
    
    for number in numbers:
        if number < threshold and (max_number is None or number > max_number):
            max_number = number
    
    return max_number


# Znalezc klucz
def FindKeysByValue(my_dict: dict, value: int) -> list[int]:
    keys = [key for key, val in my_dict.items() if val == value]
    return keys


# glowna czesc algorytmu
def GetOptimalStops(brightnessdict: dict, securityEnergy: int) -> list[int]:
    optimalStops = []

    pointNowBrightness = brightnessdict[1]
    
            
    # robimy liste jasnosci dostepnych punktow 
    pointsRange = list(brightnessdict.values())[0:securityEnergy+1]

    while brightnessdict:

        print("range: ", pointsRange)
        # pobieramy nextStop
        nextStop = FindMaxLessThan(pointsRange, pointNowBrightness)
        

        if not nextStop:
            nextStop = max(pointsRange)
        print("next stop ", nextStop)

        optimalStops.append(nextStop)
        keyNextStop = FindKeysByValue(brightnessdict, nextStop)

        brightnessdict.pop(keyNextStop[-1], None)

        #вот здесь проблема, надо как-то вернуть список доступных пунктов

        pointsRange = list(brightnessdict.values())[keyNextStop[-1] - 1:securityEnergy+1]
        print("optimal stops: ", optimalStops)

        print("")
    return optimalStops
        

if __name__ == "__main__":
    ### Input data:

    # ilosc punktow otoczki:
    otoczka = 7

    # Ilosc energii plaszczaka
    # max = ilosc punktow otoczki (for example):
    sec = 4


    # randomBrightness = MakeRandomBrightness(otoczka)
    # print(randomBrightness)
    sec1 = 6
    test1 = {1:9, 2:8, 3:6, 4:5, 5:19, 6:10, 7:15} # answer = [8,6,5,19,15,10,9]
    print(GetOptimalStops(test1, sec1))