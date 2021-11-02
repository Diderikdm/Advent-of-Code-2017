with open("C:\\Advent\\2017\\day8.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    registers = {x.split()[0] : 0 for x in data}
    mx = 0
    for row in data:
        reg, op, amt, void, target, comp, t_amp = [int(x) if x.strip('-').isdigit() else x for x in row.split()]
        registers[reg] = eval('{} {} {}'.format(registers[reg], '+' if op == 'inc' else '-', amt)) if eval('{} {} {}'.format(registers[target], comp, t_amp)) else registers[reg]
        mx = max(mx, registers[reg]) 
    print(max(registers.values()))
    print(mx)
