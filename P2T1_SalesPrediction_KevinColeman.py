# This program predicts the profit the will be made from the user's projected sales.
# 9/27/18
# CTI-110 P2T1 - Sales Prediction  
# Kevin Coleman
#

# Input the total sales.

totalSales = float(input("Enter your projected total sales: "))

# Calculate the profit as 23 percent of total sales.

profit = totalSales * .23

# Display the profit.

print ("The profit is $", format(profit, '.2f'))
