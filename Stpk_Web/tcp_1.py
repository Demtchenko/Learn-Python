import socket,os,sys

req = 'Hello TCP'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# os.sleep(600)
s.connect(('127.0.0.1', 1234))
s.send(req)
rsp = s.recv(1024)
s.close
