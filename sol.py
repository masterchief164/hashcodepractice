pmenu = []
p = 0
t2 = 0
t3 = 0
t4 = 0


def read():
    f = open("inputs/a_example.in", "r")
    global pmenu
    c = 0
    pmenu = []
    global p, t2, t3, t4
    for i in f:
        if c == 0:
            p, t2, t3, t4 = i.rstrip("\\n").split()
            p = int(p)
            t2 = int(t2)
            t3 = int(t3)
            t4 = int(t4)
            c += 1
        else:
            pmenu.append(i.rstrip("\\n").split())
            pmenu[c - 1][0] = int(pmenu[c - 1][0])
            c += 1


read()
