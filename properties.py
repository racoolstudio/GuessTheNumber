import random

guess = random.randint(0, 10)


def make_bold(name):
    def wrapper_funct():
        return f"<b>{name()}</b>"

    return wrapper_funct


def make_italic(function):
    def wrapper_funct():
        return f"<em>{function()}</em>"

    return wrapper_funct


def make_underline(function):
    def wrapper_funct():
        return f"<u>{function()}</u>"

    return wrapper_funct


def make_bold_input(name):
    def wrapper_funct(*args, **kwargs):
        return f"<b>{name(args[0])}</b>"

    return wrapper_funct


def make_italic_input(function):
    def wrapper_funct(*args, **kwargs):
        return f"<em>{function(args[0])}</em>"

    return wrapper_funct


def make_underline_input(function):
    def wrapper_funct(**kwargs):
        return f"<u>{function(kwargs['name'])}</u>"
    return wrapper_funct


def checkNumber(func):
    def wrapper(**kwargs):
        if kwargs["number"] > guess:
            return f"<center><h1>You Typed {kwargs['number']} it is High!!! Try again\n</h1>" \
                   f"<img  width='400' src='https://media0.giphy.com/media/JgKyjyun8eEEENXpKw/200w.webp?cid" \
                   f"=ecf05e47k0qnmqihw8wj9kffu9xz5cuxeb7wvrijubu4wryi&rid=200w.webp&ct=g'></center> "
        elif kwargs["number"] < guess:
            return f"<center><h1>You Typed {kwargs['number']} it is Low !!! Try again</h1>\n" \
                   f"<img src ='https://media4.giphy.com/media/i6TiqPLXSRfs2L86fy/giphy.gif?cid" \
                   f"=ecf05e47mzbaeafr5jobuydq7hotjs9a9cec4p86ooqhxiiu&rid=giphy.gif' ></center> "
        else:
            return "<center><h1>You found Me !!!<h1>\n" \
                   "<img width = '400' src = 'https://media3.giphy.com/media/3oz8xAFtqoOUUrsh7W/200w.webp?cid" \
                   "=ecf05e47mbjucskn2nbtwqjmvbp2tmjwnbuux6b2ijqlemnd&rid=200w.webp&ct=g'></center>"

    return wrapper


@make_bold_input
def greet(name):
    return f"Hello {name} you got this"


print(greet("Manned"))
