from flask import Flask

# create instace of Flask using our module's name
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
