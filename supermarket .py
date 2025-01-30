class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_stock(self, quantity):
        if quantity >= 0:
            self.quantity = quantity
        else:
            print("Quantity cannot be negative!")

    def display_product(self):
        print(f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.quantity}")


class Supermarket:
    def __init__(self):
        self.products = {}

    def add_product(self):
        product_id = input("Enter Product ID: ")
        if product_id in self.products:
            print("Product already exists!")
            return

        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Stock Quantity: "))
        self.products[product_id] = Product(product_id, name, price, quantity)
        print("Product added successfully!")

    def view_products(self):
        if not self.products:
            print("No products available!")
        else:
            print("\nAvailable Products:")
            for product in self.products.values():
                product.display_product()

    def sell_product(self):
        product_id = input("Enter Product ID to sell: ")
        if product_id in self.products:
            product = self.products[product_id]
            quantity = int(input("Enter quantity to sell: "))

            if quantity > 0 and quantity <= product.quantity:
                total_price = quantity * product.price
                product.quantity -= quantity
                print(f"Sold {quantity} {product.name}(s) for ${total_price:.2f}")
                print(f"Remaining stock: {product.quantity}")
            else:
                print("Invalid quantity or insufficient stock!")
        else:
            print("Product not found!")

    def run(self):
        while True:
            print("\n--- Supermarket Management System ---")
            print("1. Add Product")
            print("2. View Products")
            print("3. Sell Product")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.view_products()
            elif choice == "3":
                self.sell_product()
            elif choice == "4":
                print("Thank you for using the Supermarket System!")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    market = Supermarket()
    market.run()
