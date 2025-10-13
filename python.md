### 🐯 What is Python?
Python is a versatile, high-level programming language known for its simplicity and readability. It was created by Guido van Rossum in the late 1980s and officially released in 1991. Python is widely used across various domains due to its flexibility and ease of use. Here's a quick overview:

### 🐯 Key Features:
1. Readable Syntax: Python's syntax is clean and easy to understand, making it beginner-friendly. 
2. Multi-Paradigm: It supports multiple programming paradigms, including object-oriented, procedural, and functional programming. 
3. Cross-Platform: Python runs on various platforms like Windows, macOS, Linux, etc. 
4. Extensive Libraries: It has a rich standard library and a vast ecosystem of third-party libraries for tasks like web development, data analysis, machine learning, and more.

### 🐯 Common Uses:

1. Web Development: Frameworks like Django and Flask. 
2. Data Science & Machine Learning: Libraries like Pandas, NumPy, and TensorFlow. 
3. Automation & Scripting: Automating repetitive tasks. 
4. Game Development: Libraries like Pygame. 
5. Software Prototyping: Rapid application development.

Python's versatility and community support make it a go-to language for both beginners and professionals.

### 🐯 Python in Action
There are two main ways we can run python code.

**1. Command Prompt Based** - Interactively
In interactive mode, any code you write get executed immediately. Python executes each line as you enter it and then displays the output.

**2. File Based** - Non Interactively
In non-interactive mode, the code only gets executed it's explicitly instructed.

### 🐯 Python Comments
1. Python will ignore any lines starting with `#` symbol.
2. `''' '''` OR `""" """` Multiline comments but technically they are empty strings.

### 🐯 Python Basic Data Types
Python provides several built-in data types to handle different kinds of data. Here’s a quick overview:

**1. Numeric Types**

✅ int: Represents integers, whole numbers only, no decimal points, positive or negative (e.g., 5, -10, 0).
✅ float: Represents floating-point numbers, with decimal points, positive or negative (e.g., 3.14, -2.5).
✅ complex: Represents complex numbers (e.g., 3+4j).

**2. Sequence Types**

✅ str: Represents strings, a sequence of characters (e.g., "Hello", 'Python').
✅ list: Represents an ordered, mutable collection (e.g., [1, 2, 3], ['a', 'b', 'c']).
✅ tuple: Represents an ordered, immutable collection (e.g., (1, 2, 3), ('x', 'y', 'z')).

**3. Mapping Type**

✅ dict: Represents key-value pairs (e.g., {'name': 'Alice', 'age': 25}).

**4. Set Types**

✅ set: Represents an unordered collection of unique elements (e.g., {1, 2, 3}).
✅ frozenset: Immutable version of a set.

**5. Boolean Type**

✅ bool: Represents True or False.

**6. Binary Types**

✅ bytes: Represents immutable sequences of bytes (e.g., b'hello').
✅ bytearray: Mutable version of bytes.
✅ memoryview: Provides memory access to binary data.

**7. None Type**

✅ None: Represents the absence of a value (e.g., None).

These data types allow Python to handle a wide variety of data efficiently and flexibly.

### 🐯 Python Operators
Operators in Python are special symbols or keywords used to perform operations on variables and values also known as Operands. They allow you to manipulate data and perform computations. Operators are categorized based on the type of operation they perform. Here's a quick overview:

✅ () : Parentheses gets highest priority

**1. Arithmetic Operators**
Used for basic mathematical operations:

✅ + : Addition (e.g., 5 + 3 = 8)

✅ - : Subtraction (e.g., 5 - 3 = 2)

✅ * : Multiplication (e.g., 5 * 3 = 15)

✅ / : Division (e.g., 5 / 2 = 2.5)

✅ // : Floor/Integer Division (e.g., 5 // 2 = 2)

✅ % : Modulus (remainder, e.g., 5 % 2 = 1)

✅ ** : Exponentiation (e.g., 2 ** 3 = 8)

**2. Assignment Operators**
Used to assign values to variables:

✅ = : Assign (e.g., x = 5)

✅ += : Add and assign (e.g., x += 3 is equivalent to x = x + 3)

✅ -= : Subtract and assign

✅ *= : Multiply and assign

✅ /= : Divide and assign

✅ //= : Floor divide and assign

✅ %= : Modulus and assign

✅ **= : Exponentiation and assign

**3. Comparison Operators**
Used to compare two values and return a Boolean (True or False):

✅ == : Equal to

✅ != : Not equal to

✅ > : Greater than

✅ < : Less than

✅ >= : Greater than or equal to

✅ <= : Less than or equal to

**4. Logical Operators**
Used to combine conditional statements:

✅ and : Returns True if both conditions are true
✅ or : Returns True if at least one condition is true
✅ not : Reverses the Boolean value

**5. Bitwise Operators**
Operate on binary representations of numbers:

✅ & : AND

✅ | : OR

✅ ^ : XOR

✅ ~ : NOT

✅ << : Left shift

✅ >> : Right shift

**6. Identity Operators**
Used to compare memory locations of two objects:

✅ is : Returns True if both variables point to the same object
✅ is not : Returns True if they point to different objects

**7. Membership Operators**
Used to check if a value is in a sequence (like a list, tuple, or string):

✅ in : Returns True if the value exists in the sequence
✅ not in : Returns True if the value does not exist in the sequence

**8. Special Operators**

✅ Ternary Operator: Conditional expressions (e.g., x = a if condition else b)
✅ Operator Overloading: Customizing the behavior of operators for user-defined classes.

Python operators are intuitive and versatile, making them essential for writing efficient and readable code!

### 🐯 Python Variables
Python Variables are containers used to store data values. They are fundamental building blocks in Python programming, allowing you to work with and manipulate data efficiently. Here's a concise overview:
Key Features of Python Variables:

1. **Dynamic Typing:** Python variables are dynamically typed, meaning you don't need to declare their type explicitly. The type is inferred based on the value assigned.

```
x = 10       # Integer
y = "Hello"  # String
z = 3.14     # Float
```

**2. No Declaration Required:** A variable is created the moment you assign a value to it. There's no need for a separate declaration step.

```
name = "Alice"
age = 25
```

**3. Type Flexibility:** Variables can change their type during execution.

```
x = 5       # Initially an integer
x = "Five"  # Now a string
```

**4. Multiple Assignments:** You can assign values to multiple variables in a single line.
```
a, b, c = 1, 2, 3
```

**5. Case Sensitivity:** Variable names are case-sensitive.
```
var = 10
Var = 20  # Different variable
```

**5. Naming Rules:** Must start with a letter or an underscore (_). Cannot start with a number.  Can only contain alphanumeric characters and underscores. Cannot use reserved keywords (e.g., if, while, class).

```
name = "John"
age = 30
height = 5.9
```

```
print(name)  # Output: John
print(age)   # Output: 30
print(height)  # Output: 5.9
```

Python variables are simple yet powerful, making them an essential part of writing clean and effective code.


