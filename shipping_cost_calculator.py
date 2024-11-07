# shipping cost calculator

## Input package weight and shipping rate 
weight = float (input("Enter the package weight in kilograms : "))
rate = float (input ( "Enter the shipping rate per kilogram : "))

## calculate shipping cost 
shipping_cost = weight * rate 

## Display the result 
print (f"shipping cost : {shipping_cost} USD ")
