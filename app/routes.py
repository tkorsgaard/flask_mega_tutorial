from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Thomas'}
    title2 = {'title' : 'my blog'}
    return render_template('index.html', user=user, title=title2)