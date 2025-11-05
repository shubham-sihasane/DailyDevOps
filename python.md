### ⛵ What is Python?
Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used in web development, data science, automation, artificial intelligence, scientific computing, and more.

#### Key Features of Python
- Easy to learn and use with clear syntax 
- Extensive standard library and third-party packages 
- Cross-platform compatibility 
- Strong community support 
- Ideal for rapid development and prototyping

### ⛵ Background and History

Python was created by Guido van Rossum and first released in 1991. It was designed to emphasize code readability and developer productivity. The language's name was inspired by the British comedy group Monty Python, reflecting van Rossum's desire to make programming fun and approachable.

The first version of Python (0.9.0) included many features that are still present today, such as exception handling, functions, and modules. Over the years, Python has evolved through various versions, with Python 2.x and Python 3.x being the most notable. Python 3 introduced significant improvements and changes, making it the future of the language.

To begin coding in Python, you can install the latest version from the official website (https://www.python.org) and use an interactive shell or an integrated development environment (IDE) like PyCharm, VS Code, or Jupyter Notebook.

`python3 --version` ⌘ Check installed version of Python

`print("Hello, World!")` ⌘ This simple program prints a greeting message to the console.

### ⛵ Comments in Python
Comments are lines in the code that are not executed by the Python interpreter. They are used to explain and document the code, making it easier to understand for anyone reading it, including your future self. Comments help clarify the purpose of code sections, describe logic, and provide additional context.

#### Types of Comments

**Single-line comments:** Start with the # symbol and continue to the end of the line.

`# This is a single-line comment`

`print("Hello, World!")  # This comment is inline with code`

**Multi-line comments:** Can be created using triple quotes (""" or '''). Although technically these are multi-line strings, they are often used as multi-line comments.

`"""
This is a multi-line comment
that spans multiple lines.
"""
print("Hello, World!")`

🏄‍♂️**Best Practices**
- Use comments to explain why the code does something, not what it does.
- Keep comments clear and concise. 
- Avoid obvious comments that do not add value. 
- Update comments when you modify the code to keep them accurate.

### ⛵Python Variables
Variables in Python are used to store data values. A variable acts as a container for data that can be changed during program execution. You do not need to declare the type of variable explicitly; Python infers it based on the assigned value.

**Examples:**

`age = 10`  ⌘ An integer variable
`name = "shubham"`  ⌘ A string variable

#### Variable Naming Rules

- Variable names must start with a letter (a-z, A-Z) or an underscore (_). 
- The rest of the name can contain letters, digits (0-9), or underscores. 
- Variable names are case-sensitive (age and Age are different). 
- Avoid using Python reserved keywords as variable names.

### ⛵ Python Literals
Literals are the fixed values assigned to variables or used directly in the code. They represent data in its simplest form.

**Types of literals in Python include:**

1. **String literals:** Text enclosed in single, double, or triple quotes.

2. **Numeric literals:** Integers (decimal, octal, hexadecimal), floating-point numbers, and complex numbers.

3. **Boolean literals:** True and False.

4. **Special literals:** None represents the absence of a value.

**Examples:**

`name = 'shubham sihasane`  # String literal
`age = 25`  # Integer literal
`price = 19.99`  # Floating-point literal
`is_active = True`  # Boolean literal
`nothing = None`  # Special literal

###  ⛵Python Operators and Their Types
Python operators are special symbols or keywords that perform operations on one or more operands (values or variables). Operators are essential for performing calculations, comparisons, and logical operations in Python programs.

#### Types of Python Operators with Examples

1. **Arithmetic Operators**
Used for mathematical calculations.

Operator

Description

Example

Result

2. Comparison Operators

Used to compare two values and return a Boolean result.

Operator

Description

Example

Result

==

Equal to

5 == 3

False

!=

Not equal to

5 != 3

True

| =

3. Logical Operators

Used to combine conditional statements.

Operator

Description

Example

Result

and

Logical AND

True and False

False

or

Logical OR

True or False

True

not

Logical NOT

not True

False

4. Assignment Operators

Used to assign values to variables.

Operator

Description

Example

Equivalent To

=

Assign

x = 5

x = 5

+=

Add and assign

x += 3

x = x + 3

-=

Subtract and assign

x -= 3

x = x - 3

*=

Multiply and assign

x *= 3

x = x * 3

/=

Divide and assign

x /= 3

x = x / 3

%=

Modulus and assign

x %= 3

x = x % 3

//=

Floor divide and assign

x //= 3

x = x // 3

**=

Exponent and assign

x **= 3

x = x ** 3

5. Bitwise Operators

Operate on bits and perform bit-level operations.

Operator

Description

Example

Result

&

AND

5 & 3

1





OR

5

3

7

^

XOR

5 ^ 3

6

~

NOT

~5

-6

<<

Left shift

5 << 1

10

| >

| Right shift | 5 >> 1 | 2 |

6. Membership Operators

Test if a value is in a sequence (like a list, tuple, or string).

Operator

Description

Example

Result

in

Returns True if value is found in sequence

'a' in 'apple'

True

not in

Returns True if value is not found in sequence

'b' not in 'apple'

True

7. Identity Operators

Compare the memory locations of two objects.

Operator

Description

Example

Result

is

Returns True if both variables point to the same object

x is y

Depends

is not

Returns True if both variables do not point to the same object

x is not y

Depends

Example Usage

x = 10
y = 5

# Arithmetic
print(x + y)  # 15

# Comparison
print(x > y)   # True

# Logical
print(x > 5 and y < 10)  # True

# Assignment
x += 5
print(x)      # 15

# Membership
print('a' in 'apple')  # True

# Identity
z = x
print(x is z)  # True

This section provides a clear overview of Python operators and their types with practical examples to help learners understand their usage.