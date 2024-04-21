from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/")
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        print(request.json)
        return jsonify({"status":200})
    elif request.method == "GET":
        return render_template("login_page.html")