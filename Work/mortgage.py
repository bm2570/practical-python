# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month=0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month>=extra_payment_start_month and month<=extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print (month, round(principal,2),round(total_paid,2))
    month+=1
    if principal<0:
        overpayment=principal
       # print overpayment

print(f"overpayment is {overpayment:0.2f}")
newpayment=total_paid-overpayment
print(f"total paid is therefore {newpayment:0.2f}")
print(f"Month: {month}")

