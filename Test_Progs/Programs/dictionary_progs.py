d1 = {575: "Apple", 876: "Mango", 132: "Grapes", 782: "Banana"}
d2 = {'a': 10, 'b': 9, 'c': 15, 'd': 2, 'e': 32,'f':0}

# print(d1.items())
print(d1.keys())
print(d1.values())
print(sorted(d1.keys()))
print(sorted(d1.values()))

d4={'a': 10, 'b': 9, 'c': 15, 'd': 2, 'e': 32}
sum=0
for i in d4:
    # print(i)
    sum=sum+d4[i]
print(sum)