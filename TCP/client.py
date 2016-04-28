import socket
import time

TCP_IP = 'localhost'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
s.connect((TCP_IP, TCP_PORT))

while True:
    try:
        s.send(MESSAGE)
        print "Data sent"
        data = s.recv(BUFFER_SIZE)
        print "received data:", data
        time.sleep(1)

    except socket.timeout as e:
        print "exception: ", e

    except Exception, e:
        print "exception: ", e
        s.close()
        break

# s.close()

