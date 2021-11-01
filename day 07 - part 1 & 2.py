def find_weakness(current, diff = None, val = None):
    weights_of_stacks = [data[x]['Weight'] + (sum(find_weakness(x)) if len(data[x]['Disks']) else 0) for x in data[current]['Disks']]
    wrong = next(iter(x for x in weights_of_stacks if weights_of_stacks.count(x) == 1), None)
    if wrong:
        diff = next(iter(x for x in weights_of_stacks if x != wrong), None) - wrong
        find_weakness(data[current]['Disks'][weights_of_stacks.index(wrong)], diff, data[data[current]['Disks'][weights_of_stacks.index(wrong)]]['Weight'])
    if diff and len(set(weights_of_stacks)) == 1 and not(p2):
        p2.append(val + diff)
    return weights_of_stacks

    
with open("C:\\Advent\\2017\\day7.txt", 'r') as file:
    data = {x.split()[0] : {'Weight' : int(x.split()[1].strip('(').strip(')')), 'Disks' : [y.strip(',') for y in x.split()[3:]]} for x in file.read().splitlines()}
    current = next(iter(k for k,v in data.items() if k not in sum([x['Disks'] for x in data.values()], [])), None)
    print(current)
    p2 = []
    find_weakness(current)
    print(p2[0])
