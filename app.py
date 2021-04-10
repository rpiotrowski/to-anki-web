from flask import Flask, render_template, abort, jsonify
from model import db

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('base.html')


@app.route('/settings')
def settings():
    return 'Settings'


@app.route('/card/<int:index>')
def show_card(index):
    try:
        card = db[index]
        return render_template('cards/card.html', card=card, index=index, max_index=len(db) - 1)
    except IndexError:
        abort(404)


@app.route('/cards')
def show_cards():
    return render_template('cards/cards.html', cards=db)


@app.route('/add_card')
def add_card():
    return render_template('cards/add_card.html')


@app.route('/api/card/<int:index>')
def api_show_card(index):
    try:
        return db[index]
    except IndexError:
        abort(404)


@app.route('/api/cards')
def api_show_cards():
    return jsonify(db)


if __name__ == '__main__':
    app.run()
