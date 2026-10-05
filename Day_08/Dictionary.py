# Exercise 1
dog = {}

# Exercise 2
dog['name'] = 'Coco'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

print(dog)


# Exercise 3
student = {
    'first_name': 'Anjana',
    'last_name': ' M Nair',
    'gender': 'Female',
    'age': 18,
    'marital_status': 'Single',
    'skills': ['Python', 'HTML'],
    'country': 'India',
    'city': 'Kochi',
    'address': 'Kerala'
}

# Exercise 4
print(len(student))


# Exercise 5
print(student['skills'])
print(type(student['skills']))


# Exercise 6
student['skills'].append('CSS')
student['skills'].append('GitHub')

print(student['skills'])


# Exercise 7
print(list(student.keys()))


# Exercise 8
print(list(student.values()))


# Exercise 9
print(list(student.items()))


# Exercise 10
del student['marital_status']

print(student)


# Exercise 11
del dog

print(student)
