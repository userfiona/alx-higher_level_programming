#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    # Perform calculations
    sum_result = add(a, b)
    difference_result = sub(a, b)
    product_result = mul(a, b)
    quotient_result = div(a, b)

    # Print the results
    print("Sum: {} + {} = {}".format(a, b, sum_result))
    print("Difference: {} - {} = {}".format(a, b, difference_result))
    print("Product: {} * {} = {}".format(a, b, product_result))
    print("Quotient: {} / {} = {:.2f}".format(a, b, quotient_result))
