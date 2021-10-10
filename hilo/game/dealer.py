import random

class Dealer:
    """A code template for a person who deals cards in the game. The responsibility of 
    this class is to keep an arrauy of cards and deal the cards to the player.

    Attributes:
        cards (string array): Array of 13 strings representing card values.
    """

    #eber
    def __init__(self):
        """Initializes the dealer class object with a deck of cards.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    #tyson
    def deal_first_card(self):
        """Deals (prints) a random card to the user.

        Args:
            self (Dealer): An instance of Dealer.
        Returns:
            int: Value representing the integer representation of the card for comparison.
        """
        randomCardIndex = random.randint(0,12)
        print(f'The card is: {self.cards[randomCardIndex]}')
        return randomCardIndex

    #tyson
    def deal_second_card(self):
        """Deals (prints) a random card to the user.

        Args:
            self (Dealer): An instance of Dealer.
        Returns:
            int: Value representing the integer representation of the card for comparision.
        """
        randomCardIndex = random.randint(0,12)
        print(f'The next card was: {self.cards[randomCardIndex]}')
        return randomCardIndex