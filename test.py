data = {'username': 'test', 'password': '1234'}

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
                 return {"status":403, "message":"user already registered"}
    with open("userNpass.txt", "a") as f:
        f.write(f"{to_write}\n")
    

def readData(data):
    with open("userNpass.txt", "r") as f:
            contents = f.readlines()
            for i in range(len(contents)):
                contents[i] = contents[i].replace("\n", "").split(":")

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

print("a")