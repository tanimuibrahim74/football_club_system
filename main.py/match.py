class Match:
    # OOP USED HERE: This is a CLASS (blueprint for match objects)

    """
    Match class stores match information.
    """

    def __init__(self, match_id, opponent, score):
        # OOP USED HERE: Constructor method (runs when object is created)

        self.match_id = match_id  
        # Stores the match ID inside the object (attribute)

        self.opponent = opponent  
        # Stores opponent team name inside the object

        self.score = score        
        # Stores match score inside the object

    def get_match_info(self):
        # OOP USED HERE: Method belonging to Match object

        """
        Returns match information as a string.
        """

        return f"Match ID: {self.match_id}, Opponent: {self.opponent}, Score: {self.score}"
        # Creates and returns a formatted string with match details

    def to_dict(self):
        # OOP USED HERE: Method for converting object to dictionary

        """
        Converts Match object to dictionary for JSON storage.
        """

        return {
            "match_id": self.match_id,
            # Adds match_id to dictionary

            "opponent": self.opponent,
            # Adds opponent to dictionary

            "score": self.score
            # Adds score to dictionary
        }
