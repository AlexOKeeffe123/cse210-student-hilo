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
        pass

    #alex
    def run_game(self):
        while (self.isRunnning):
            Keep_playing= input("Keeping playing [y/n] ")
            if Keep_playing.lower() == "n" or self.score == 0:
                self.isRunnning = False
            