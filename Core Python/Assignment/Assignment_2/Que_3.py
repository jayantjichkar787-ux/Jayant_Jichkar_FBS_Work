# Convert Distance given in feet and inches into meter and centimeter

f = int(input('Enetr Feet : '))
i = int(input('Enetr Inches : '))

inches = f * 12 + i  # (feet*12+inches)
cm = inches * 2.54

meters = int(cm//100)
centimeter = cm % 100

print(f'Distance is {meters} Meters & {centimeter} Centimeter.')
