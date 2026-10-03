#=========================================================================================
# EXERCISE: LEVEL 1
#=========================================================================================

# 1. Create an empty tuple
empty_tuple = ()
print(empty_tuple)

# 2. Create a tuple of sisters and brothers
sisters = ('Jaya', 'lakshmi')
brothers = ('Aromal', 'Adwaith')

# 3. Join brothers and sisters
siblings = brothers + sisters
print(siblings)

# 4. How many siblings do you have?
print("Number of siblings:", len(siblings))

# 5. Add father and mother to create family_members
family_members = siblings + ('Father', 'Mother')
print(family_members)

#==========================================================================================
#EXERCISE: LEVEL 2
#==========================================================================================
# 1. Unpack siblings and parents from family_members
siblings = family_members[:-2]
parents = family_members[-2:]

print("Siblings:", siblings)
print("Parents:", parents)

# 2. Create fruits, vegetables and animal products tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage')
animal_products = ('milk', 'meat', 'butter')

# Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change food_stuff_tp tuple to a list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items
middle = len(food_stuff_lt) // 2

if len(food_stuff_lt) % 2 == 0:
    print(food_stuff_lt[middle - 1:middle + 1])
else:
    print(food_stuff_lt[middle])

# 5. Slice out the first three and last three items
print("First three:", food_stuff_lt[:3])
print("Last three:", food_stuff_lt[-3:])
# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)