
# Create a Class
class Snack:
    def __init__(self, item, brand, size, price):
        self.item = item
        self.brand = brand
        self.size = size
        self.price = price

    # Create a Method
    def unit_price(self):
        unit = self.price / self.size
        return round(unit,2)

# Create a new Class
class Drinks(Snack):
    def __init__(self, item, brand, size, price, case):
        super().__init__(item, brand, size, price)
        self.case = case
        self.price = price * case

if __name__ == "__main__":
    snack_1 = Snack('chips', 'Lays', 9.5, 4.25)
    snack_2 = Snack('soda','Pepsi', 12, 1.25)
   
    print("Snack_1 size:", snack_1.size)
    print("Snack_2 brand:", snack_2.brand)
    print("Snack_1 unit price:", snack_1.unit_price())

    snack_2 = Drinks('soda','Pepsi', 12, 1.25, 6)
    print("Snack_2 case quantity:", snack_2.case)
    print("Snack_2 price:", snack_2.price)
