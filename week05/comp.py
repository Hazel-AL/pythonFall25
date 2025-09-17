#comprehensions
#[expression for item in iterable if condition]
# do expression for each item in iterable if condition is true
evenSquare = {x: x**2 for x in range(11) if x%2 == 0}
print(evenSquare)

#list of cubes for odd numbers in a given range
def cubeOdd(start, end):
    return [x**3 for x in range(start, end) if x%2 != 0]
print(cubeOdd(1, 10))

# function that creates a list of uppercase words longer than three characters
def longUpper(words):
    return [word.upper() for word in words if len(word) > 3]
words = ["Polytechnic", "COP", "oop", "StUdEnT"]
print(longUpper(words))

# return a dict mapping each word to its length
def wordLen(words):
    return {word: len(word) for word in words}
print(wordLen(words))