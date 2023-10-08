# Import daily sales data from the text file
with open('daily_sales.txt', 'r') as file:
    daily_sales = file.read().strip()


#------------------------------------------------

# Initialize a variable to hold the raw daily sales data.
daily_sales_replaced = daily_sales.replace(";,;","+")


# Initialize a variable to hold the raw daily sales data.
daily_transactions = daily_sales_replaced.split(",")


daily_transactions_split = []

# Loop to iterate through data or perform repeated operations.
for transaction in daily_transactions:
  daily_transactions_split.append(transaction.split("+"))


transactions_clean = []
# Loop to iterate through data or perform repeated operations.
for transaction in daily_transactions_split:
# Loop to iterate through data or perform repeated operations.
  transactions_clean.append([item.strip() for item in transaction])


customers = []
sales = []
thread_sold = []


# Loop to iterate through data or perform repeated operations.
for transaction in transactions_clean:
  customers.append(transaction[0])
  sales.append(transaction[1])
  thread_sold.append(transaction[2])


total_sales = 0

new_sales = []

# Loop to iterate through data or perform repeated operations.
for item in sales:
    item = item.replace("$", "")  # remove the dollar sign
    new_sales.append(item)
    total_sales += float(item)  # convert to float and add to 


thread_sold_split= []

# Loop to iterate through data or perform repeated operations.
for sale in thread_sold:
# Loop to iterate through data or perform repeated operations.
  for color in sale.split("&"):
    thread_sold_split.append(color)



# Define a function to perform a specific operation.
def color_count(color):
    count = 0
# Loop to iterate through data or perform repeated operations.
    for item in thread_sold_split:
# Conditional statements to handle different scenarios.
        if item == color:
            count += 1
# Return the result from the function.
    return count



colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']
# Iterate through the list of colors, calculating and displaying the sales count for each color using the `color_count` function.
for color in colors:
  print("Thread Shed sold {} threads of {} thread today.".format(color_count(color), color))

