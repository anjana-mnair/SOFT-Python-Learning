#Day 2:30 Days Of Python Programming
# Declare individual variables with values
first_name = 'Anjana'
last_name = 'mnair'
full_name = 'Anjana mnair'
country = 'India'
city = 'kochi'
age = 17
year = 2026
is_married = False
is_true = True
is_light_on = True
#declare multiple variables on one line'
job,skills,hobby = 'student',['python','vscode'],'coding'
print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)
print(job)
print(skills)
print(hobby)


#==================================================================================
#EXECISES:LEVEL 2
#=================================================================================
print("\n------LEVEL 2 Data Types Checking---")
# check the data type using type()
print("first_name data type:",type(first_name))
print("age data type:",type(age))
print("skills data type:",type(skills))
print("\n---Length & Comparison---")
#use len() to find lengths
first_name_len  = len(first_name)
last_name_len = len(last_name)
print("Length of first_name:",first_name_len)
print("Is first name longer than last name?",first_name_len > last_name_len)
print("\n---Arithmetic operations---")
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print("Total:",total)
print("Difference:",diff)
print("Product:",product)
print("Division:",division)
print("Remainder:",remainder)
print("power:",exp)
print("Floor Division:",floor_division)
print("\n---Circle Calculations---")
pi=3.14
radius = 30
area_of_circle = pi *( radius ** 2)
circum_of_circle = 2 * pi * radius
print("Area of Circle:",area_of_circle)
print("Circumference:",circum_of_circle)
#6.take radius as user input and calculate area
print("\n---User Input circle calculations---")
user_radius = float(input("Enter the radius: "))
user_area= pi * (user_radius ** 2)
print("Area  with your radius:",user_area)
#7.get user profile data using input() 
print("\n---Dynamic User Profile---")
user_first= input("Enter your first name: ")
user_last = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")
print(f"Profile saved: {user_first} {user_last}from {user_country}, Age:{user_age} ")
#8.Check Python reserved keywords
print("\n---Python Keywords---")
help('keywords')