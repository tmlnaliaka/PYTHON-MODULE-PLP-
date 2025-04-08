# Assignment 1: Design Your Own Class!

class Smartphone:
    """Represents a smartphone with attributes and methods."""

    def __init__(self, brand, model, storage, camera_resolution):
        """Initializes a Smartphone object."""
        self.brand = brand
        self.model = model
        self.storage = storage
        self.camera_resolution = camera_resolution
        self.is_on = False

    def power_on(self):
        """Turns the smartphone on."""
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now powered on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        """Turns the smartphone off."""
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now powered off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def take_photo(self):
        """Simulates taking a photo."""
        if self.is_on:
            print(f"Taking a photo with {self.camera_resolution}MP camera...")
        else:
            print(f"{self.brand} {self.model} is off. Power it on to take photos.")

    def get_storage_info(self):
        """Returns the storage information."""
        return f"Storage: {self.storage}GB"

class GamingSmartphone(Smartphone):
    """A gaming-specific smartphone, inheriting from Smartphone."""

    def __init__(self, brand, model, storage, camera_resolution, cooling_system):
        """Initializes a GamingSmartphone object."""
        super().__init__(brand, model, storage, camera_resolution)
        self.cooling_system = cooling_system

    def boost_performance(self):
        """Boosts performance for gaming."""
        if self.is_on:
            print(f"Activating {self.cooling_system} for optimal gaming performance.")
        else:
            print(f"{self.brand} {self.model} is off. Power it on to boost performance.")

# Example Usage:
my_phone = Smartphone("Google", "Pixel 7", 128, 50)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 512, 64, "AeroActive Cooler 6")

my_phone.power_on()
my_phone.take_photo()
print(my_phone.get_storage_info())
my_phone.power_off()

gaming_phone.power_on()
gaming_phone.boost_performance()
gaming_phone.take_photo()
gaming_phone.power_off()

# Activity 2: Polymorphism Challenge! 

class Animal:
    def move(self):
        """Base move method."""
        print("This animal moves.")

class Dog(Animal):
    def move(self):
        print("Running on four legs.")

class Fish(Animal):
    def move(self):
        print("Swimming in water.")

class Bird(Animal):
     def move(self):
        print("Flying through the air.")

class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the air. ✈️")

# Example Usage:
animals = [Dog(), Fish(), Bird()]
vehicles = [Car(), Plane()]

for animal in animals:
    animal.move()

for vehicle in vehicles:
    vehicle.move()