x = 1
while x <= 100:
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz")
        x += 1
    elif x % 3 == 0:
        print("Fizz")
        x += 1
    elif x % 5 == 0:
        print("Buzz")
        x += 1
    else:
        print(x)
        x += 1
