#An attempt to make a tarot deck that will print different randomized spreads. 

from random import randint
tarot = {
 1:	"The Magician", 2:	"The High Priestess", 3:"The Empress", 4:"The Emperor", 5:"The Hierophant", 6:"The Lovers",
 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man",
 13:"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon",
  19:"The Sun", 20:"Judgement", 21:"The World", 22: "The Fool"}

def card_spread(spread_length):
	for card in range(spread_length):
		num = randint(1, 22)
		print(tarot[num])
		del(tarot[num])


card_spread(4)


