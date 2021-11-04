def run(prg, registers, r, other, times, total_sent, i):
    while i in range(len(data)):
        if data[i][0] == 'snd':
            if prg == -1:
                snd = registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1])
            else:
                other.append(registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1]))
                total_sent += 1
        elif data[i][0] == 'set':
            registers[data[i][1]] = registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
        elif data[i][0] == 'add':
            registers[data[i][1]] += registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
        elif data[i][0] == 'mul':
            registers[data[i][1]] *= registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
        elif data[i][0] == 'mod':
            registers[data[i][1]] %= registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
        elif data[i][0] == 'rcv':
            if prg == -1:
                if registers[data[i][1]] != 0:
                    print(snd)
                    break
            if r:
                registers[data[i][1]] = r[0]
                r.pop(0)
                times = 0
            else:
                if not times:
                    return prg, registers, r, other, times+1, total_sent, i
                else:
                    return 0,0,0,0,times+1,total_sent, i
        elif data[i][0] == 'jgz' and (registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1])) > 0:
            i += registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
            continue
        i+=1
    return prg, registers, r, other, times + 1, total_sent, i

with open("day18.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
    registers = {x[1] : 0 for x in data}
    p0 = {k:v for k,v in registers.items()}
    p1 = {k:v for k,v in p0.items()}
    p1['p'] = 1
    p0_r, p1_r = [], []
    t0, t1 = 0, 0
    s0, s1 = 0, 0
    i0, i1 = 0, 0
    run(-1, registers, 0, 0, 0, 0, 0)
    while t0 < 2 or t1 < 2:
        if p0:
            prg, p0, p0_r, p1_r, t0, s0, i0 = run(0, p0, p0_r, p1_r, t0, s0, i0)
        if p1:
            prg, p1, p1_r, p0_r, t1, s1, i1 = run(1, p1, p1_r, p0_r, t1, s1, i1)
    print(s1)
