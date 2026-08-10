# 1. Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:


l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
r = float(input("Enter radius of semicircle: "))


area_rect = l * b

area_semicir = (3.14 * r * r) / 2

area = area_rect + area_semicir

perimeter = (2 * l) + b + (3.14 * r)

print("Area =", area)
print("Perimeter =", perimeter)