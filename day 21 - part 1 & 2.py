def turn(lines, turns):
    for x in range(turns):
        turn = []
        for y in range(len(lines)):
            turn.append(''.join([''.join(z[y]) for z in reversed(lines)]))
        lines = [y for y in turn]
    return '/'.join(lines)


with open("day21.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    guide = {}
    prog = ['.#.',
            '..#',
            '###']
    for row in data:
        rule, res = row.split(' => ')
        lines = rule.split('/')
        for x in set([turn(lines, 1),
                      turn(lines, 2),
                      turn(lines, 3),
                      turn(lines, 4),
                      turn([x[::-1] for x in lines], 1),
                      turn([x[::-1] for x in lines], 2),
                      turn([x[::-1] for x in lines], 3),
                      turn([x[::-1] for x in lines], 4)]):
            guide[x] = res
            
    for i in range(18):
        temp = []
        t = 2 if len(prog) % 2 == 0 else 3
        for y in range(int(len(prog) / t)):
            res = ['' for x in range(t + 1)]
            for x in range(int(len(prog) / t)):
                result = guide['/'.join([prog[y * t + z][x * t : (x + 1) * t] for z in range(t)])].split('/')
                for e,z in enumerate(result):
                    res[e] += result[e]
            temp += res
        prog = temp
        if i == 4 or i == 17:
            print(''.join(prog).count('#'))
