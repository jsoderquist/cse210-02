import random


class Card:
    """A paper showing a number.

    The responsibility of Card is to keep track of its own value.
   
    Attributes:
        value (int): The number on the card.
    """

    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def flip(self):
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)
