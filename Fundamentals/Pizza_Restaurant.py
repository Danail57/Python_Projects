
# Създайте програма, която симулира меню за поръчка на пица с
# различни видове пици, размери и добавки.
# Програмата трябва да позволи на потребителя да избере пица,
# размер и добавки, след което да изчисли общата цена на поръчката.


def pizza_menu():
    
    pizzas = ["Pepperoni", "Hawaiian", "Ordinary"]
    print("Available pizzas:")
    for idx, pizza in enumerate(pizzas, 1):
        print(f"{idx}. {pizza}")

    choice = int(input("Select the type of pizza (1-3): "))
    if choice in range(1, 4):
        return pizzas[choice - 1]
    else:
        print("Invalid choice!")
        return None


def pizza_size():
    sizes = {"S": 5, "M": 7, "L": 10}
    print("Available sizes: S, M, L")
    size = input("Please, select a size (S, M, L): ").upper()
    if size in sizes:
        return size, sizes[size]
    else:
        print("Invalid size choice!")
        return None, 0


def additionals_menu():
    additionals = {
        "cheese": 0.75,
        "ranch sausage": 1.20,
        "chicken meat": 2.10
    }

    print("Available additions:")
    for idx, (addition, price) in enumerate(additionals.items(), 1):
        print(f"{idx}. {addition} - {price} leva")

    selected_additions = input("Please, select additions (comma separated): ").lower().split(',')

    total_addition_price = 0
    for addition in selected_additions:
        addition = addition.strip()
        if addition in additionals:
            total_addition_price += additionals[addition]
        else:
            print(f"{addition} is not a valid addition.")

    return total_addition_price


def main():
    pizza = pizza_menu()
    if pizza:
        size, size_price = pizza_size()
        if size:
            print(f"You selected {pizza} pizza with size {size}.")
            additions_price = additionals_menu()
            if additions_price is not None:
                total_price = size_price + additions_price
                print(f"The total price for your pizza is: {total_price:.2f} leva.")
            else:
                print("No additions selected.")
        else:
            print("No valid size selected.")
    else:
        print("No valid pizza selected.")

main()
