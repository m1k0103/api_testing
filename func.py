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
            
def passwordCheck(json):
    password = json["password"]
    with open("userNpass.txt", "r") as f:
        contents = f.readlines()
        for i in range(len(contents)):
            contents[i] = contents[i].replace("\n", "").split(":")
        if password in [contents[i][1] for i in range(len(contents))]:
            return True
        else:
            return False