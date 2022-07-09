import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for i in it.permutations(notes,4):
    print(i)

print(f"there is {math.factorial(len(notes))/math.factorial(len(notes)-4)} posibilities")

for i in it.product(notes,repeat=4):
    print(i)

print(f"there is {pow(len(notes),4)} posibilities")