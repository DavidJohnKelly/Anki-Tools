import example
import definition
import pinyin
import pronunciation

import genanki


def generateCard(word, AnkiModel):
    pron = pronunciation.getPronunciation(word)
    examp = example.getExamples(word)
    defin = definition.getDefinition(word)
    pyn = pinyin.getPinyin(word)

    return genanki.Note(
        model=AnkiModel,
        fields=[word, pron, examp, defin, pyn]
    )
