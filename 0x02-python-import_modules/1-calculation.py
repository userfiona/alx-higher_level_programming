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
    print("Sum: {:d} + {:d} = {:d}".format(a, b, sum_result))
    print("Difference: {:d} - {:d} = {:d}".format(a, b, difference_result))
    print("Product: {:d} * {:d} = {:d}".format(a, b, product_result))
    print("Quotient: {:d} / {:d} = {:d}".format(a, b, quotient_result))
