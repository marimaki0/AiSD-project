NOTWORKING

# import random
# import matplotlib.pyplot as plt
# import numpy as np

# #max brightness
# MAX_RANDOM_BRIGHTNESS = 20
# MIN_RANDOM_BRIGHTNESS = 2

# #robimy losowy slownik jasnosci
# def MakeRandomBrightness(otoczka: int) -> dict:
#     otoczka_brightness = {}
#     for i in range(1, otoczka + 1):
#         otoczka_brightness[i] = random.randint(MIN_RANDOM_BRIGHTNESS, MAX_RANDOM_BRIGHTNESS)
#     return otoczka_brightness

# #znalezc maksymalna liczbe, mniejsza niz podana
# def FindMaxLessThan(numbers: list[int], threshold: int) -> int:
#     max_number = None
#     for number in numbers:
#         if number < threshold and (max_number is None or number > max_number):
#             max_number = number
#     return max_number

# # Znalezc klucz
# def FindKeysByValue(my_dict: dict, value: int) -> list[int]:
#     keys = [key for key, val in my_dict.items() if val == value]
#     return keys

# # Glowna czesc algorytmu
# def GetOptimalStops(brightness_dict: dict, security_energy: int, viz: bool) -> list[int]:
#     optimal_stops = []
#     current_position = 1
#     remaining_energy = security_energy
#     path = [current_position]
#     energy_levels = [remaining_energy]
#     brightness_dict_cp = brightness_dict.copy()

#     if not brightness_dict:
#         return optimal_stops

#     current_brightness = brightness_dict[current_position]

#     while brightness_dict:
#         #robimy liste jasnosci dostepnych punktow
#         start_index = max(0, current_position - remaining_energy - 1)
#         end_index = min(len(brightness_dict), current_position + remaining_energy)
#         points_range = list(brightness_dict.values())[start_index:end_index]

#         if not points_range:
#             break

#         next_stop = max(points_range)

#         optimal_stops.append(next_stop)
#         key_next_stop = FindKeysByValue(brightness_dict, next_stop)[0]

#         #aktualizacja energii
#         distance_travelled = abs(key_next_stop - current_position)
#         remaining_energy -= distance_travelled

#         #sprawdzenie czy straznik musi odpoczac
#         if next_stop >= current_brightness or remaining_energy <= 0:
#             remaining_energy = security_energy  #odpoczynek i odzyskanie energii

#         current_position = key_next_stop
#         path.append(current_position)
#         energy_levels.append(remaining_energy)
#         current_brightness = brightness_dict.pop(current_position)

#     # print("Path: ", path)
#     # print("Energy levels: ", energy_levels)

#     if viz:
#         VisualizePath(path, energy_levels, otoczka, brightness_dict_cp)

#     return optimal_stops

# def VisualizePath(path, energy_levels, otoczka_len, brightness_dict):
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

#     theta = [2 * np.pi * i / otoczka_len for i in range(otoczka_len)]
#     x = [10 * np.cos(t) for t in theta]
#     y = [10 * np.sin(t) for t in theta]

#     path_x = [x[i - 1] for i in path]
#     path_y = [y[i - 1] for i in path]

#     x.append(x[0])
#     y.append(y[0])
#     path_x.append(path_x[0])
#     path_y.append(path_y[0])

#     ax1.plot(x, y, 'bo-', label='Points')
#     ax1.plot(path_x, path_y, 'ro-', label='Path')
#     for i, txt in enumerate(range(1, otoczka_len + 1)):
#         brightness = brightness_dict.get(i + 1, 0)
#         ax1.annotate(f'{txt}:{brightness}', (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    
#     ax1.annotate('Start', (path_x[0], path_y[0]), textcoords="offset points", xytext=(-10, -20), ha='center', color='green', fontsize=12, fontweight='bold', arrowprops=dict(arrowstyle="->", color='green'))

#     ax1.annotate('End', (path_x[-2], path_y[-2]), textcoords="offset points", xytext=(-10, -20), ha='center', color='red', fontsize=12, fontweight='bold', arrowprops=dict(arrowstyle="->", color='red'))
    
#     for i in range(len(path_x) - 1):
#         ax1.annotate('', xy=(path_x[i + 1], path_y[i + 1]), xytext=(path_x[i], path_y[i]), arrowprops=dict(arrowstyle="->", color='gray'))

#     ax1.set_title("Path on the Polygon")
#     ax1.legend()

#     color = 'tab:blue'
#     ax2.set_xlabel('Step')
#     ax2.set_ylabel('Position', color=color)
#     ax2.plot(range(len(path)), path, color=color, marker='o', label='Path')
#     ax2.tick_params(axis='y', labelcolor=color)
#     ax2.legend(loc='upper left')

#     ax3 = ax2.twinx()  
#     color = 'tab:red'
#     ax3.set_ylabel('Energy Level', color=color)  
#     ax3.plot(range(len(energy_levels)), energy_levels, color=color, marker='x', linestyle='--', label='Energy Level')
#     ax3.tick_params(axis='y', labelcolor=color)
#     ax3.legend(loc='upper right')

#     fig.tight_layout()  
#     plt.title("Path and Energy Levels")
#     plt.show()


# if __name__ == "__main__":
#     # Testowanie
#     otoczka = 7
#     sec1 = 6
#     test1 = {1: 9, 2: 8, 3: 6, 4: 5, 5: 19, 6: 10, 7: 15}
#     print("Optimal stops (new):", GetOptimalStops(test1, sec1, True))
