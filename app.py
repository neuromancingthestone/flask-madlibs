from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "madlibstories"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('base.html', my_story=story)

@app.route('/story')
def filled_story():
    entries = request.args
    full_story = story.generate(entries)
    return render_template('story.html', my_story=full_story)