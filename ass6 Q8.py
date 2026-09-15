list =[10, -5, 20, -8, 30, -2, 15]
positive = 0
negetive = 0
for i in list:
    if i>0:
        positive +=1
    elif i<0:
        negetive +=1
print("Positive numbers:", positive)
print("Negetive numbers:", negetive)
