f = open('26.txt')
zakazy = [int(x) for x in f]
k = len(zakazy)
kd = k // 4
minz = sorted(zakazy)
mins = 0
for i in range(kd):
    mins += minz[i]
minsnn = sum(minz) - mins + mins * 1.2
maxsx = (sum(minz) - mins) * 1.2 + mins
maxz = sorted(zakazy, reverse=True)
maxs = 0
for i in range(kd):
    maxs += maxz[i]
maxsnn = sum(maxz) - maxs + maxs * 1.2
minsx = (sum(maxz) - maxs) * 1.2 + maxs
print(int(maxsnn + maxsx), int(minsnn + minsx))




