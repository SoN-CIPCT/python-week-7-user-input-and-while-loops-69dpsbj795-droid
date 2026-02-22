# List of pizza orders
pizza_orders = ["Pepperoni", "Margherita", "Hawaiian", "Veggie", "Combo"]

# Empty list for finished pizzas
finished_pizzas = []

# Process each pizza order
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print("Your pizza pie is finished!")
 # Move finished pizza to finished_pizzas list
    finished_pizzas.append(current_pizza)

# Print confirmation for all finished pizzas
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")