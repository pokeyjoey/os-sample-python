from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "This is the way the world ends, not with a bang .... but a whimper."

if __name__ == "__main__":
    application.run()
