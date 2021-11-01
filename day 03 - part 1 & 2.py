data = 368078
current = (0,0)
i = 1
coords = {current : i}
sums = {current : i}
dirs = lambda x,y : [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]
times = 1
idx = 0
p2 = None
while i <= data:
    for x in [list(range(times))] * 2:
        for y in x:
            i += 1
            current = dirs(*current)[idx % 4]
            coords[current] = i
            if not p2:
                sums[current] = sum(sums[k] for k in dirs(*current) if k in sums)
                p2 = sums[current] if sums[current] > data else None
        idx += 1
    times += 1

print(next(iter(abs(k[0]) + abs(k[1]) for k,v in coords.items() if v == data), None))
print(p2)    
