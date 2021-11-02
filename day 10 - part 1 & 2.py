def calc(lst, i = 0, inc = 0):
    for length in data:
        slc = [lst[x % len(lst)] for x in range(i, i + length)][::-1]
        if i + length > len(lst) - 1:
            slc = [lst[x % len(lst)] for x in range(i, i + length)][::-1]
            for e, y in enumerate(slc):
                lst[(i + e) % len(lst)] = y
        else:
            lst = lst[: i] + lst[i : i + length][::-1] + lst[i + length:]
        i = (i + length + inc) % len(lst)
        inc += 1
    return (lst, i, inc)


with open("day10.txt", 'r') as file:
    data = [int(x) for x in file.read().split(',')]
    lst = [x for x in range(256)]
    lst, i, inc = calc(lst)
    print(lst[0] * lst[1])
    data = [ord(x) for x in ','.join([str(y) for y in data])] + [17, 31, 73, 47, 23]
    lst, i, inc = [x for x in range(256)], 0, 0
    for x in range(64):
        lst, i, inc = calc(lst, i, inc)
    knot = ''.join([hex(z)[2:].rjust(2, '0') for z in [eval(' ^ '.join([str(x) for x in lst[y: y + 16]])) for y in range(0, len(lst), 16)]])
    print(knot)
