from app import app
from flask import render_template


@app.route('/')
def hello():
    return "hello world"


@app.route("/keklol")
def keklol():
    return "Hello this is really kek!"


@app.route("/calc/<int:number_1>/<int:number_2>")
def hello_user(number_1, number_2):
    sum = number_1 + number_2
    return render_template("index.html", sum=sum)


# @app.route("/news/<int:id>")
# def news(id):
#     #news= SELECT * FROM news WHERE id=id
#     return news