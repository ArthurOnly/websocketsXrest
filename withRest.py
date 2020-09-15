import json
from flask import Flask,request
from flask_cors import CORS
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
CORS(app)

@app.route('/', methods=["POST"])
def resources():
    request_json = request.get_json()
    
    print(request_json)

    return json.dumps("{'Recebido':'True'}")

if __name__=="__main__":
    app.run()
