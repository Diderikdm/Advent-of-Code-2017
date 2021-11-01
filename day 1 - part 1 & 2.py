with open("C:\\Advent\\2017\\day1.txt", 'r') as file:
    data = [int(x) for x in file.read()]
    print(sum(x for e,x in enumerate(data) if data[(e+1)%len(data)] == x))
    print(sum(x for e,x in enumerate(data) if data[(e+len(data)//2)%len(data)] == x))
