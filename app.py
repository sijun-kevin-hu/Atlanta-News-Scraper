from flask import Flask, render_template
from scraper import scrape

app = Flask(__name__)

@app.route("/")
def index():
    headlines = scrape()
    return render_template('index.html', headlines=headlines)