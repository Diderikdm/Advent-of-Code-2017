with open("C:\\Advent\\2017\\day5.txt", 'r') as file:
    d = [int(x) for x in file.read().splitlines()]
    p2 = False
    for data in [d[:], d[:]]:
        i = 0
        e = 0
        while i in range(len(data)):
            temp = data[i]
            data[i] += -1 if p2 and temp >= 3 else 1
            i += temp
            e += 1
        p2 = True 
        print(e)    
