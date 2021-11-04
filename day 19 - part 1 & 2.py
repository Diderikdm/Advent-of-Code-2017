with open("day19.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    grid = {}
    dirs = {'u' : lambda x,y : (x,y-1),
            'd' : lambda x,y : (x,y+1),
            'l' : lambda x,y : (x-1,y),
            'r' : lambda x,y : (x+1,y)}
    for y, row in enumerate(data):
        for x, what in enumerate(row):
            if what != ' ':
                grid[(x,y)] = what
    current = next(iter(k for k in grid.keys() if k[1] == 0))
    dr = next(iter(k for k,v in dirs.items() if v(*current) in grid))
    string = ''
    i = 1
    while True:
        if grid[current].isalpha():
            string += grid[current]
        dr = dr if dirs[dr](*current) in grid else next(iter(d for d in dirs.keys() if d in (['l','r'] if dr in ['u','d'] else ['u','d']) and dirs[d](*current) in grid), None)
        if not dr:
            break
        current = dirs[dr](*current)
        i += 1
    print(string)
    print(i)
