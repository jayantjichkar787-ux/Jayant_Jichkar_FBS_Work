# 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter amount: "))

for note in D:
    count = amount // note

    if count > 0:
        print(note, ":", count)
        amount = amount % note

if amount != 0:
    print("Remaining amount:", amount)