sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result_list = []
for i in range(len(sample_list)):
    if i != 0 and i != 4 and i != 5:
        result_list.append(sample_list[i])
print("Expected Output:", result_list)
