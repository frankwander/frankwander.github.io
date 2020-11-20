
try: 
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit()

try:
    result = x/y
except ZeroDivisionError:
    print("Error: cannot divide by 0.")
    sys.exit()

print(result)