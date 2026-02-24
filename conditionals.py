#!/usr/bin/env python3
# conditionals.py
# Demonstrates if / elif / else logic and boolean conditions in Python

# -----------------------------
# Basic Conditional Logic
# -----------------------------

age = 42
is_employed = True

print("Age:", age)
print("Employed:", is_employed)

# Determine age category
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# -----------------------------
# Boolean Logic with AND / OR
# -----------------------------

# Check eligibility condition
if age >= 18 and is_employed:
    print("Eligible for benefits.")
else:
    print("Not eligible for benefits.")

# -----------------------------
# Comparison Examples
# -----------------------------

temperature = 75

if temperature > 80:
    print("It's hot outside.")
elif temperature > 60:
    print("Weather is moderate.")
else:
    print("It's cold outside.")

