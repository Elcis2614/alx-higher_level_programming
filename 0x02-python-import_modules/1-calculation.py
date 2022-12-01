#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    print("{x} + {y} = {z}".format(x=a, y=b, z=calc.add(a, b)))
    print("{x} - {y} = {z}".format(x=a, y=b, z=calc.sub(a, b)))
    print("{x} * {y} = {z}".format(x=a, y=b, z=calc.mul(a, b)))
    print("{x} / {y} = {z}".format(x=a, y=b, z=calc.div(a, b)))
