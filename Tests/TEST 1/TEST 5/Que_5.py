# 5. Python Program to Find the Union of two Lists without
# using set concept.

L1 = [1, 2, 3, 4, 5]
L2 = [4, 5, 6, 7, 8]

Union = []

for i in L1:
    if i not in Union:
        Union.append(i)

for i in L2:
    if i not in Union:
        Union.append(i)

print("Union =", Union)