from flask import Flask

from app.mypackage.mymodule import myfunction

app = Flask(__name__)

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def hello_world(path):
    response = myfunction()
    return response
