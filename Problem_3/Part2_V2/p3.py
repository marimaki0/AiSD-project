import random
import matplotlib.pyplot as plt

#max brightness
MAX_RANDOM_BRIGHTNESS = 20
MIN_RANDOM_BRIGHTNESS = 2

#robimy losowy slownik jasnosci
def MakeRandomBrightness(otoczka: int) -> dict:
    otoczka_brightness = {}
    for i in range(1, otoczka + 1):
        otoczka_brightness[i] = random.randint(MIN_RANDOM_BRIGHTNESS, MAX_RANDOM_BRIGHTNESS)
    return otoczka_brightness

#znalezc maksymalna liczbe, mniejsza niz podana
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

# Glowna czesc algorytmu
def GetOptimalStops(brightness_dict: dict, security_energy: int) -> list[int]:
    optimal_stops = []
    current_position = 1
    remaining_energy = security_energy
    path = [current_position]
    energy_levels = [remaining_energy]

    if not brightness_dict:
        return optimal_stops

    current_brightness = brightness_dict[current_position]

    while brightness_dict:
        #robimy liste jasnosci dostepnych punktow
        start_index = max(0, current_position - remaining_energy - 1)
        end_index = min(len(brightness_dict), current_position + remaining_energy)
        points_range = list(brightness_dict.values())[start_index:end_index]

        if not points_range:
            break

        next_stop = FindMaxLessThan(points_range, current_brightness)

        if next_stop is None:
            next_stop = max(points_range)

        optimal_stops.append(next_stop)
        key_next_stop = FindKeysByValue(brightness_dict, next_stop)[0]

        #aktualizacja energii
        distance_travelled = abs(key_next_stop - current_position)
        remaining_energy -= distance_travelled

        #sprawdzenie czy straznik musi odpoczac
        if next_stop >= current_brightness or remaining_energy <= 0:
            remaining_energy = security_energy  #odpoczynek i odzyskanie energii

        current_position = key_next_stop
        path.append(current_position)
        energy_levels.append(remaining_energy)
        current_brightness = brightness_dict.pop(current_position)

    # print("Path: ", path)
    # print("Energy levels: ", energy_levels)

    
    return optimal_stops


if __name__ == "__main__":
    # Testowanie
    otoczka = 7
    sec1 = 6
    test1 = {1: 9, 2: 8, 3: 6, 4: 5, 5: 19, 6: 10, 7: 15}
    print("Optimal stops (new):", GetOptimalStops(test1, sec1))
