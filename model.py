"""
Example for prototyping
"""

import json


def load_flashcards():
    with open("flashcards_example.json") as file:
        return json.load(file)


db = load_flashcards()
