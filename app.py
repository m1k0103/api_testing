from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

def writeData(data):
    to_write = f'{data["username"]}:{data["password"]}'
    to_write_split = to_write.split(":")
    with open("userNpass.txt", "r") as f:
        contents = f.readlines()
        for i in range(len(contents)):
            contents[i] = contents[i].replace("\n", "").split(":")
            if to_write_split[0] not in contents[i][0]:
                 continue
            else:
                 return False
            
    with open("userNpass.txt", "a") as f:
        f.write(f"{to_write}\n")
        return True

def checkIfUserExists(json):
    userdata = [json["username"],json["password"]]
    with open("userNpass.txt", "r") as f:
        contents = f.readlines()
        for i in range(len(contents)):
            contents[i] = contents[i].replace("\n", "").split(":")
            if userdata[0] in contents[i][0]:
                 return True
            else:
                 return False

app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if checkIfUserExists(request.json) == True:
            print(request.json)
            return jsonify({"status":401, "message":"bad password or user doesnt exist"})
        elif checkIfUserExists(request.json) == False:
            return jsonify({"status":200, "message":"logged in"})
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

