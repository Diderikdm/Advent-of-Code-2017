def find(current, to_match, data, path):
    tup = tuple(sorted(path))
    if tup in bridges:
        return
    bridges.add(tup)
    for part in data:
        if to_match in part and part not in path:
            next_match = next(iter(x for x in part if x != to_match or part.count(x) == 2), None)
            if next_match:
                find(part, next_match, data, path + [part])

with open("day24.txt", 'r') as file:
    data = [tuple([int(y) for y in x.split('/')]) for x in file.read().splitlines()]
    bridges = set()
    for e,x in enumerate(filter(lambda x: 0 in x, data)):
        find(x, next(iter(y for y in x if y)), data, [tuple(x)])
    print(max(sum(sum(x) for x in y) for y in bridges))
    max_len = max(len(x) for x in bridges)
    print(max(sum(sum(x) for x in y) for y in filter(lambda z: len(z) == max_len, bridges)))
