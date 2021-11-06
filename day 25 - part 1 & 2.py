with open("day25.txt", 'r') as file:
    data = [x.splitlines() for x in file.read().split('\n\n')]
    state = data[0][0].strip('.').split()[-1]
    end = int(data[0][1].split()[-2])
    ops = {}
    lmd = {}
    for x in data[1:]:
        cur = [y.split()[-1].strip(':').strip('.') for y in x]
        cur = [int(y) if y.isdigit() else y for y in cur]
        ops[cur[0]] = cur
        lmd[cur[0]] = lambda x,y : ops[x][2:5] if not y else ops[x][-3:]
    turing = {}
    i=0
    for x in range(end):
        cur = 0 if i not in turing else turing[i]
        write, move, state = lmd[state](state, cur)
        turing[i] = write
        i = i + (1 if move == 'right' else -1)
    print(sum(turing.values()))
