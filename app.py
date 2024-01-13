from flask import Flask, send_file, request
from flask_cors import CORS
from support import urlID_to_Buffer, searchYotube, playlistFetch
app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return 'Music'

@app.route('/music/<id>')
def stream(id):
    musicOBJ = urlID_to_Buffer(id)
    return send_file(musicOBJ['music'],mimetype=musicOBJ['mime'], as_attachment=False)

@app.route('/get/<q>')
def searcher(q):
    return searchYotube(q)

@app.route('/playlist',methods=['POST'])
def playlist():
    url = request.json['playlist']
    return playlistFetch(url)


if __name__=='__main__':
    app.run()