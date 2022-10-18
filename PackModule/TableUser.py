def export(user):
    file = open("UserInfo.txt", 'w')
    for i in range(len(user)):
        file.write(user[i] + "\n");
    print("Saved")
