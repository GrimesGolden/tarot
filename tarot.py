from random import randint
from random import shuffle

class Card:
  suits = ["Wands",
            "Cups",
            "Swords",
            "Pentacles"]

  values = [None, None,"2", "3",
            "4", "5", "6", "7",
            "8", "9", "10",
            "Page", "Queen",
            "King", "Knight", "Ace",]

  def __init__(self, v, s):
    """suit + value are ints"""
    self.value = v
    self.suit = s

  def __repr__(self):
    v = self.values[self.value] +" of " + self.suits[self.suit]
    return v
        
class Tarot:
  def __init__(self):
    major_arcana = ["The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers",
                    "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
                     "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World", "The Fool",]
    self.cards = []
    for i in range(2, 16):
      for j in range(4):
        self.cards.append(Card(i,j))
    for i in range(len(major_arcana)):
      self.cards.append(major_arcana.pop())
      shuffle(self.cards)

  def spread(self, size):
    for i in range(size):
      draw = self.cards.pop()
      print(draw)

deck = Tarot()
# Call spread with integer number of how many cards to draw. 
deck.spread(3)