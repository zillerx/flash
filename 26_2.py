f = open('26.txt')
zakazy = [int(x) for x in f]
k = len(zakazy)
kd = k // 4
minz = sorted(zakazy)
mins = 0
for i in range(kd):
    mins += minz[i]

mins = sum(minz) - mins + mins * 1.2
maxz = sorted(zakazy, reverse=True)
maxs = 0
for i in range(kd):
    maxs += maxz[i]

maxs = sum(maxz) - maxs + maxs * 1.2
print(int(maxs), int(mins)) 