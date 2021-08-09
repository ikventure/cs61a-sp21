# All cards available in a standard deck.
from classes import *

#TAs
richard_z = TACard('Richard Zhu, Left Winger of 61A FC', 1999, 1000)
patricia = TACard('Patricia, Ace Trainer', 1999, 1999)
richard_r = TACard('Richard, Protector of Grogu', 1888, 1600)
jade = TACard('Jade Singher of Songs', 1300, 1000)
murtz = TACard('KingMuntzy Boi', 2100, 1100)
chris = TACard('Chris, Dean of Procrastination', 2000, 1000)
vanshaj = TACard('Vanshaj, Head Memefinder', 1758, 1243)
shayna = TACard('Shayna, The Retired', 1200, 2200)
yersultan = TACard('Yersultan, Yogurt', 1717, 1717)
rachel = TACard('Rache, Wearer of Jeans', 1080, 2250)

#Tutors
constance = TutorCard('Connie, Consumer of Carbs', 1357, 1853)
ben = TutorCard('Ben, the recursive panda', 1024, 2048)
cyrus = TutorCard('Cyrus, Pizza of Piazza', 1500, 2200)
kenny = TutorCard('Kenny, Surveyor of Surveys', 1920, 1080)




# Professors

# A standard deck contains all standard cards.
standard_cards = [richard_r, richard_z, patricia, jade, murtz, chris, vanshaj, shayna, yersultan, rachel, constance, ben, cyrus, kenny]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()