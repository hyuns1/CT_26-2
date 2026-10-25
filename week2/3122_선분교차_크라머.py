# 정올 3122 두 선분이 만나는 경우의 수 - 교점 구하기 (크라머 공식)
# 직선을 a*x + b*y = c 꼴로 바꾸고, 크라머 공식으로 교점을 구한 뒤
# 교점이 두 선분 범위 안에 있는지 확인
 
import sys
input = sys.stdin.readline  # 입력이 많아서 빠른 입력 사용
 
 
def meet(s1, s2):
    x1, y1, x2, y2 = s1
    x3, y3, x4, y4 = s2
 
    # 직선을 a*x + b*y = c 꼴로 (세로선도 나눗셈 없이 표현 가능)
    a1, b1 = y2 - y1, x1 - x2
    c1 = a1 * x1 + b1 * y1
    a2, b2 = y4 - y3, x3 - x4
    c2 = a2 * x3 + b2 * y3
 
    # 크라머 공식의 분모, 0이면 평행
    D = a1 * b2 - a2 * b1
 
    if D == 0:
        # 서로 다른 직선이면 안 만남 (점짜리 선분 때문에 양쪽 다 확인)
        if a1 * x3 + b1 * y3 != c1 or a2 * x1 + b2 * y1 != c2:
            return False
        # 같은 직선이면 x 구간, y 구간이 둘 다 겹치는지
        x_overlap = max(min(x1, x2), min(x3, x4)) <= min(max(x1, x2), max(x3, x4))
        y_overlap = max(min(y1, y2), min(y3, y4)) <= min(max(y1, y2), max(y3, y4))
        return x_overlap and y_overlap
 
    # 교점 = (X / D, Y / D), 소수 오차 막으려고 나누지 않음
    X = c1 * b2 - c2 * b1
    Y = a1 * c2 - a2 * c1
 
    # D를 양수로 맞춰야 부등호 방향이 안 바뀜
    if D < 0:
        D, X, Y = -D, -X, -Y
 
    # 교점이 두 선분의 x, y 범위 안에 있는지 (양변에 D를 곱해서 비교)
    return (min(x1, x2) * D <= X <= max(x1, x2) * D and
            min(y1, y2) * D <= Y <= max(y1, y2) * D and
            min(x3, x4) * D <= X <= max(x3, x4) * D and
            min(y3, y4) * D <= Y <= max(y3, y4) * D)
 
 
N = int(input())
seg = []
for i in range(N):
    seg.append(tuple(map(int, input().split())))
 
# 모든 두 선분 쌍을 확인
cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if meet(seg[i], seg[j]):
            cnt += 1
 
print(cnt)
