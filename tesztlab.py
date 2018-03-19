from random import choice, randint, randrange
import tkinter
import time


tablameret = 157
tabla = [[0] * tablameret for i in range(tablameret)]
pontmeret = 3
wait = 0.00

def keretrajzol():
    for x in range(tablameret-1):
        point(x, 0)
        point(x, tablameret-1)
        point(0, x)
        point(tablameret-1, x)
    point(tablameret-1, x+1)

def point(x,y):
    canvas.create_rectangle(x*pontmeret, y*pontmeret, (x+1)*pontmeret, (y+1)*pontmeret, fill='black')
    tabla[x][y] = 1
    time.sleep(wait)
    canvas.update()

def get_point(x, y):
    return tabla[y][x] == 1

def vonalhuz(s1, v):
    s = [s1[0]]
    s.append(s1[1])
    if s[0] == v[0]: #függőleges
        if abs(v[1] - s[1]) > 0:
            ajto = randint(0, abs(v[1] - s[1]))
            irany = int((v[1]-s[1])/abs(v[1]-s[1]))
            ajto = (ajto*irany) + s[1]
            if tabla[s[0]][s[1]-irany] == 0:
                s[1] += irany
                ajto = 9999
            if tabla[v[0]][v[1]+irany] == 0:
                v[1] -= irany
                ajto = 9999
            for i in range(s[1],v[1]+irany,irany):
                if i != ajto:
                    point(s[0],i)
    else:          #vízszintes
        if abs(v[0] - s[0]) > 0:
            ajto = randint(0, abs(v[0] - s[0]))
            irany = int((v[0]-s[0])/abs(v[0]-s[0]))
            ajto = (ajto*irany) + s[0]
            if tabla[s[0]-irany][s[1]] == 0:
                s[0] += irany
                ajto = 9999
            if tabla[v[0]+irany][v[1]] == 0:
                v[0] -= irany
                ajto = 9999
            for i in range(s[0],v[0]+irany,irany):
                if i != ajto:
                    point(i,s[1])

def van_fal(x, y, xirany, yirany):
    return tabla[x-xirany][y-yirany]==1 or tabla[x][y]==1 or tabla[x+xirany][y+yirany]==1

def get_fal_vege(start, xirany, yirany):
    x = start[0]
    y = start[1]
    while not van_fal(x+xirany, y+yirany, yirany, xirany):
        x += xirany;
        y += yirany;
    return x, y

def rnd(p1, p2):
    if p1 == p2:
        return p1
    else:
        return randrange(p1, p2, 2)
        '''r = range(p1, p2, 2)
        m = int((len(r))*1/3)
        n = int((len(r))*2/3)
        return randrange(r[m],r[n],2)'''

def labgen_vizsz(start, irany):
    x = start[0]
    y = start[1]
    end_x, end_y = get_fal_vege(start, irany, 0)
    if end_x == x:
        return
    else:
        vonalhuz(start,[end_x, y])
    if abs(end_x - x) < 2:
        return
    if abs(end_x - x) == 2:
        x += irany
        labgen_fugg([x, y+1], 1)
        labgen_fugg([x, y-1], -1)
    else:
        for irany in range(1, -2, -2):
            x = rnd(min(start[0], end_x)+1, max(start[0], end_x))
            labgen_fugg([x, y+irany], irany)
    return

def labgen_fugg(start, irany):
    x = start[0]
    y = start[1]
    end_x, end_y = get_fal_vege(start, 0, irany)
    if end_y == y:
        return
    else:
        vonalhuz(start, [x, end_y])
    if abs(end_y - y) < 2:
        return
    if abs(end_y - y) == 2:
        y += irany
        labgen_vizsz([x+1, y], 1)
        labgen_vizsz([x-1, y], -1)
    else:
        for irany in range(1, -2, -2):
            y = rnd(min(start[1], end_y)+1, max(start[1], end_y))
            labgen_vizsz([x+irany, y], irany)
    return

root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.config(width=pontmeret*tablameret+pontmeret, height=pontmeret*tablameret+pontmeret)
canvas.pack()
keretrajzol()
canvas.pack()
labgen_vizsz([1,rnd(2, tablameret-3)], 1)
root.mainloop()

