import os

from flask import Flask
app = Flask(__name__)
greeting = 'hello'
message = 'Rajesh Sarakinti'


@app.route("/")
def hello():
    return greeting + " " + message


if __name__ == '__main__':
#   greeting = os.environ['GREETINGS_KEY']
#   message = os.environ['MESSAGE_KEY']

    app.run(debug=False, host='0.0.0.0')