import socket
import threading
from recog import jsonRec
import time
import json


listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.bind(('127.0.0.1',1234))
listener.listen()


print('Waiting for connect...')

def connection(client_executor, addr):

    json=""
    print('Accept new connection from %s:%s...' % addr)

    #recive
    while True:
        msg = client_executor.recv(1024)

        if not msg or msg.decode('utf-8') == 'exit':
            print('%s:%s request close' % addr)
            break
        json=json+msg.decode('utf-8')
        print('%s:%s: %s' % (addr[0], addr[1], json))


    client_executor.send(jsonRec(json).encode('utf-8'))
    client_executor.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    client_executor,addr=listener.accept()
    print('got connect...')
    print('addr=',addr)
    t=threading.Thread(target=connection,args=(client_executor,addr))
    t.start()




