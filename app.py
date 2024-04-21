from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        data = request.json
        #basic user data storing tests
        usrdata = [data["username"], data["password"]]
        with open("./users.txt", "r") as f:
            contents = [i.strip("\n").split(":") for i in f.readlines()]
            for i in range(len(contents)):
                if usrdata[0] in contents[i]:
                    if usrdata[1] in contents[i]:
                        return jsonify({"registered":True}) 
            return jsonify({"registered":False})
    elif request.method == "GET":
        return render_template("login_page.html")
    
@app.route("/signup", route=["GET", "POST"])
def signup():
    if request.method == "POST": # TO DO: create signup functionality
        pass
    elif request.method == "GET":
        return render_template("signup.html")