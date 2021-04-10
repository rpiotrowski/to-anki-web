"""
Example for prototyping
"""

import json


def load_flashcards():
    with open("flashcards_example.json") as file:
        return json.load(file)


def save_db():
    with open("flashcards_example.json", 'w') as file:
        return json.dump(db, file)


db = load_flashcards()
