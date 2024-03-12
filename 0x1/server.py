import socket


def listen():
    HOST = ''
    PORT = 8080
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv = (HOST,PORT)
    tcp.bind(srv)
    tcp.listen(1)
    while True:
        con, cliente = tcp.accept()
        print(f'Conectado por {cliente}')
        while True:
            msg = con.recv(2048)
            if not msg: break
            print(f'{cliente}: {msg}')
        print('Encerrando...')
        con.close()
        break
listen()