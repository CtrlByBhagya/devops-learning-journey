# Day 3 – Python Functions

## 1. What is a Function?

A function is a reusable block of code that performs a particular task.

Instead of writing the same code repeatedly, we can define a function once and call it whenever required.

Python provides built-in functions such as `print()`, `len()` and `input()`. We can also create our own functions.

**Example:**

```python
def greet():
    print("Hello!")

greet()
```

- `def` is used to define a function.
- `greet` is the function name.
- `greet()` calls the function.
- The indented statement belongs to the function.

## 2. Parameters and Arguments

**Parameters:** Variables written inside the parentheses when defining a function.

**Arguments:** Actual values passed to the function when calling it.

**Example:**

```python
def add(a, b):
    print(a + b)

add(5, 3)
```

- `a` and `b` are parameters.
- `5` and `3` are arguments.
- Output: `8`

## 3. Return Value

The return value is the value that a function sends back when it finishes executing.

We use the `return` statement to return a value.

**Example:**

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:

```text
30
```

**Difference between print and return:**

| print() | return |
|---|---|
| Displays output on the screen. | Sends a value back from the function. |
| Does not return the displayed value as the function result. | Can be stored in a variable and used later. |
| Used to show information. | Used to pass results to other parts of the program. |

A function stops executing when it reaches `return`.

## 4. The end Parameter in print()

By default, `print()` moves to a new line after displaying output.

We can change this behaviour using the `end` parameter.

**Example:**

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

Here, `end=" "` adds a space instead of moving to a new line.

## 5. Local and Global Variables

**Local variable:** A variable created inside a function. It is generally accessible only within that function.

**Global variable:** A variable created outside a function. It can be accessed inside functions.

**Example:**

```python
x = 100  # Global variable

def show():
    y = 20  # Local variable
    print(x)
    print(y)

show()
```

Output:

```text
100
20
```

Important points:

- Function parameters are also local variables.
- A local variable cannot normally be accessed outside its function.
- A function can access a global variable.
- To modify a global variable inside a function, we can use the `global` keyword.

## 6. Passing Lists as Arguments

A list can also be passed to a function as an argument.

**Example:**

```python
def display_items(items):
    for item in items:
        print(item)

fruits = ["Apple", "Banana", "Mango"]

display_items(fruits)
```

Here, `items` is the parameter and `fruits` is the argument.

We can use list indexing and `len()` inside functions to work with list elements.

## 7. Useful String Methods

Python provides built-in string methods that help us check the contents of a string.

| Method | Purpose |
|---|---|
| `isdigit()` | Checks whether all characters are digits. |
| `isalpha()` | Checks whether all characters are alphabets. |
| `isalnum()` | Checks whether all characters are letters or digits. |
| `isupper()` | Checks whether all letters are uppercase. |
| `islower()` | Checks whether all letters are lowercase. |

These methods return either `True` or `False`.

**Example:**

```python
text = "Hello123"

print(text.isalnum())
print(text.isalpha())
```

Output:

```text
True
False
```

## 8. Important Concepts Used in Practice

### Counter Variable

A counter variable keeps track of how many times something happens.

```python
count = 0

for i in range(5):
    count += 1

print(count)
```

Output: `5`

### Modulo Operator (%)

The modulo operator gives the remainder after division.

```python
num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output: `Even`

### Dictionary

A dictionary stores data in key-value pairs.

```python
student = {
    "name": "Bhagyashree",
    "age": 21
}

print(student["name"])
```

Output: `Bhagyashree`

## 9. Functions – Key Takeaways

- Functions make code reusable and organised.
- `def` is used to define a function.
- Calling a function executes its code.
- Parameters are variables in the function definition.
- Arguments are values passed during a function call.
- `return` sends a result back to the caller.
- `print()` displays output.
- Local variables belong to their function.
- Global variables are defined outside functions.
- Lists, strings and dictionaries can be used inside functions.
- Functions can contain loops, conditions and other function calls.