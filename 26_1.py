f = open('26.txt')
zakazy = [int(x) for x in f]
k = len(zakazy)
sum = 0
for i in range(k):
    sum += zakazy[i]
srz = sum /k
srn = sum / 4
print(int(srz), int(srn))