# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    """
    A simple Dog class to learn OOP concepts

    Attributes:
        breed - the breed of the dog
        fur_color - the fur color of the dog
        name - the name of the dog
        age - the age of the dog
    """
    def __init__(self, breed = "dog", fur_color = "brown", name = "no_name", age = 1) -> None:
        """Initialize a new Dog with breed, fur_color, name, and age"""
        self.breed = breed
        self.fur_color = fur_color
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """String representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"
    
    def bark(self):
        print(f"{self.name} says: Woof, woof!")

    def birthday(self):
        """celebrate the dog's birthday"""
        self.age += 1
        print(f"{self.name} is celebrating their {self.age} birthday!")

    def paint_dog(self, new_color):
        """Changes the fur_color of the dog"""
        old_color = self.fur_color
        self.fur_color = new_color
        print(f"{self.name} changed their fur color from {old_color} to {new_color}.")


if __name__ == "__main__":
    patrick_dog = Dog("rottweiler", "black", "lunch", 10)
    matthew_dog = Dog(breed = "labrador", name = "bella", age = 1)
    default_dog = Dog()

    print(default_dog)
    print(patrick_dog)
    print(matthew_dog)

    patrick_dog.bark()
    patrick_dog.birthday()
    patrick_dog.paint_dog("purple")