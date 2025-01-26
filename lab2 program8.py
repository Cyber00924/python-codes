a = 1
b = 1
print(a, b, end=" ")
for i in range(5):
    next_num = a + b
    print(next_num, end=" ")
    a = b
    b = next_num
