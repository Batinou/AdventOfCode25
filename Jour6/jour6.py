from math import prod
from pathlib import Path

p = Path("Jour6\\input.txt")

lines = p.read_text(encoding="utf-8").splitlines()
total = 0
column = len(lines[0]) - 1
numbers = []

while column >= 0:
    while True:
        numbers.append(int(''.join([line[column] for line in lines[:-1]])))
        if lines[-1][column] == ' ': column -= 1
        else:
            ajout = (sum(numbers) if lines[-1][column] == '+' else prod(numbers))
            total = total + ajout
            numbers = [] 
            column = column - 2
            break
print(total)