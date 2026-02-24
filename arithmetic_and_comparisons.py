#!/usr/bin/env python3
# arithmetic_and_comparisons.py
# Demonstrates arithmetic operations and comparison logic in Python

# -----------------------------
# Basic Arithmetic Operations
# -----------------------------

a = 3  # integer value
b = 2  # integer value

print("Addition:", a + b)          # Adds a and b
print("Subtraction:", a - b)       # Subtracts b from a
print("Multiplication:", a * b)    # Multiplies a and b
print("Division:", a / b)          # Regular division (returns float)
print("Floor Division:", a // b)   # Integer division (no decimal)
print("Modulus:", a % b)           # Remainder of division
print("Exponent:", a ** b)         # a raised to the power of b

print("\n--- Area Calculations ---")

# -----------------------------
# Area Calculations
# -----------------------------

# Area of a circle formula: πr²
radius = 10
area_of_circle = 3.14 * radius ** 2
print("Area of circle:", area_of_circle)

# Area of a rectangle formula: length × width
length = 10
width = 20
area_of_rectangle = length * width
print("Area of rectangle:", area_of_rectangle)

print("\n--- Boolean Comparisons ---")

# -----------------------------
# Comparison Operators
# -----------------------------

print("3 > 2:", 3 > 2)                  # Greater than
print("3 == 2:", 3 == 2)                # Equality check
print("3 != 2:", 3 != 2)                # Not equal
print("3 > 2 and 4 > 3:", 3 > 2 and 4 > 3)  # Logical AND
print("3 > 2 or 4 < 3:", 3 > 2 or 4 < 3)    # Logical OR
print("not True:", not True)            # Logical NOT

print("\n--- String Comparison ---")

# -----------------------------
# String and Length Comparison
# -----------------------------

print("Length comparison:", len("python") > len("dragon"))
print("'coding' in 'coding for all':", "coding" in "coding for all")

