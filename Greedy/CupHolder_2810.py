import sys;
import re;
cnt = int(sys.stdin.readline().rstrip());

sit = sys.stdin.readline().rstrip();

sit = re.sub('[L]{1,2}', 'L', sit);

if cnt > len(sit) + 1:
    print(len(sit) + 1);
else:
    print(cnt);