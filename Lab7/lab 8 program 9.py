my_tuple = (1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 2)
repeated_items = set(x for x in my_tuple if my_tuple.count(x) > 1)
print(repeated_items)
