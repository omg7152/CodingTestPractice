import sys;
import re;
msg = sys.stdin.readline().rstrip();
alp = ['U', 'C', 'P', 'C'];

msg = re.sub('[^UCP]', '', msg);
check = True;
for i in range(4):
    if alp[i] in msg:
        check = True;
        msg = msg[msg.find(alp[i]) + 1:]
    else:
        check = False;
        break;

if check:
    print("I love UCPC");
else:
    print("I hate UCPC");

