file = open("input.txt", "r")
lst1 = []
lst2 = []
result = 0

for line in file:
    data = line.strip().split("   ")
    lst1.append(int(data[0]))
    lst2.append(int(data[1]))

lst1.sort()
lst2.sort()

for i in range(len(lst1)):
    result += abs(lst1[i] - lst2[i])

print(result)

result = 0
for num in lst1:
    result += lst2.count(num)*num
print(result)