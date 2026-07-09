# WAP to calculate selling price of book based on cost price and discount.

cp = int (input('Enter Cost Price : '))
d = float(input('Enter Discount : '))/100

sp = cp - (cp * d)

print(f'Selling Price : {sp}')