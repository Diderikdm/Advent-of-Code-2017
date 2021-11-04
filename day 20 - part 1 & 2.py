with open("day20.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    p, v, a = {}, {}, {}
    for e, part in enumerate(data):
        q,r,s = [[int(u) for u in z] for z in [y.split(',') for y in [x.split('<')[1].strip('>') for x in part.split(', ')]]]
        p[e], v[e], a[e] = q, r, s
    print(sorted(a.items(), key = lambda x: sum(abs(y) for y in x[1]))[0][0])
    while [x[0] for x in sorted(p.items(), key = lambda x: sum(abs(y) for y in x[1]))] != [x[0] for x in sorted(a.items(), key = lambda x : (sum(abs(y) for y in x[1]), sum(abs(y) for y in p[x[0]])))]:
        lst = [tuple(y) for y in p.values()]
        to_remove = [x for x in p.keys() if lst.count(tuple(p[x])) > 1]
        for x in to_remove:
            p.pop(x)
            v.pop(x)
            a.pop(x)
        for e, vals in a.items():
            v[e][0] += vals[0]
            v[e][1] += vals[1]
            v[e][2] += vals[2]
            p[e][0] += v[e][0]
            p[e][1] += v[e][1]
            p[e][2] += v[e][2]
    print(len(p))
