#!/usr/bin/env python3
# functions.py
# Demonstrates basic Python functions: parameters, return values, and simple input validation

# -----------------------------
# Function 1: Add two numbers
# -----------------------------
def add(a, b):
    """Return the sum of a and b."""
    return a + b


# -----------------------------
# Function 2: Check if a number is even
# -----------------------------
def is_even(n):
    """Return True if n is even, otherwise False."""
    return n % 2 == 0


# -----------------------------
# Function 3: Disk alert message (simple decision logic)
# -----------------------------
def disk_status(used_pct, threshold=80):
    """
    Return 'ALERT' if used_pct >= threshold, otherwise 'OK'.
    used_pct and threshold are expected to be integers.
    """
    if used_pct >= threshold:
        return "ALERT"
    return "OK"


# -----------------------------
# Main: Call functions and print results
# -----------------------------
if __name__ == "__main__":
    # Example calls
    print("add(2, 3) =", add(2, 3))
    print("is_even(10) =", is_even(10))
    print("is_even(7) =", is_even(7))

    # Example of default parameter usage
    print("disk_status(55) =", disk_status(55))          # uses default threshold=80
    print("disk_status(85) =", disk_status(85))          # triggers ALERT
    print("disk_status(85, 90) =", disk_status(85, 90))  # custom threshold

