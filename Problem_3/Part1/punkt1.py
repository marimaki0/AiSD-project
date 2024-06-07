import random
import numpy as np

plaszczaki=[random.randint(0, 100) for _ in range(800)]

part_size=len(plaszczaki)//8 
parts = np.array_split(plaszczaki, 8)
max_numbers = [np.max(part) for part in parts]

strazniki = {}
counter=1
for i in max_numbers:
    strazniki[f"plasczak {counter}"]=i
    counter+=1

for key, value in strazniki.items():
    print(f"{key}: {value}")



