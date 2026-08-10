# 2. Write a program to calculate simple interest based on Principal, Rate and Time 
# (SI = P*R*T/100)  


p = float(input("Enter Principal Amount : "))
r = float(input("Enter Rate Interest : "))
t = float(input("Enter Time Period : "))

si = (p * r * t) / 100

print("Simple Interest =", si)