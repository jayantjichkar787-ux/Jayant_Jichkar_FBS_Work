# WAP calculate total salary of an Employee abseed on basic da =10% , ta = 12%, hra = 15% 0f basic salary

BS = int(input('Enter Basic Salary : '))

da = BS * 0.10
ta = BS * 0.12
hra = BS* 0.15
Total_S = BS + da + ta + hra
print(f'Total Salary : {Total_S}')