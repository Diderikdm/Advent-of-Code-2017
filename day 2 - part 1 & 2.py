with open("C:\\Advent\\2017\\day2.txt", 'r') as file:
    data = [[int(x) for x in y.split() if x] for y in file.read().splitlines()]
    print(sum(max(x) - min(x) for x in data))
    print(sum(sum(sum([[[int(y/z) for z in x[:e] + x[e+1:] if y/z == int(y/z)] for e,y in enumerate(x)] for x in data], []), [])))
