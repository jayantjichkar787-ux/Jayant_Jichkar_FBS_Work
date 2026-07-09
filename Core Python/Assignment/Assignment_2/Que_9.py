# WAP to swap two numbers without using third variable

x = 10 
y = 20 
print(f'before swaping x={x} & y={y}')

x = x + y  # x become 30 = 10 + 20
y = x - y  # y become 10 = 30 - 20
x = x - y  # x become 20 = 30 - 10


print(f'After swaping x={x} & y={y}')