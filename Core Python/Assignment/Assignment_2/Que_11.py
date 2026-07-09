# WAP to accept of an integer amount from user and tell menimum number of notes needed for repredenting that amount.

amt = int(input('Enter Amount : '))

tho = amt//2000
amt = amt % 2000

fh = amt//500
amt = amt % 500

th = amt//200
amt = amt % 200

h = amt//100
amt = amt % 100

f = amt//50
amt = amt % 50

t = amt//20
amt = amt % 20

ten = amt//10
amt = amt % 10

total_notes = tho + fh + th + h + f + t + ten
print(total_notes)
