x = input("Give me a number: ")

try:
    if float(x).is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except:
    print("This number is a decimal.")