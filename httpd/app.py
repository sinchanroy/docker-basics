from flask import Flask

app = Flask(__name__)

@app.route("/invocations")
def home():
    return "Hello invocations"

@app.route("/")
def home():
    return "Hello root"


if __name__ == "__main__":
    app.run(port='8080')
