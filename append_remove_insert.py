stats = [48,45,34,78]
print(stats)
stats.append(56)
print(stats)

stats.insert(3,24)
print(stats)

stats.remove(48)
print(stats)

#print(stats.index(67))   67 not in the list
print(stats.index(45))
item = stats.pop()

print(item)
print(stats)

#pop and append behave as a stack (last in first out)
ori = [[1,2],[3,4]]
new_list = ori[:]
new_list[0][0] = 5
print(ori)