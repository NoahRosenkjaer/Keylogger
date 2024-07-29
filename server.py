import socket


def bind_socket(host, port, s):
    print("Binding port: " + str(port))
    try:
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket bind error: " + str(msg) + "\nRetrying.")
        bind_socket(host, port, s)

def accept_connection(s):
    conn, addr = s.accept()
    print(f"Connected to {addr[0]} on port {addr[1]}")
    receive(conn)
    conn.close()

def receive(conn):
    while True:
        response = str(conn.recv(1024), "utf-8")
        print(response, end="")
        with open("data.txt", "a")as file:
            file.write(str(response))

def main():
    host = ""
    port = 9999
    print("creating socket")
    s = socket.socket()

    bind_socket(host, port, s)
    accept_connection(s)

main()
