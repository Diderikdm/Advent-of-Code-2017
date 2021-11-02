with open("day11.txt", 'r') as file:
    data = [x for x in file.read().split(',')]
    walk = {'n' : lambda x,y : (x,y+2),
            'ne': lambda x,y : (x+1,y+1),
            'se': lambda x,y : (x+1,y-1),
            's' : lambda x,y : (x,y-2),
            'sw': lambda x,y : (x-1,y-1),
            'nw': lambda x,y : (x-1,y+1)}
    current = (0,0)
    steps = []
    for x in data:
        current = walk[x](*current)
        steps.append((abs(current[0]) + abs(current[1])) // 2)
    print(steps[-1])
    print(max(steps))    
