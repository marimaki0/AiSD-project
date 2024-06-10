import random
import numpy as np

def generate_and_find_max_plaszczaki(punkty_otoczki: int) -> list[int]:
    plaszczaki=[random.randint(0, punkty_otoczki) for _ in range(800)]

    parts = np.array_split(plaszczaki, 8)
    max_numbers = [np.max(part) for part in parts]

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



