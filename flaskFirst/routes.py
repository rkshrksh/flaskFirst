from flask import render_template
from flaskFirst import app, db
from flaskFirst.models import Quote


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/quotes')
def quote():
    quotes = Quote.query.all()
    return str(quotes)
