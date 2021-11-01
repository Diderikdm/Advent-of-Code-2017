with open("C:\\Advent\\2017\\day6.txt", 'r') as file:
    data = [int(y) for y in [x.split() for x in file.read().splitlines()][0]]
    states = []
    state = data[:]
    e = 0
    p1 = None
    p2 = None
    while tuple(state) not in states or p2:
        states.append(tuple(state))
        current = state.index(max(state))
        val = state[current]
        state[current] = 0
        i = 0
        for x in range(val):
            i += 1
            state[(current + i) % len(state)] += 1
        e += 1
        if tuple(state) == p2:
            p2 = e - p1
            break
        p2 = p2 or tuple(state) if tuple(state) in states else None
        p1 = p1 or e if p2 else None
    print(p1)
    print(p2)
