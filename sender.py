import os
import socket
import random
import sys
import time
from colored import fg, bg, attr

ip = "192.168.1.117"
port = 5001
msg = input("Message to send: ").encode("utf-8")

duration = 5
timeout = time.time() + duration
sent = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    if time.time() > timeout:
        break
    else:
        try:
            sock.sendto(msg, (ip, port))
            sent = sent + 1
            print(f"%s[{sent}] %s Sending UDP Messages to %s{ip}:{port} %s==> %s[MESSAGE CONTENT: {msg.decode('utf-8')}]" % (fg(50), fg(162), fg(202), fg(1),attr(0)))
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("%sEXIT" % fg(196), attr(0))
            sys.exit()