from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('welcome.html', message="Welcome",)


@app.route('/settings')
def settings():
    return 'Settings'


if __name__ == '__main__':
    app.run()
