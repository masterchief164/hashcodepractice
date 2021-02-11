def read():
    f = open("inputs/a_example.in", "r")
    c = 0
    pmenu = []
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
    print(pmenu)


read()
