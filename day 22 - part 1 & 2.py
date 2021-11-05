with open("day22.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    grid = {}
    for y, row in enumerate(data):
        for x, what in enumerate(row):
            if what == '#':
                grid[(x,y)] = what
    grid_2 = {k:v for k,v in grid.items()}
    d = 0
    cur_dir = ['u', 'r', 'd', 'l']
    dirs = {'u' : lambda x,y : (x,y-1), 'r' : lambda x,y : (x+1,y), 'd' : lambda x,y : (x,y+1), 'l' : lambda x,y : (x-1,y)}
    current = (len(data[0])//2, len(data)//2)
    bursts = 0
    for i in range(10000):
        if current not in grid:
            d = (d - 1) % 4
            grid[current] = '#'
            bursts += 1
        else:
            d = (d + 1) % 4
            grid.pop(current)
        current = dirs[cur_dir[d]](*current)
    print(bursts)
    
    d = 0
    current = (len(data[0])//2, len(data)//2)
    bursts = 0
    grid = grid_2
    for i in range(10000000):
        if current not in grid:
            d = (d - 1) % 4
            grid[current] = 'W'
        elif grid[current] == '#':
            d = (d + 1) % 4
            grid[current] = 'F'
        elif grid[current] == 'W':
            grid[current] = '#'
            bursts += 1
        elif grid[current] == 'F':
            d = (d + 2) % 4
            grid.pop(current)
        current = dirs[cur_dir[d]](*current)
    print(bursts)
            
            
    
            
