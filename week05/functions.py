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

# capitalize the words
words = ["python", "c", "java"]
words2 = list(map(str.upper, words))
print(words2)

#take away whitespace at the beginning and end
texts = [" Hello World  ", " Python  Programming", "  Data Science   "]
lambda s: ' '.join(s.split())
texts = list(map(lambda s: ' '.join(s.split()), texts))
print(texts)

# filter() even numbers
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x%2 == 0, numbers))
result = list(map(lambda x: x**2, filter(lambda x: x%2 == 0, numbers)))
print(even)
print(result)

#comprehensions
#[expression for item in iterable if condition]
# do expression for each item in iterable if condition is true
evenSquare = {x: x**2 for x in range(11) if x%2 == 0}
print(evenSquare)