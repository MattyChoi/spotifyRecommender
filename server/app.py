import os

from flask import Flask,  request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape

import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
CORS(app)
# db = SQLAlchemy(app)

# to start app
# set FLASK_APP=app (or set FLASK_APP since files is called app.py) for windows
# export FLASK_APP=app (or set FLASK_APP since files is called app.py) for mac
# flask run

# enable dev mode be like
# set FLASK_ENV=development
# export FLASK_APP=development (or set FLASK_APP since files is called app.py) for mac
# flask run


client = os.getenv('client_id')
secret = os.getenv('client_secret')
uri = os.getenv('redirect_uri')
scope = 'user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client,
                                               client_secret=secret,
                                               redirect_uri=uri,
                                               scope=scope))
                                        
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


@app.route("/")
def hello_world():
    return f"client: {client}, secret: {secret}"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

    
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return "<p>Hello, World!</p>"
#     else:
#         return "<p>Hello, World!</p>"