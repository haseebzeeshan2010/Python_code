# ---------------------------------------------------------
# Constants
# ---------------------------------------------------------
# =====> Create constants for the flat fees





# =====> Create constants for the prices per gram





# ---------------------------------------------------------
# Variables
# ---------------------------------------------------------
# =====> Initialise the two variables to an appropriate value
weight =
totalPrice =
theFee = 0.0            # Keeping the fee for the output
thePrice = 0.0          # Keeping the price per gram for the output

# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

# Get the weight of the package
weight = int (input ("Enter the weight of the package in grams "))

# Check if weight is invalid
# =====> Complete the test to validate the weight
if (weight           ):
    print ("Weight is too small")
# =====> Complete the test to validate the weight
elif (weight         ):
    print ("Weight is too large")
else:
    # Find out the flat fee and the price per gram
    # =====> Complete the test with the correct relational operator
    if (weight      1501):
        # =====> Complete the lines to set the variables
        theFee =
        thePrice =
        # =====> Complete the test with the correct value
    elif (weight >=     ):
        # =====> Complete the lines to set the variables
        theFee =
        thePrice =
        # =====> Complete the test
    elif (               ):
        # =====> Complete the lines to set the variables
        theFee =
        thePrice =
    else:           # Only need else, because already checked weight
        # =====> Complete the lines to set the variables
        theFee =
        thePrice =

    # Calculate the total price
    # =====> Add a line to calculate the total price


    # Report to the user
    print ("Flat fee:", theFee, "Total price: ", totalPrice)