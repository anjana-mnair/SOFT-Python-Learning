#===========================================================================
# Exercises: Level 1
#===========================================================================
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once
it_companies.update(['Intel', 'Netflix', 'Adobe'])
print(it_companies)

# 4. Remove one company
it_companies.remove('IBM')
print(it_companies)

# 5. Difference between remove and discard
# remove() gives an error if the item does not exist.
# discard() does not give an error if the item does not exist
#==================================================================================
#EXERCISE: LEVEL 2
#==================================================================================
# Exercises: Level 2

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 1. Join A and B
print(A.union(B))

# 2. Find A intersection B
print(A.intersection(B))

# 3. Is A a subset of B?
print(A.issubset(B))

# 4. Are A and B disjoint sets?
print(A.isdisjoint(B))

# 5. Join A with B and B with A
print(A.union(B))
print(B.union(A))

# 6. Symmetric difference between A and B
print(A.symmetric_difference(B))

# 7. Delete the sets completely
del A
del B
#=============================================================================
#EXERCISE: LEVEL 3
#=============================================================================
# 1. Compare the length of the list and set

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages_set = set(ages)

print("Length of ages list:", len(ages))
print("Length of ages set:", len(ages_set))

# 2. Difference between string, list, tuple and set

# String: collection of characters
# List: ordered and changeable collection
# Tuple: ordered and unchangeable collection
# Set: unordered collection of unique items

# 3. Unique words in the sentence

sentence = "I am a teacher and I love to inspire and teach people."

words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
len(unique_words)
