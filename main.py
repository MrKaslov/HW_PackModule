from PackModule import *

#Main
a = 1
user = ["Sanzhar", "Wasima", "Fayzrahman"]
print("Для получения сведений об командах наберите -help")

def menu(com):
    if com == "-help":
        Help.help_def()
        return
    if com == "-create_user_info":
        Creat.create_user_info(user)
        return
    if com == "-show_users":
        Show.show_users(user)
        return
    if com == "-export":
        TableUser.export(user)
        return
    if com == "-exit":
        return -1
    else:
        help()
        return

#Бесконечный цикл
while a != -1:
    com = input()
    a = menu(com)

