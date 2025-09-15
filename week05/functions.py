# lambda functions:
greet = lambda name: print(f"Hello {name}!")
greet("Billy")

# implement addition, subtraction, multiplication, and division with lambda
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Error: Division by zero!"
# test all
inputs = [(10, 5), (8, 0), (14, 6)]
for x, y in inputs:
    print(f"Inputs: {x}, {y}")
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")
    print(f"Multiply: {multiply(x, y)}")
    print(f"Divide: {divide(x, y)}")
    print()