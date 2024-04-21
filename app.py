from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world"

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        return {"status":200}