from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import json

def writeData(data):
    with open("userNpass.txt", "w+") as f:
        contents = json.load(f)
        for i in contents["username"]:
            if i == data["username"]:
                return True
        json.dump(data, f, ensure_ascii=False, indent=4)
        return False


app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        print(request.json)
        return jsonify({"status":200})
    elif request.method == "GET":
        return render_template("login_page.html")
    
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup_page.html")
    elif request.method == "POST":
        a = writeData(request.json)
        if a == False:
            return jsonify({"status":200, "message":"Signed up successfully"})
        elif a == True:
            return jsonify({"status":200, "message":"Username exists"})

