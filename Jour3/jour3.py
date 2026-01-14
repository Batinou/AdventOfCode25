import fileinput

fileinput.close()
filename = 'Jour3\\input.txt'
f = open(filename, 'r')

total = 0

def maxarray(array, length):
    newarray = []
    if(length == 1):
        newarray.append(max(array))
        return newarray
    else:
        maximum = max(array[0:-(length - 1)])
        newarray.append(maximum)
        arraydroite = array[array.index(maximum) + 1:]
        arrayrec = maxarray(arraydroite, length - 1)
        return newarray + arrayrec


for line in f.readlines():
    array = [int(i) for i in str(line[0:-1])]
    digits = maxarray(array,12)
    number = int(''.join(map(str, digits)))
    total += number


print(total)
f.close()