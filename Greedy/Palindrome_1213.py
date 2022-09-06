import sys;
msg = sys.stdin.readline().rstrip();
alp = [0 for _ in range(26)];

for i in range(len(msg)):
    alp[ord(msg[i]) - 65] += 1;

single = '';
result = "";
for i in range(26):
    if alp[i] % 2 == 1:
        single += chr(i + 65);
    
    result += chr(i + 65) * (alp[i] // 2);

if len(single) > 1:
    print("I'm Sorry Hansoo");
else:
    print(result + single + result[::-1]);
