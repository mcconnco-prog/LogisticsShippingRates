# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kgs: ))
rate = float(input("Enter the shipping rate per kgs: ))

## Perform Calculation
shipping_cost = weight * rate

## Display total
print(f"Shipping Cost is {shipping_cost} USD")
