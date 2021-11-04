with open("day16.txt", 'r') as file:       
    data = [x for x in file.read().split(',')]
    progs = [chr(x) for x in range(97, 113)]
    dances = []
    while True:
        progs = [x for x in progs]
        for x in data:
            if x[0] == 's':
                progs = progs[-int(x[1:]):] + progs[:-int(x[1:])]
            elif x[0] == 'x':
                a, b = [int(y) for y in x[1:].split('/')]
                av, bv = progs[a], progs[b]
                progs[a], progs[b] = bv, av
            elif x[0] == 'p':
                a, b = [progs.index(y) for y in x[1:].split('/')]
                av, bv = progs[a], progs[b]
                progs[a], progs[b] = bv, av
        dance = ''.join(progs)
        if dance not in dances:
            dances.append(''.join(progs))
        else:
            break
    print(dances[0])
    print(dances[1000000000 % len(dances) - 1])
