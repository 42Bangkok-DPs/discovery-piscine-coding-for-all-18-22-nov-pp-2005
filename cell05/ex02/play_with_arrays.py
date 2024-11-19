ori = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

for i in range(len(ori)):
    x = ori[i]+2
    if x>5:
        new.append(x)

print(ori)
print(new)
