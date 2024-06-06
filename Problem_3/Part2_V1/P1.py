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
def GetOptimalStops(brightness_dict: dict, security_energy: int) -> list[int]:

    optimal_stops = []
    current_position = 1

    if not brightness_dict:
        return optimal_stops
    
    current_brightness = brightness_dict[current_position]

    while brightness_dict:
        # Robimy liste jasnosci dostepnych punktow
        start_index = max(0, current_position - security_energy - 1)
        end_index = min(len(brightness_dict), current_position + security_energy)
        points_range = list(brightness_dict.values())[start_index:end_index]

        if not points_range:
            break

        next_stop = FindMaxLessThan(points_range, current_brightness)

        if next_stop is None:
            next_stop = max(points_range)

        optimal_stops.append(next_stop)
        key_next_stop = FindKeysByValue(brightness_dict, next_stop)[0]

        current_position = key_next_stop
        current_brightness = brightness_dict.pop(current_position)

    return optimal_stops

        

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