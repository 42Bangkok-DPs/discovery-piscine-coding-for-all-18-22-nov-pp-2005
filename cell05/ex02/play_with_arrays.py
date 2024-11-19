ori = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

index=0
while index<len(ori):
    x = ori[index]+2
    if x>5:
        new.append(x)
    index+=1

print(ori)
print(new)
