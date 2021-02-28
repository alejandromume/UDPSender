import os
import socket
import random
import sys
import time
from colored import fg, bg, attr

prefix = ("%s[~]%s" % (fg(50), attr(0)))

ip = input(f"{prefix} IP: ")
port = int(input(f"{prefix} PORT: "))
duration = int(input(f"{prefix} SECONDS: "))
msg = input(f"{prefix} Message to send: ").encode("utf-8")
print("")
timeout = time.time() + duration
sent = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f" ╦")
print(f" ║")
while True:
    if time.time() > timeout:
        break
    else:
        try:
            sock.sendto(msg, (ip, port))
            sent = sent + 1
            print(f" ╠════>   %s[{sent}] %s Sending UDP Messages to %s{ip}:{port} %s==> %s[MESSAGE CONTENT: {msg.decode('utf-8')}]" % (fg(50), fg(162), fg(202), fg(1),attr(0)))
            print(f" ║")
            time.sleep(0.2)
            input("")
        except KeyboardInterrupt:
            print("%sEXIT" % fg(196), attr(0))
            sys.exit()