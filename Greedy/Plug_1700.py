import sys;

N, K = list(map(int, sys.stdin.readline().rstrip().split()));
kind = list(map(int, sys.stdin.readline().rstrip().split()));

plug = [];
result = 0;
for i in range(K):

    #플러그에 이미 꽂혀있으면 넘어감
    if kind[i] in plug:
        continue;

    #플러그에 안꽂혀있는데가 있으면 거기에 꽂음
    if len(plug) < N:
        plug.append(kind[i]);
        continue;

    idxs = [];
    for j in range(N):
        #남은 제품중 이미 플러그에 꽂혀있는 제품 인덱스 추가 없으면 101
        try:
            idx = kind[i:].index(plug[j]);
        except:
            idx = 101;
        idxs.append(idx);

    # 위에서 뽑은 인덱스중 제일 큰값 제거하고 현재값 추가
    out_plugIdx = idxs.index(max(idxs));
    del plug[out_plugIdx];
    plug.append(kind[i]);
    result += 1;

print(result);

