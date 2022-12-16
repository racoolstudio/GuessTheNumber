from flask import Flask
from properties import *

app = Flask(__name__)


@app.route('/')
@make_bold
@make_underline
@make_italic
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/<name>')
def greetName(name):
    return f"Hello {name} you got this"


@app.route("/game")
def gameStart():
    return "<center><img src ='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width = '400'></center>"


@app.route("/game/<int:number>")
@checkNumber
def check(number):
    return ""


if __name__ == '__main__':
    app.run()
