import hashlib

def registration():

    users = (input("users: "))
    password = (input("Enter your password: "))
    h_password = hashlib.md5(bytes(password, 'UTF-8'))
    users = h_password.hexdigest()
    Acc = dict()
    Acc[users] = password


    print(f"Users: {users}")
    print(f"Password: {h_password.hexdigest()}\n")

    enter = (input("Enter your Username: "))
    passw = int(input("Enter your password: "))
    EnterAcc = dict()
    EnterAcc[enter] = passw

    if Acc == EnterAcc:
        print("colision")

    if users or password == enter or passw :
        print("Succses")
    else:
        print("Tru again")

registration()
