from abc import ABC, abstractmethod
# Imports ABC (Abstract Base Class) and abstractmethod decorator
# These are used to create abstract classes in Python

class Person(ABC):
    # OOP USED HERE: This is a CLASS
    # OOP USED HERE: It is an ABSTRACT CLASS because it inherits from ABC

    """
    Abstract base class for a person.
    This class cannot be instantiated directly.
    """

    def __init__(self, name):
        # OOP USED HERE: Constructor method

        self.name = name  
        # OOP USED HERE: Encapsulation
        # Stores the name inside the object as an attribute

    @abstractmethod
    def display_info(self):
        # OOP USED HERE: Abstract method
        # This method MUST be implemented by any subclass

        """
        Abstract method that must be implemented by subclasses.
        """

        pass
        # pass means "no code here"
        # This method has no body because subclasses will define it
