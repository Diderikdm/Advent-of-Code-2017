from itertools import combinations

def find_group(x):
    if x not in prev:
        prev.add(x)
        for y in adj(*x):
            find_group(y)
        

def calc(lst, i = 0, inc = 0):
    for length in data:
        slc = [lst[x % len(lst)] for x in range(i, i + length)][::-1]
        if i + length > len(lst) - 1:
            slc = [lst[x % len(lst)] for x in range(i, i + length)][::-1]
            for e, y in enumerate(slc):
                lst[(i + e) % len(lst)] = y
        else:
            lst = lst[: i] + lst[i : i + length][::-1] + lst[i + length:]
        i = (i + length + inc) % len(lst)
        inc += 1
    return (lst, i, inc)


start = 'xlqgujun'
knots = []
idx = [str(x) for x in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
for y in range(128):
    data = [ord(x) for x in '{}-{}'.format(start, y)] + [17, 31, 73, 47, 23]
    lst, i, inc = [x for x in range(256)], 0, 0
    for x in range(64):
        lst, i, inc = calc(lst, i, inc)
    knot = ''.join([hex(z)[2:].rjust(2, '0') for z in [eval(' ^ '.join([str(x) for x in lst[y: y + 16]])) for y in range(0, len(lst), 16)]])
    knots.append(knot)
grid = {}
for y in range(128):
    for x in range(0, 128, 4):
        grid[(x,y)], grid[(x+1,y)], grid[(x+2,y)], grid[(x+3,y)] = [int(z) for z in bin(idx.index(knots[y][x//4]))[2:].rjust(4, '0')]
filtered = [k for k,v in grid.items() if v]
print(len(filtered))
prev = set()
adj = lambda x,y : list(set([(x+a,y+b) for a,b in list(combinations([-1,0,1]*2, 2)) if sum([a,b]) in [-1,1] and (x+a, y+b) in filtered]))
gr = 0
for x in filtered:
    if x not in prev:
        find_group(x)
        gr += 1
print(gr)
