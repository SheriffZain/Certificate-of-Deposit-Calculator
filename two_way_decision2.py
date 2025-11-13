# Calculate the ending balance of a 1-year certificate of deposit (2 rates)
 
# Prompt for the initial investment
invest = float(input("Please enter investment amount: "))
 
# Determine the interest rate, depending on the size of the investment
if invest >= 1000:
    interest_rate = 3.25
else:
    interest_rate = 3.0
 
# Calculate the ending balance
end_balance = invest * (1 + interest_rate / 100)
 
# Display the result
print("Interest rate =", interest_rate, "%")
print("Ending balance = $", end_balance)