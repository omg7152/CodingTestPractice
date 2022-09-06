import sys

msg = sys.stdin.readline().rstrip()

msg = msg.replace("XXXX", "AAAA")
msg = msg.replace("XX", "BB")

if msg.find("X") == -1:
    print(msg)
else:
    print(-1)