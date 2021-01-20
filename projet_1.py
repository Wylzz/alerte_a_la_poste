warning = open('warning.txt', 'r')
connexion = open('connexion.log', 'r')

# exercice 1

def log(file):
    z = list(file)

    for x in z:
        a = x.split(";")
        b = a[2].split(" ")
        hours, minutes = map(int, b[1].split(':'))
        if hours > 19 or hours < 8:
            # print(b[1])
            print(a[1])
            print(a[0])
            break


#log(connexion)

# exercice 1 et 2

def warn(txt, logg):
    u = list(logg)
    z = list(txt)

    for x in u:
        a = x.split(";")
        for e in z:
            h = e.rstrip()
            if h == a[0]:

                o = open("suspect.txt", "a")
                o.write(a[1] + ";" + str(h.count(a[0])) + "\n")
                print(a[1])


warn(warning, connexion)