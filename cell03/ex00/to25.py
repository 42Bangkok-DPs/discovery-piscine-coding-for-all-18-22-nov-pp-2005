num = int(input())

if num <= 25:
    for i in range(num,26,1):
        print(f"Inside the loop, my variable is {i}")
else:
    print("Error")