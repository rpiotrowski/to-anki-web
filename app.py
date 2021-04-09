from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('welcome.html', message="Welcome",)


@app.route('/settings')
def settings():
    return 'Settings'

@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        return render_template('card.html', card=card)
    except IndexError:
        abort(404)


if __name__ == '__main__':
    app.run()
