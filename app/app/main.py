from flask import Flask

from app.mypackage import mymodule

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    response = mymodule.myfunction()
    return response
