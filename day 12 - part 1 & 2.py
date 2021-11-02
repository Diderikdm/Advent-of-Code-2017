def find(current):
    for x in data[current]:
        if x not in prgs:
            prgs.append(x)
            find(x)


with open("day12.txt", 'r') as file:       
    data = {e : [int(y) for y in x.split(' <-> ')[1].split(', ')] for e,x in enumerate(file.read().splitlines())}
    prgs = [0]
    groups = []
    find(0)
    print(len(prgs))
    i = 1
    while any(x not in prgs for x in data.keys()):
        x = next(iter(x for x in data.keys() if x not in prgs), None)
        find(x)
        i += 1
    print(i)
