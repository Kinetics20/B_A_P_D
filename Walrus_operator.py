# The walrus operator := in Python allows you to assign a value to a variable as part of an expression.
# This can make your code more concise and readable by reducing the need for separate assignment statements.
# It was introduced in Python 3.8.
#
# Here are some examples to illustrate its use:
#
#     Using the walrus operator in an if statement:
#
#     Without the walrus operator:

# 1/ Using the walrus operator in an if statement:
#
# Without the walrus operator:

n = len(my_list)
if n > 10:
    print(f"List has {n} elements.")

# With the walrus operator:

if (n := len(my_list)) > 10:
    print(f"List has {n} elements.")

# 2/ Using the walrus operator in a while loop:
#
# Without the walrus operator:

line = file.readline()
while line != '':
    print(line)
    line = file.readline()

# With the walrus operator:

while (line := file.readline()) != '':
    print(line)

# 3/ Using the walrus operator in a list comprehension:
#
# Without the walrus operator:

results = []
for x in data:
    y = process(x)
    if y is not None:
        results.append(y)

# With the walrus operator:

results = [y for x in data if (y := process(x)) is not None]

# 4/ Using the walrus operator in a for loop with condition:

# Without the walrus operator:

values = [1, 2, 3, 4, 5]
for value in values:
    square = value ** 2
    if square > 10:
        print(f"Square of {value} is {square}")

# With the walrus operator:

values = [1, 2, 3, 4, 5]
for value in values:
    if (square := value ** 2) > 10:
        print(f"Square of {value} is {square}")


# 5/Using the walrus operator in a function definition:

# While the walrus operator can be used in various expressions within a function, it is not typically used directly
# in the return statement for simple conditions. However, for more complex logic, it can be useful:
#
# Without the walrus operator:

def process(data):
    result = compute(data)
    if result is not None:
        return result
    return None


# With the walrus operator:

def process(data):
    if (result := compute(data)) is not None:
        return result
    return None

# The walrus operator can significantly improve the readability and conciseness of your code,
# especially when dealing with complex conditions or repeated computations.

if (n := len(my_list)) > 10:
    print(f"Lista ma {n} elementów")

while (line := file.readline()) != '':
    print(line)

nums = [1, 2, 3, 4, 5]
squared_even_nums = [y := x**2 for x in nums if (y := x**2) % 2 == 0]
print(squared_even_nums)
