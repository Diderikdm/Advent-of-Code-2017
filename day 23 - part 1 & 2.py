with open("day23.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
    for registers in [{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}, {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}]:
        muls = 0
        i = 0
        h = 0
        while i in range(len(data)):
            if registers['a'] == 1 and data[i][0] == 'jnz':
                sorted_regs = sorted(registers.items(), key=lambda x: x[1])
                if sorted_regs[-3][1] % 2 == 1 and sorted_regs[-3][1] * 2 - sorted_regs[-2][1] == sorted_regs[0][-1]:
                    for x in range(sorted_regs[-2][1], sorted_regs[-1][1] + 1, 17):
                        if any(x % y == 0 for y in range(2, x)):
                            h += 1
                    break
            if data[i][0] == 'set':
                registers[data[i][1]] = registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
            elif data[i][0] == 'sub':
                registers[data[i][1]] -= registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
            elif data[i][0] == 'mul':
                muls += 1
                registers[data[i][1]] *= registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
            elif data[i][0] == 'jnz' and (registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1])) != 0:
                i += registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
                continue
            i+=1
        if registers['a'] == 0:
            print(muls)
        else:
            print(h)
