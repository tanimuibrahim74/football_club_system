# Entry point of the program
from football_club_system import FootballClubSystem  
# Imports the FootballClubSystem class from another file
# OOP USED HERE: Importing a CLASS

if __name__ == "__main__":
    # Checks if this file is run directly (not imported as a module)

    FootballClubSystem.start()  
    # OOP USED HERE: Calling a CLASS METHOD of FootballClubSystem
    # This starts the whole system without creating an object in this file
