from pathlib import Path
import itertools

p = Path("Jour10\\input.txt")

lines = p.read_text(encoding="utf-8").splitlines()

machines = []

for line in lines:
    machine = line.split()
    lumiere = []
    for char in machine[0]:
        if char == '#':
            lumiere.append(True)
        elif char == '.':
            lumiere.append(False)

    buttons = []
    for string in machine[1:-1]:
        numbers = string.removeprefix("(").removesuffix(")").split(',')
        button = list(map(int,numbers))
        buttons.append(button)
    
    joltage = []
    for char in machine[-1]:
        if char.isdigit():
            joltage.append(int(char))
    machines.append((lumiere,buttons,joltage))

def pressbuttonslight(state, buttons):
    for step in buttons:
        for button in step:
            state[button] = not state[button]

def fewestbuttonpresslight(lumiere, buttons):
    lumzero = [False] * len(lumiere)
    for iteration in range(1,len(buttons)):
        combinaisons = list(itertools.combinations(buttons,iteration))
        for combinaison in combinaisons:
            lumact = lumzero.copy()
            pressbuttonslight(lumact,combinaison)
            if(lumact == lumiere):
                return iteration

totalpressed = 0

for i in range(len(machines)):
    totalpressed += fewestbuttonpresslight(machines[i][0],machines[i][1])

print(totalpressed)