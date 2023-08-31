import random
import genanki


def generateDeck():
    deckID = random.randrange(1 << 30, 1 << 31)
    return genanki.Deck(
        deckID,
        'Output Deck'
    )
