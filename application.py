from flask import Flask

application = Flask(__name__)

@application.route('/', defaults={'path': ''})

@application.route('/<path:path>')
def hello_world(path):
    return 'Hello, World!'

if __name__ == "__main__":
    application.debug = True
    application.run()
