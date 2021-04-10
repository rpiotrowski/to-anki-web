from flask import Flask, render_template, abort, jsonify
from model import db

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html', message="Welcome", )


@app.route('/settings')
def settings():
    return 'Settings'


@app.route('/card/<int:index>')
def show_card(index):
    try:
        card = db[index]
        return render_template('card.html', card=card, index=index, max_index=len(db) - 1)
    except IndexError:
        abort(404)


@app.route('/cards')
def show_cards():
    return render_template('cards.html', cards=db)


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
