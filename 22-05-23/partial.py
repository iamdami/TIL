from functools import partial


def power(base, exponent):
    return base ** exponent
# print(power(2, 3))  # 8

square = partial(power, exponent = 2)
cube = partial(power, exponent = 3)
print(square(2))
print(cube(3))

# def square(base):
#     return power(base, 2)

# def cube(base):
#     return power(base, 3)

# print(square(2))  # 4
# print(cube(3))  # 27
