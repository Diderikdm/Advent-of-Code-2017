def calc(data, a = 1, b = 1, cur = 0, y = 40000000):
    for x in range(y):
        data['A'] = (data['A'] * 16807) % 2147483647
        while data['A'] % a != 0:
            data['A'] = (data['A'] * 16807) % 2147483647
        data['B'] = (data['B'] * 48271) % 2147483647
        while data['B'] % b != 0:
            data['B'] = (data['B'] * 48271) % 2147483647 
        if not int(bin(data['A'] - data['B'])[-16:].replace('b','0')):
            cur += 1
    return cur

with open("day15.txt", 'r') as file:       
    data = {x.split()[1] : int(x.split()[-1]) for x in file.read().splitlines()}
    data2 = {k:v for k,v in data.items()}
    print(calc(data))
    print(calc(data2, a=4, b=8, y=5000000))
