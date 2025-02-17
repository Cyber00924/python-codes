list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
common_member_found = False

for item in list1:
    if item in list2:
        common_member_found = True
        break

print("Do the lists have at least one common member?", common_member_found)
