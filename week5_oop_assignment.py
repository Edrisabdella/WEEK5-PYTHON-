class Superhero:
    def __init__(self, name, secret_identity, powers, health=100):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
        self.health = health
        self._is_transformed = False  # Encapsulated attribute

    def use_power(self, power_index):
        if power_index < len(self.powers):
            print(f"{self.name} uses {self.powers[power_index]}!")
            return True
        else:
            print(f"{self.name} doesn't have that power!")
            return False

    def transform(self):
        if not self._is_transformed:
            self._is_transformed = True
            print(f"{self.secret_identity} transforms into {self.name}!")
        else:
            print(f"{self.name} is already transformed!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            self.health = 0
        else:
            print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def heal(self, amount):
        if self.health > 0:
            self.health = min(100, self.health + amount)
            print(f"{self.name} heals {amount} points. Health: {self.health}")
        else:
            print(f"{self.name} is defeated and cannot heal!")

    # Encapsulation: Getter method for private attribute
    def get_transformation_status(self):
        return self._is_transformed

    def __str__(self):
        return f"Superhero: {self.name} (Secret: {self.secret_identity}), Powers: {', '.join(self.powers)}, Health: {self.health}"


# Inheritance example: A specific type of superhero
class CosmicSuperhero(Superhero):
    def __init__(self, name, secret_identity, powers, health=100, cosmic_energy=100):
        super().__init__(name, secret_identity, powers, health)
        self.cosmic_energy = cosmic_energy

    # Polymorphism: Override the use_power method
    def use_power(self, power_index):
        if self.cosmic_energy >= 10:
            success = super().use_power(power_index)
            if success:
                self.cosmic_energy -= 10
                print(f"Cosmic energy remaining: {self.cosmic_energy}")
            return success
        else:
            print(f"{self.name} doesn't have enough cosmic energy!")
            return False

    def absorb_cosmic_energy(self, amount):
        self.cosmic_energy = min(100, self.cosmic_energy + amount)
        print(f"{self.name} absorbs {amount} cosmic energy. Total: {self.cosmic_energy}")

    def __str__(self):
        return f"CosmicSuperhero: {self.name}, Cosmic Energy: {self.cosmic_energy}, Health: {self.health}"


# Testing the classes
if __name__ == "__main__":
    print("=== Superhero Class Demonstration ===")
    
    # Create a regular superhero
    spider_man = Superhero("Spider-Man", "Peter Parker", 
                          ["Web Shooting", "Spider-Sense", "Wall-Crawling"])
    print(spider_man)
    spider_man.transform()
    spider_man.use_power(0)
    spider_man.take_damage(25)
    spider_man.heal(10)
    
    print("\n")
    
    # Create a cosmic superhero (inheritance example)
    silver_surfer = CosmicSuperhero("Silver Surfer", "Norrin Radd", 
                                   ["Cosmic Blast", "Flight", "Matter Manipulation"], 
                                   cosmic_energy=80)
    print(silver_surfer)
    silver_surfer.use_power(0)  # Uses cosmic energy
    silver_surfer.use_power(0)  # Uses more cosmic energy
    silver_surfer.absorb_cosmic_energy(30)
    silver_surfer.use_power(1)

    activity 2
    class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def speak(self):
        return f"I am {self.name}"

class Fish(Animal):
    def move(self):
        return "Swimming gracefully through the water 🐟"
    
    def speak(self):
        return "Blub blub!"

class Bird(Animal):
    def move(self):
        return "Flying high in the sky 🦅"
    
    def speak(self):
        return "Chirp chirp!"

class Cheetah(Animal):
    def move(self):
        return "Running at incredible speed! 🐆"
    
    def speak(self):
        return "Growl!"

# Demonstration of polymorphism
def demonstrate_movement(animals):
    for animal in animals:
        print(f"{animal.speak()} {animal.move()}")

if __name__ == "__main__":
    print("\n=== Polymorphism Challenge: Animal Movement ===")
    
    # Create different animals
    nemo = Fish("Nemo")
    tweety = Bird("Tweety")
    chester = Cheetah("Chester")
    
    # Demonstrate polymorphism
    animals = [nemo, tweety, chester]
    demonstrate_movement(animals)
    
    print("\n=== Additional Example: Vehicles ===")
    
    # Additional example with vehicles
    class Vehicle:
        def __init__(self, name):
            self.name = name
            
        def move(self):
            raise NotImplementedError("Subclasses must implement this method")
            
    class Car(Vehicle):
        def move(self):
            return f"{self.name} is driving on the road 🚗"
            
    class Plane(Vehicle):
        def move(self):
            return f"{self.name} is flying in the air ✈️"
            
    class Boat(Vehicle):
        def move(self):
            return f"{self.name} is sailing on water ⛵"
    
    # Create different vehicles
    mustang = Car("Mustang")
    boeing = Plane("Boeing 747")
    yacht = Boat("Luxury Yacht")
    
    vehicles = [mustang, boeing, yacht]
    for vehicle in vehicles:
        print(vehicle.move())