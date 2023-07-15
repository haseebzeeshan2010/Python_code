DISCOUNT_RATE = 10/100
TAX_RATE = 20/100
number_of_units = 1024
cost_per_unit = 0.75

subtotal = number_of_units * cost_per_unit
tax_due = subtotal * TAX_RATE
discount = subtotal*DISCOUNT_RATE
total = (subtotal+tax_due)-discount

print("The discount is",discount)
print("The tax which is due is",tax_due)
print("The total to pay is", total)