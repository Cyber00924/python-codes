s1 = "Hello"
s2 = "World"
if len(s1) < 2 or len(s2) < 2:
 print(s1 + " " + s2)
else:
 print(s2[:2] + s1[2:] + " " + s1[:2] + s2[2:])
