from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello people"


@app.route("/alive")
def alive():
    return "ALIVE!!!"


if __name__ == "__main__":
    app.run()
