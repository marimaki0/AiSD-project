import random
<<<<<<< HEAD
import numpy as np
import Problem_1.Punkt_2.otoczka_wypukla_grahama as p6
=======
from numpy import array_split, max
>>>>>>> a534097 (testing3)

def generate_and_find_max_plaszczaki(punkty_otoczki: list[int]) -> list[int]:

    plaszczaki=[random.randint(0, len(punkty_otoczki)) for _ in range(800)]

    parts = array_split(plaszczaki, 8)
    max_numbers = [max(part) for part in parts]

    strazniki = {}
    counter=1

    for i in max_numbers:
            strazniki[f"plasczak {counter}"]=i
            counter+=1

    for key, value in strazniki.items():
        print(f"{key}: {value}")

    return max_numbers

if __name__ == "__main__":
    max_numbers = generate_and_find_max_plaszczaki(100)
    strazniki = {}
    counter=1

    for i in max_numbers:
            strazniki[f"plasczak {counter}"]=i
            counter+=1

    for key, value in strazniki.items():
        print(f"{key}: {value}")



