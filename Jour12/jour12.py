from pathlib import Path

p = Path("Jour12\\input.txt")

lines = p.read_text(encoding="utf-8").splitlines()

shapes = {}
areas = []
numperarea = []

for line in range(len(lines)) :
    if lines[line] and lines[line][0].isnumeric() and lines[line][1] == ":":
        shapes[int(lines[line][0])] = lines[line+1] + "\n" + lines[line+2] + "\n" + lines[line+3]

    elif lines[line] and lines[line][0].isnumeric() and lines[line][2] == "x":
        splitline = lines[line].split(':')
        sarea = splitline[0].split('x')
        area = (int(sarea[0]),int(sarea[1]))
        areas.append(area)
        numbers = []
        for num in splitline[1].split(' ')[1:]:
            numbers.append(int(num))
        numperarea.append(numbers)
    

def shapecountdiese(shapetocount:str):
    return shapetocount.count('#')

areasofshape = []

for shape in shapes.values():
    areasofshape.append(shapecountdiese(shape))

def compareareatocount(area,count):
    a1, a2 = area[0], area[1]
    zonearea = a1*a2
    areaoccupied = 0
    for i in range(len(count)):
        areaoccupied += areasofshape[i] * count[i]

    if areaoccupied > zonearea:
        return 0

    return 1

fit = 0

for pack in range(len(areas)):
    fit += compareareatocount(areas[pack],numperarea[pack])

print(fit)