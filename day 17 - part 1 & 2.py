data = 359
buffer = [0]
i = 0
for x in range(1, 2018):
    i = (i + data) % len(buffer) + 1
    buffer.insert(i, x)
print(buffer[(buffer.index(2017) + 1) % len(buffer)])

for x in range(2018, 50000001):
    i = (i + data) % x + 1
    if i == 1:
        val = x
print(val)
