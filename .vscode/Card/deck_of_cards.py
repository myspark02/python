import random

class Card :
    def __init__(self, suite, value) :
        self.suite = suite
        self.value = value

    def show(self) :
        print("{} of {}".format(self.value, self.suite))    

class Deck :
    def __init__(self) :
        self.cards = []
        self.build()
    
    def build(self) :
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"] :
            for v in range(1, 14) :
                self.cards.append(Card(s, v))

    def show(self) :
        for c in self.cards :
            c.show()

    def shuffle(self) :
        for i in range(len(self.cards)-1, 0, -1) :
                rand = random.randint(0, i)
                self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]
        # random.shuffle(self.cards)
    
    def drawCard(self) :
        return self.cards.pop()


class Player :
    def __init__(self, name) :
      self.name = name  
      self.hand = []

    def draw(self, deck) :
        self.hand.append(deck.drawCard())
        return self

    def showHand(self) :
        for card in self.hand :
            card.show()

    def discard(self) :
        return self.hand.pop()        

deck = Deck()
deck.shuffle()
# deck.show()

bob = Player("Bob")
bob.draw(deck).draw(deck).draw(deck)
bob.showHand()


# card = deck.drawCard()
# card.show()   


