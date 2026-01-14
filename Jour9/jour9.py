from pathlib import Path
import itertools

p = Path("Jour9\\inputlower.txt")

lines = p.read_text(encoding="utf-8").splitlines()

coord_list = [[int(val)for val in sublist.split(',')] for sublist in lines]


pairs = list(itertools.combinations(coord_list,2))

def area_tiles(pair):
    c1 , c2 = pair[0], pair[1]
    longueur = abs(c1[0]-c2[0]) + 1
    largeur = abs(c1[1]-c2[1]) + 1
    return longueur * largeur

pairs_sorted = sorted(pairs,key=area_tiles, reverse=True)

print (pairs_sorted[0])
print (area_tiles(pairs_sorted[0]))


coord_list.append(coord_list[0])

def bresenham_line(x1, y1, x2, y2):
    coords = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        coords.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return coords

def coordinrect(rect, coord):

    xmax, xmin = max(rect[0][0], rect[1][0]), min(rect[0][0], rect[1][0])
    ymax, ymin = max(rect[0][1], rect[1][1]), min(rect[0][1], rect[1][1])

    return xmin<coord[0]<xmax and ymin<coord[1]<ymax
        

def intersect(rect,startline, endline):
    for coord in bresenham_line(startline[0],startline[1],endline[0],endline[1]):
        if(coordinrect(rect,coord)):
            print("La ligne : " + str(startline) + "," + str(endline) + " coupe le rectange : " + str(rect) + " en "+ str(coord))
            return True

    return False

for bigger in pairs_sorted:
    inter = False
    for numedge in range(len(coord_list) - 1):
        startline = coord_list[numedge]
        endline = coord_list[numedge + 1]
        if intersect(bigger,startline, endline):
            inter = True
            break
        
    if not inter:
        print(bigger)
        print(area_tiles(bigger))
        break