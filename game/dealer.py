from game.card import Card


class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
        card (int): Card in play.
        lastCard (int): The last card drawn
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
        guess (char): The player's guess.
    """

    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.card = 0
        self.lastCard = Card()
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.guess = "n"

        self.card = Card()
        self.card.flip()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to guess.

        Args:
            self (Dealer): An instance of Dealer.
        """
        

        print("")
        print(f"The card is: {self.card.value}")
        self.guess = input("Higher or lower? [h/l] ")
            
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return 

        #deal a card
        self.lastCard.value = self.card.value
        self.card.flip()
        self.score = 0

        #check whether the new card is higher or lower
        answer = "n"
        if(self.card.value > self.lastCard.value):
            answer = "h"
        elif(self.card.value < self.lastCard.value):
            answer = "l"

        if(answer == "n"):
            self.score = 0
        elif(self.guess == answer):
            self.score = 100
        else:
            self.score = -75
        self.total_score += self.score

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to guess again. 

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return

        print(f"Next card was: {self.card.value}")
        print(f"Your score is: {self.total_score}")
        self.is_playing = (self.total_score > 0)

        if(self.is_playing):
            deal_card = input("Play again? [y/n] ")
            self.is_playing = (deal_card == "y")