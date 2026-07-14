# 9. WAP to  input 5 subject mmarks from display grade (eg. first class , second class)

m1 = int (input('Enter Marks of Marathi : '))
m2 = int (input('Enter Marks of English : '))
m3 = int (input('Enter Marks of Science : '))
m4 = int (input('Enter Marks of History : '))
m5 = int (input('Enter Marks of Math : '))

per = (m1+m2+m3+m4+m5/500)*100
per = 65
if(per >= 85 and per<=100):
    print('Grade : first class')
elif(per>=65 and per<85):
    print('Grade : Second class')
elif(per>=35 and per<65):
    print('Grade : Third Class')
else:
    print('Fail.')