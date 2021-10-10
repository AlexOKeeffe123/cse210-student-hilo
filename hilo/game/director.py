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
        self.dealer = Dealer()
        self.score = 300

    #alex
    def play_round(self):

        self.get_cards()
        if  self.blank == True:
            self.score += 100
        else:
            self.score =+ 75
        return self.score

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
        while (self.isRunnning):
            Keep_playing= input("Keeping playing [y/n] ")
            if Keep_playing.lower() == "n" or self.score == 0:
                self.isRunnning = False
            