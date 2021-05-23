from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

# This allows CORS for all domains on all routes
CORS(app)

@app.route('/')
@cross_origin() # this allows CORS only for the specified route
def index():
    return "Hi"


### 2 ways to run the flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)