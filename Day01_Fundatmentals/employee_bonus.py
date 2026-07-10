Sal = int(input("Enter your salary: "))
Bonus = 0
if Sal > 100000:
    Bonus = 20
elif Sal > 50000:
    Bonus = 10
else:
    Bonus = 5

print("Salary: " , Sal , "Bonus: " , Bonus ,"%")

