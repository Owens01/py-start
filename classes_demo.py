
class Bus:
    def __init__(self, bus_number, model, color, year):
        self.bus_number = bus_number
        self.model = model
        self.color = color
        self.year = year

    def print_info(self):
        print(self.bus_number)
        print(self.model)

    def start(self):
        print(f"My bus is {self.model} and its number is {self.bus_number}, it has {self.color} color and was built in {self.year}")

my_bus = Bus("123", "Volvo", "red", 2026)
# my_bus.print_info()
my_bus.start()


