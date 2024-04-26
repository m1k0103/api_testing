from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from func import writeData, checkIfUserExists, passwordCheck

app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if checkIfUserExists(request.json) == False:
            if passwordCheck(request.json) == True:
                return jsonify({"status":401, "message":"bad password or user doesnt exist"})
        elif checkIfUserExists(request.json) == False:
            return jsonify({"status":200, "message":"not logged in"})
        else:
            return jsonify({"status":401, "message": "denied"})
    elif request.method == "GET":
        return render_template("login_page.html")
    
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup_page.html")
    elif request.method == "POST":
        if writeData(request.json) == False:
            return jsonify({"status":200, "message":"Signed up successfully"})
        elif writeData(request.json) == True:
            return jsonify({"status":200, "message":"Username exists"})

