import fileinput

fileinput.close()
filename = 'Jour1\input.txt'
dial = 50
zeroreached = 0

for line in fileinput.input(files=filename):
    sign = 1 if line[0] == 'R' else -1
    number = int(line[1:])
    
    for i in range(0, number):
        dial = dial + sign
        if (dial % 100 == 0):
            zeroreached = zeroreached + 1
    
    print(dial, end='\n')
    
   
print(zeroreached, end = '\n')