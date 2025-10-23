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
    def __init__(self, breed, fur_color, name, age) -> None:
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

if __name__ == "__main__":
    patrick_dog = Dog("rottweiler", "black", "lunch", 10)

    print(patrick_dog)
    patrick_dog.bark()