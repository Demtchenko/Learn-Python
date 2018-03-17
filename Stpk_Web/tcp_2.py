import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',1234))
s.listen(10)
while True:
    conn,addr=s.accept()
    while True:
        data=conn.recv(1024)
        print(data.decode("utf-8"))
        if not data or data.decode('utf-8').strip()=='Exit': break
        conn.send(data)
    conn.close
