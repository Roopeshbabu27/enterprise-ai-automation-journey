Basic = int(input("Enter your basic salary: "))
Bonus = int(input("Enter your bonus: "))
Tax = int(input("Enter your tax %: "))
Gross = Basic+Bonus
taxamount = Gross * (Tax / 100)
net = Gross - taxamount 

print(f"Gross Salary: {Gross}" )
print(f"Tax Amount: {taxamount}" )
print(f"Net Salary: {net}" )