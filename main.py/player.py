from person import Person
# Imports the Person class
# OOP USED HERE: Using another class (Inheritance relationship)

class Player(Person):
    # OOP USED HERE: This is a CLASS
    # OOP USED HERE: INHERITANCE – Player inherits from Person

    """
    Player class inherits from Person.
    """

    def __init__(self, player_id, name, position, goals):
        # OOP USED HERE: Constructor method for Player

        super().__init__(name)
        # OOP USED HERE: Calls the constructor of the parent class (Person)
        # This sets self.name using Person's __init__ method

        self.player_id = player_id  
        # Stores unique player ID as an attribute

        self.position = position    
        # Stores playing position as an attribute

        self.goals = goals          
        # Stores number of goals scored as an attribute

    def display_info(self):
        # OOP USED HERE: Method OVERRIDING (Polymorphism)

        """
        Polymorphism: overrides abstract method from Person.
        """

        return f"ID: {self.player_id}, Name: {self.name}, Position: {self.position}, Goals: {self.goals}"
        # Returns formatted string with player details

    def to_dict(self):
        # Method to convert Player object into dictionary

        """
        Converts Player object to dictionary for JSON storage.
        """

        return {
            "player_id": self.player_id,
            # Adds player_id to dictionary

            "name": self.name,
            # Adds name (inherited from Person)

            "position": self.position,
            # Adds position

            "goals": self.goals
            # Adds goals
        }
