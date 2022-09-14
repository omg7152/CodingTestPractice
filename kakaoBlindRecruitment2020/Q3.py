def solution(key, lock):

    n, m = len(lock), len(key)
    spin = 0

    keyCount = sum([sum(i) for i in key])
    lockCount = n * n - sum([sum(i) for i in lock])

    if lockCount > keyCount:
        return False

    dol = []
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                dol.append([i, j])

    while spin < 4:
        temp = []

        # 90도 회전
        for x, y in dol:
            temp.append([m - y - 1, x])

        dol = temp

        # 키 이동
        for i in range(-n + 1, n):
            for j in range(-n + 1, n):
                count = 0
                remain = False
                for dolx, doly in dol:
                    dx, dy = dolx + i, doly + j

                    if 0 <= dx < n and 0 <= dy < n:
                        if lock[dx][dy] == 0:
                            count += 1
                        else:
                            remain = True

                if count == lockCount and not remain:
                    return True
        spin += 1
   
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))