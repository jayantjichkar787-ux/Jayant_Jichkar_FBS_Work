# Convert time entered in hours, min, and sec into seconds.

h = int(input('Enter Hours : '))
m = int(input('Enter Minutes : '))
s = int(input('Enter Seconds : '))

sec = h*3600 + m*60 + s

print(f'Total Seconds {sec}.')