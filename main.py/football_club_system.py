from player import Player
# Imports Player class (OOP: using another class)

from match import Match
# Imports Match class (OOP: using another class)

from file_manager import FileManager
# Imports FileManager class (OOP: composition – using an object inside another class)

class FootballClubSystem:
    # OOP USED HERE: This is a CLASS (blueprint for the system)

    """
    Controls the entire football club system.
    """

    def __init__(self):
        # OOP USED HERE: Constructor method

        self.players = []
        # List that will store Player objects

        self.matches = []
        # List that will store Match objects

        self.file_manager = FileManager()
        # OOP USED HERE: Creating an OBJECT from FileManager class

        self.role = None
        # Stores current role (admin or user)

        self.load_data()
        # Calls load_data method when object is created

    @classmethod
    def start(cls):
        # OOP USED HERE: Class method (belongs to class, not object)

        system = cls()
        # Creates an object of FootballClubSystem

        system.run()
        # Calls run method on the object

    def load_data(self):
        # OOP USED HERE: Method inside class

        data = self.file_manager.load_data()
        # Loads raw data from JSON using FileManager object

        self.players = [Player(**p) for p in data["players"]]
        # Recreates Player objects from dictionary data

        self.matches = [Match(**m) for m in data["matches"]]
        # Recreates Match objects from dictionary data

    def save_data(self):
        # Method to save system data

        data = {
            "players": [p.to_dict() for p in self.players],
            # Converts each Player object into dictionary

            "matches": [m.to_dict() for m in self.matches]
            # Converts each Match object into dictionary
        }

        self.file_manager.save_data(data)
        # Saves data to JSON using FileManager object

    def login(self):
        # Method for login system

        print("\n--- Login ---")
        print("1. Admin")
        print("2. User")

        choice = input("Choose role: ")
        # Takes user choice

        if choice == "1":
            password = input("Enter admin password: ")
            # Asks for admin password

            if password == "12345":
                self.role = "admin"
                # Sets role to admin
                print("Logged in as Admin")
                return True
            else:
                print("Wrong password")
                return False

        elif choice == "2":
            self.role = "user"
            # Sets role to user
            print("Logged in as User")
            return True

        else:
            print("Invalid option")
            return False

    def run(self):
        # Main controller logic

        if not self.login():
            # If login fails, stop program
            return

        if self.role == "admin":
            # Checks role
            self.admin_menu()
        else:
            self.user_menu()

    def admin_menu(self):
        # Admin menu method

        while True:
            print("\n--- ADMIN MENU ---")
            print("1. Add Player")
            print("2. Delete Player")
            print("3. Edit Player")
            print("4. Add Match")
            print("5. Edit Match")
            print("6. View Players")
            print("7. View Match History")
            print("8. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.add_player()
            elif choice == "2":
                pid = int(input("Enter player ID: "))
                self.delete_player(pid)
            elif choice == "3":
                pid = int(input("Enter player ID: "))
                self.edit_player(pid)
            elif choice == "4":
                self.add_match()
            elif choice == "5":
                mid = int(input("Enter match ID: "))
                self.edit_match(mid)
            elif choice == "6":
                self.view_players()
            elif choice == "7":
                self.view_match_history()
            elif choice == "8":
                self.save_data()
                print("Exiting system...")
                break
            else:
                print("Invalid option")

    def user_menu(self):
        # User menu (view only)

        while True:
            print("\n--- USER MENU ---")
            print("1. View Players")
            print("2. View Match History")
            print("3. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.view_players()
            elif choice == "2":
                self.view_match_history()
            elif choice == "3":
                print("Exiting system...")
                break
            else:
                print("Invalid option")

    def add_player(self):
        # Adds new Player object

        pid = int(input("ID: "))
        name = input("Name: ")
        pos = input("Position: ")
        goals = int(input("Goals: "))

        self.players.append(Player(pid, name, pos, goals))
        # OOP USED HERE: Creating Player object

        self.save_data()

    def delete_player(self, player_id):
        # Deletes Player by ID

        self.players = [p for p in self.players if p.player_id != player_id]
        # Filters list using condition

        self.save_data()

    def edit_player(self, player_id):
        # Edits Player object

        for p in self.players:
            if p.player_id == player_id:
                p.name = input("New name: ")
                p.position = input("New position: ")
                p.goals = int(input("New goals: "))
                self.save_data()
                return

        print("Player not found")

    def view_players(self):
        # Displays all players

        for p in self.players:
            print(p.display_info())
            # OOP USED HERE: Calling method on Player object

    def add_match(self):
        # Adds Match object

        mid = int(input("Match ID: "))
        opp = input("Opponent: ")
        score = input("Score: ")

        self.matches.append(Match(mid, opp, score))
        # OOP USED HERE: Creating Match object

        self.save_data()

    def edit_match(self, match_id):
        # Edits Match object

        for m in self.matches:
            if m.match_id == match_id:
                m.opponent = input("New opponent: ")
                m.score = input("New score: ")
                self.save_data()
                return

        print("Match not found")

    def view_match_history(self):
        # Displays match history

        for m in self.matches:
            print(m.get_match_info())
            # OOP USED HERE: Calling method on Match object
