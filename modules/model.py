import random
import genanki


def generateModel():
    modelID = random.randrange(1 << 30, 1 << 31)

    return genanki.Model(
        modelID,
        'Hanzi Model',
        fields=[
            {'name': 'Character'},
            {'name': 'Pronunciation'},
            {'name': 'Examples'},
            {'name': 'Definition'},
            {'name': 'Pinyin'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt':
                """
                <div style="text-align: center;font-size: 20px;">
                    {{Character}}
                </div>
            """,
                'afmt':
                """
                <div style="text-align: center;">
                    {{Pronunciation}}
                    <hr id="examples">{{Examples}}
                    <hr id="definition">{{Definition}}
                    <hr id="pinyin">{{Pinyin}}
                </div>
            """,
            },
        ],
    )
