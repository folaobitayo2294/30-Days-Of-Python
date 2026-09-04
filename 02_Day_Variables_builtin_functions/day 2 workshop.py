"""Day 2 workshop"""

#Level 1
first_name = "Ben"
last_name = "Smith"
full_name = "Ben Smith"
country = "England"
city = "Essex"
age = 50
year = 2026
is_married = True
is_true = True
is_light = False
a, b, c = 1, 2, 3

#Level 2
#question 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(a, b, c))

#3
print(len(first_name))
len_firstName = len(first_name)
len_lastName = len(last_name)
if (len_firstName < len_lastName):
  print("first name has less char than the last name. ")
else:
  print("last name has less char than the first name. ")

num_one = 5
num_two = 4
total = num_one + num_two
difference = num_one - num_two
product = num_one * num_two
division = num_one / num_two
modulus = num_one % num_two
exponent = (num_one)^num_two
floor_division = num_one // num_two
#q12
radius = 30
#i
area = 3.142 * (radius^2)
circumference = 2 * 3.142 * radius
rad = input("What is the radius")
Area = 3.142 * (rad^2)


