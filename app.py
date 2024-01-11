from flask import Flask, send_file
from flask_cors import CORS
from support import urlID_to_Buffer, searchYotube
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

if __name__=='__main__':
    app.run()
