# Create a tuple with different data types
tuple1 = ("tuple", False, 3.2, 1)
print(tuple1)

# Create a tuple
tuple2 = (6, 2, 8, 3)
print(tuple2)

# Tuples are immutable, so you can not add new elements
# Using merge of tuples with the + operator you can add an element
tuple3 = tuple2 + (9,)
print(tuple3)

# Counts the number of occurrences of item 5 from a tuple
tuple1 = (5, 10, 6, 7, 5)
print(tuple1.count(5))

# Create a tuple
tuple4 = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

# use tuple[start:stop] the start index is inclusive and the stop index
# is exclusive
slice = tuple4[3:5]
print(slice)

# if the slice index isn't defined, is taken from the beginning of the tuple
slice = tuple4[:6]
print(slice)