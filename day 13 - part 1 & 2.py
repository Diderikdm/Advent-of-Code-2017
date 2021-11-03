def walk(delay = 0, severity = 0, i = 0):
    for fw in range(max(data.keys()) + 1):
        if i in data:
            if data[i][(i + delay) % (len(data[i])) if i + delay > len(data[i]) - 1 else i + delay] == 0:
                severity += (i * (max(data[i]) + 1))
                if delay > 0:
                    return True
        i += 1
    return severity

with open("day13.txt", 'r') as file:       
    data = {int(x.split(':')[0]) : [y for y in range(int(x.split(': ')[1]))] + [y for y in range(int(x.split(': ')[1]) - 2, 0, -1)] for x in file.read().splitlines()}
    delay = 0
    severity = walk(delay)
    print(severity)
    while severity:
        delay += 1
        severity = walk(delay)
    print(delay)
