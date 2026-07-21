# 2. Enter number of students from user. For those many students accept marks of 5
#    subject marks from user and calculate percentage. Display all percentage and
#    average percentage of students.


n = int(input('Enter Number of Student : '))
total_per = 0 

for i in range(1, n+1):
    print('Enter marks of Student :')
    total = 0 
    
    for j in range(1, 6):
        marks = int(input('Enter Marks of Subject '+ str(j)+':'))
        total = total + marks

    per = total / 5
    print(f'Percentage of Student {i} = {per}%')
    total_per = total_per + per 

average = total_per / n
print(f'Average percentage OF Student {average}%')



