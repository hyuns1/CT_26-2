# 정올 3122 두 선분이 만나는 경우의 수 - CCW
# 두 선분이 만나려면 "서로가 서로의 반대편에 있어야" 한다
 
import sys
input = sys.stdin.readline
 
 
# A에서 B로 갈 때 C가 왼쪽이면 1, 오른쪽이면 -1, 일직선이면 0
def ccw(A, B, C):
    value = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0
 
 
def meet(A, B, C, D):
    # AB 기준으로 C, D가 어느 쪽인지 곱함 (음수면 반대편, 0이면 선 위)
    ab = ccw(A, B, C) * ccw(A, B, D)
    # CD 기준으로 A, B가 어느 쪽인지 곱함
    cd = ccw(C, D, A) * ccw(C, D, B)
 
    # 네 점이 전부 일직선 위에 있는 경우
    if ab == 0 and cd == 0:
        # 각 선분에서 작은 점이 앞에 오도록 정렬
        if A > B:
            A, B = B, A
        if C > D:
            C, D = D, C
        # 구간이 겹치면 만남
        return C <= B and A <= D
 
    # 서로가 서로의 반대편(또는 선 위)에 있으면 만남
    return ab <= 0 and cd <= 0
 
 
N = int(input())
seg = []
for i in range(N):
    sx, sy, ex, ey = map(int, input().split())
    seg.append(((sx, sy), (ex, ey)))  # (시작점, 끝점)
 
# 모든 두 선분 쌍을 확인
cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if meet(seg[i][0], seg[i][1], seg[j][0], seg[j][1]):
            cnt += 1
 
print(cnt)
