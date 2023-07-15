# ---------------------------------------------------------
# Constants
# ---------------------------------------------------------
# =====> Create constants for the flat fees

FLAT_FEES_10_500 = 1
FLAT_FEES_501_1000 = 1.5
FLAT_FEES_1001_1500 = 2
FLAT_FEES_1501_5000 = 2.5



# =====> Create constants for the prices per gram

PRICE_PER_GRAM_10_500 = 0.385
PRICE_PER_GRAM_501_1000 = 0.278
PRICE_PER_GRAM_1001_1500 = 0.600
PRICE_PER_GRAM_1501_5000 = 0.450



# ---------------------------------------------------------
# Variables
# ---------------------------------------------------------
# =====> Initialise the two variables to an appropriate value
weight = 0
totalPrice = 0
theFee = 0.0            # Keeping the fee for the output
thePrice = 0.0          # Keeping the price per gram for the output

# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

# Get the weight of the package
weight = int (input ("Enter the weight of the package in grams "))

# Check if weight is invalid
# =====> Complete the test to validate the weight
if (weight<10):
    print ("Weight is too small")
# =====> Complete the test to validate the weight
elif (weight>5000):
    print ("Weight is too large")
else:
    # Find out the flat fee and the price per gram
    # =====> Complete the test with the correct relational operator
    if (weight>=1501):
        # =====> Complete the lines to set the variables
        theFee = FLAT_FEES_1501_5000
        thePrice = PRICE_PER_GRAM_1501_5000
        # =====> Complete the test with the correct value
    elif (weight >= 1001):
        # =====> Complete the lines to set the variables
        theFee = FLAT_FEES_1001_1500
        thePrice = PRICE_PER_GRAM_1001_1500
        # =====> Complete the test
    elif (weight >= 501):
        # =====> Complete the lines to set the variables
        theFee = FLAT_FEES_501_1000
        thePrice = PRICE_PER_GRAM_501_1000
    else:           # Only need else, because already checked weight
        # =====> Complete the lines to set the variables
        theFee = FLAT_FEES_10_500
        thePrice = PRICE_PER_GRAM_10_500

    # Calculate the total price
    # =====> Add a line to calculate the total price
    totalPrice = weight*thePrice+theFee

    # Report to the user
    print ("Flat fee:", theFee, "Total price: ", totalPrice)
