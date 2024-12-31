class Animal:
    """Parent class for all animals on the farm."""
    def __init__(self, name: str, age: int, sound: str):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self) -> str:
        """Animals make their unique sound."""
        return f"{self.name} says {self.sound}!"

    def eat(self) -> str:
        """Simulates the animal eating."""
        return f"{self.name} is eating."

    def sleep(self) -> str:
        """Simulates the animal sleeping."""
        return f"{self.name} is sleeping."

class Cow(Animal):
    """Represents a cow on the farm."""
    def __init__(self, name: str, age: int, milk_production: float):
        super().__init__(name, age, sound="Moo")
        if milk_production < 0:
            raise ValueError("Milk production must be a positive value.")
        self.milk_production = milk_production  # in liters per day

    def produce_milk(self) -> str:
        """Simulates the cow producing milk."""
        return f"{self.name} produces {self.milk_production} liters of milk per day."

class Chicken(Animal):
    """Represents a chicken on the farm."""
    def __init__(self, name: str, age: int, egg_production: int):
        super().__init__(name, age, sound="Cluck")
        if egg_production < 0:
            raise ValueError("Egg production must be a positive value.")
        self.egg_production = egg_production  # eggs per day

    def lay_eggs(self) -> str:
        """Simulates the chicken laying eggs."""
        return f"{self.name} lays {self.egg_production} eggs per day."

class Sheep(Animal):
    """Represents a sheep on the farm."""
    def __init__(self, name: str, age: int, wool_amount: float):
        super().__init__(name, age, sound="Baa")
        if wool_amount < 0:
            raise ValueError("Wool amount must be a positive value.")
        self.wool_amount = wool_amount  # in kilograms per year

    def shear_wool(self) -> str:
        """Simulates shearing the sheep's wool."""
        return f"{self.name} provides {self.wool_amount} kg of wool per year."

# Example usage:
def main():
    cow = Cow(name="Bessie", age=5, milk_production=20)
    chicken = Chicken(name="Clucky", age=2, egg_production=4)
    sheep = Sheep(name="Woolly", age=3, wool_amount=8)

    animals = [cow, chicken, sheep]

    for animal in animals:
        print("-" * 30)
        print(animal.make_sound())
        print(animal.eat())
        print(animal.sleep())

    # Specific actions for each animal
    print("-" * 30)
    print(cow.produce_milk())
    print(chicken.lay_eggs())
    print(sheep.shear_wool())

if __name__ == "__main__":
    main()
