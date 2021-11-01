with open("C:\\Advent\\2017\\day4.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    print(sum(1 for x in data if all(x.count(y) == 1 for y in x.split())))
    print(sum(1 for x in data if all([''.join(sorted(z)) for z in x.split()].count(''.join(sorted(y))) == 1 for y in x.split())))
