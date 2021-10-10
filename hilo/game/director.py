from dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        isRunning (boolean): Whether or not the game is running.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """

    #pedro
    def __init__(self):
        """Initializes the Director class object with a score of 300, a dealer object, and the game running.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.isRunning = True
        self.dealer = Dealer()
        self.score = 300

    #alex
    def play_round(self):
        """Plays one round of High Low and updates the score accordingly (+100 for a win, -75 for a loss).

        Args:
            self (Dealer): An instance of Dealer.
        """
        guess = self.get_cards()
        if guess == True:
            self.score += 100
        else:
            self.score -= 75

    #chase
    def get_cards(self):
        """Get the inputs at the beginning of each round and returns True or False depending on user's choice

        Args:
            self (Director): An instance of Director
            dealer (Dealer): an instance of Dealer
        
        Returns:
            boolean: values represent one of two values, True or False. For comparing card1 and card2.
        """
        card1 = self.dealer.deal_first_card()
        guess = input(f'High or Low? (h/l)').lower
        
        card2 = self.dealer.deal_second_card()
        if guess == 'l':
            if card2 <= card1:
                return True
            else:
                return False
        elif guess == 'h':
            if card2 >= card1:
                return True
            else:
                return False

        


        

    #alex
    def run_game(self):
        """Starts the game loop for one game of high low. Ends the game at user request or failure.

        Args:
            self (Dealer): An instance of Dealer.
        """
        while (self.isRunnning):
            isRunning = input("Keeping playing [y/n] ")
            self.play_round()
            if isRunning.lower() == "n" or self.score <= 0:
                self.isRunnning = False