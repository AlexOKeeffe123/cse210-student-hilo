from dealer import Dealer

class Director:

    #pedro
    def __init__(self):
        pass
    
    #alex
    def start_game(self):
        pass

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
        pass