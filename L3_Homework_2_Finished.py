
# Set constants
# =====> Create a constant named DISCOUNT and set it to 0.15

DISCOUNT = 0.15

# Set variables
# =====> Create variables for the number of pens, pencils, and scissors
# =====> Set the variables to 44, 24, and 3, respectively

pens = 44
pencils = 24
scissors = 3

# =====> Create variables for the cost of each pens, pencils, and scissors
# =====> Set the variables to 0.55, 0.23, and 1.38, respectively

pens_cost = 0.55
pencils_cost = 0.23
scissors_cost = 1.38

# Calculate
# =====> Calculate the total cost of all the items

totalcost_pens = pens * pens_cost
totalcost_pencils = pencils * pencils_cost
totalcost_scissors = scissors * scissors_cost
sum_of_costs = totalcost_pens + totalcost_pencils + totalcost_scissors
# =====> Calculate the mean cost of all the items
sum_of_items = pens+pencils+scissors

mean_cost = sum_of_costs/sum_of_items


# =====> Calculate the value of the discount to be applied

discount = sum_of_costs * DISCOUNT



# =====> Calculate the total to pay and round to two decimal places

with_discount = sum_of_costs - discount
total = round(with_discount,2)

# Display the results
# =====> Display the total cost, the mean cost, the value of
#        the discount, and the amount to pay, each on a separate
#        line, with an informative text message

print("The total cost is",sum_of_costs)
print("The mean cost is", mean_cost)
print("The discount is" , discount)
print("To pay is",total)