import socket

HEADER = 64
PORT = 7750
FORMAT ='utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.0.9'

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg) :
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)

    # b indicates 'byte representation' of it's string 
    # 64에서 메시지의 크기를 나타내는 문자열의 크기만큼 뺀만큼을 공백으로 추가해준다. => '25                     '
    send_length += b' ' * (HEADER - len(send_length))  
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
input()
send("Hello Everyone!")
input()
send(DISCONNECT_MESSAGE)