# Receipt program for Lovely Loveseats for Neat Suites on Fleet Street using Python

# Items with their respective description block
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# Item prices block
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

# Sales tax variable
sales_tax = .088

# Customer/Sales tracking and calculations block
# Customer Itemization and Price
customer_one_total = 0
customer_one_itemization = ""
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Customer Sales tax calculations
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Displaying the receipt
# Items and their descriptions
print("Customer One Items: " + customer_one_itemization)

# Total cost of all items, plus sales tax
print("Customer One Total: ", "${:.2f}".format(customer_one_total))
