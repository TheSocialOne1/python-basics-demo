#!/usr/bin/env python3
# Demonstration of Python variables and data structures

first_name = "Brandon"
last_name = "Watson"
country = "United States"
state = "California"
city = "Long Beach"
age = 42
is_married = False

skills = ["Linux", "Python", "Bash", "C++", "VMware"]

person_info = {
    "first_name": first_name,
    "last_name": last_name,
    "country": country,
    "state": state,
    "city": city
}

print("First name:", first_name)
print("Last name:", last_name)
print("City:", city)
print("Age:", age)
print("Married:", is_married)
print("Skills:", skills)
print("Person info:", person_info)

# Multiple assignment
first_name, last_name, state, age, is_married = "Brandon", "Watson", "California", 30, False

print("\nReassigned:")
print(first_name, last_name, state, age, is_married)

