from pathlib import Path

p = Path("Jour7\\input.txt")

lines = p.read_text(encoding="utf-8").splitlines()

compte = []

#first line
for char in lines[0]:
    if char == 'S':
        compte.append(1)
    else:
        compte.append(0)

total = 0
totalsep = compte.copy()

for line in lines[1:]:
    suivant = compte.copy()
    for i in range(len(line)):
        if compte[i] >= 1 and line[i] == '^':
            total += 1
            
            if(i-1 >=0):
                suivant[i-1] = suivant[i] + 1
                totalsep[i-1] +=1
                
            if(i+1 < len(line)):
                suivant[i+1] = suivant[i] + 1
                totalsep[i+1] += 1

            suivant[i] = 0

    compte = suivant
    print(compte)

print(total)
print(totalsep)
tot = 0
for i in totalsep:
    tot += i
print(tot)