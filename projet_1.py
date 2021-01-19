warning = open('warning.txt', 'r')
connexion = open('connexion.log', 'r')


def log(file):
    z = list(file)

    for x in z:
        a = x.split(";")
        b = a[2].split(" ")
        hours, minutes = map(int, b[1].split(':'))
        if hours > 19:
            # print(b[1])
            print(a[1])
            print(a[0])
            break


#log(connexion)


def warn(txt, logg):
    u = list(logg)
    z = list(txt)

    for x in u:
        a = x.split(";")
        for e in z:
            h = e.rstrip()
            if h == a[0]:

                o = open("suspect.txt", "a")
                o.write(a[1] + ";" + "\n")
                print(a[1])

warn(warning, connexion)

'''o = open("suspect.txt", "w+")
o.write(str(warn(warning, connexion)))'''

'''
for x in z:
    v = x.split
    print(x)'''

'''for x in range(0, 11):
    for v in z:
        a = v.replace(str(x), '')
        print(a)'''

'''for x in z:
    a = x.replace(".", "")
    b = a.replace("1", "")
    c = b.replace("2", "")
    d = c.replace("3", "")
    e = d.replace("4", "")
    f = e.replace("5", "")
    g = f.replace("6", "")
    h = g.replace("7", "")
    i = h.replace("8", "")
    j = i.replace("9", "")
    k = j.replace("10", "")
    l = k.replace("0", "")
    m = l.replace("/", "")
    o = m.replace(":", "")
    print(o.replace(";", ""))'''

'''str = open('connexion.log', 'r')
print(f.read())

z = list(str)
for x in z:
    print(x)

    with open('connexion.log', 'r') as f:
    mylist = [line.rstrip('\n') for line in f]

    print(mylist)'''
