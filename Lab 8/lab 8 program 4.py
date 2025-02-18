set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
if not set1.isdisjoint(set2):
    common_elements = set1 & set2
    print("Common elements:", common_elements) 
