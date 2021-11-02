with open("C:\\Advent\\2017\\day9.txt", 'r') as file:
    data = [x for x in file.read()]
    i = 0
    cancelled = 0
    while i in range(len(data)):
        if data[i] == '<':
            if '>' in data:
                cls = data[i:].index('>')
                if '!' in data:
                    excl = data[i:].index('!')
                    while cls > excl:
                        for x in range(i + excl + 1, i + excl - 1, -1):
                            data.pop(x)
                        excl = data[i:].index('!') if '!' in data else data[i:].index('>')
                        cls = data[i:].index('>')
            cancelled += len(range(i + 1, i + cls))
            for x in range(i + cls, i - 1, -1):
                data.pop(x)
        else:
            i += 1
    data = [x for x in ''.join(data).replace(',','')]
    total = 0
    times = 0
    for x in data:
        if x == '{':
            times += 1
        else:
            total += times
            times -= 1
    print(total)
    print(cancelled)
