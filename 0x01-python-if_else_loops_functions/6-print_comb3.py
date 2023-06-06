for num1 in range(10):
    for num2 in range(num1, 10):
        if num1 != num2:
            print("{:02d}, ".format(num1 * 10 + num2), end="")
print() 
