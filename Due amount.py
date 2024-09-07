def dueAmount(b , g):
    return g - b
    
bill = int(input("Enter the bill: "))
given =int(input("Enter the given amount: "))

due = dueAmount(bill , given)
print(f"Bill: {bill}\nGiven: {given}\nDue Amount= {due}")