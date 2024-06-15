import random
import numpy as np

def GenerateAndFindMaxPlaszczaki(punkty_otoczki: list[int]) -> list[int]:
    #Tworzymy listu plaszczakow, w której będzie maksymalna ilosc energii - to ilość punktów otoczki
    plaszczaki=[random.randint(0, len(punkty_otoczki)) for _ in range(800)]

    #Dzielimy na 8 części i wybieramy z maksymalną energią
    parts = np.array_split(plaszczaki, 8)
    max_numbers = [np.max(part) for part in parts]

    return max_numbers

if __name__ == "__main__":
    max_numbers = GenerateAndFindMaxPlaszczaki(100)
    strazniki = {}
    counter=1

    for i in max_numbers:
            strazniki[f"plasczak {counter}"]=i
            counter+=1

    for key, value in strazniki.items():
        print(f"{key}: {value}")



