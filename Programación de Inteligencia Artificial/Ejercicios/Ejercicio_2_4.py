a, b = 1, 1
list = [a,b]
for i in range(18):
    list.append(list[i] + list[i+1])

print(f"{list}")