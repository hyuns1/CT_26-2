# 정올 종교 - 유니온 파인드 (Union-Find) (AI)
#
# [문제 요약]
# 학생 n명, "같은 종교" 쌍 m개가 주어질 때 종교가 최대 몇 가지인지 구한다.
# 같은 종교로 이어진 학생들을 한 그룹으로 묶으면, 그룹 개수가 곧 답이다.
#
# [아이디어]
# 1. 처음엔 학생마다 각자 다른 그룹이라고 본다. → 그룹 수 = n
# 2. 쌍 (i, j)가 나올 때마다 두 학생의 그룹을 하나로 합친다.
# 3. 서로 다른 그룹이 합쳐질 때마다 그룹 수를 1 줄인다.
#
# [그룹 표현 방법: 대표]
# parent[x] = x의 바로 위 사람
# 위로 계속 따라 올라가서 꼭대기(parent[x] == x)에 있는 사람이 그룹의 대표다.
# 두 학생의 대표가 같으면 같은 그룹, 다르면 다른 그룹.
#
# [초보 방식과의 차이]
# 그룹을 합칠 때 그룹원 전원의 번호를 고치지 않고,
# 대표 한 명만 다른 대표 밑으로 붙인다. 그래서 훨씬 빠르다.

import sys
input = sys.stdin.readline  # 입력이 최대 10만 줄이라 빠른 입력 사용

n, m = map(int, input().split())  # n: 학생 수, m: 쌍 개수

# parent[x]: x의 바로 위 사람
# 처음엔 모두 자기 자신 → 각자 혼자서 그룹의 대표
# 학생 번호가 1부터라 n + 1칸을 만들고 0번 칸은 안 씀
parent = list(range(n + 1))


# x가 속한 그룹의 대표를 찾는 함수
def find(x):
    while parent[x] != x:              # 꼭대기에 도착할 때까지 올라감
        parent[x] = parent[parent[x]]  # 경로 압축: 내 위를 "위의 위"로 바꿔서 다음엔 더 빨리 찾게 함
        x = parent[x]                  # 한 칸 위로 이동
    return x                           # 꼭대기에 있는 사람이 대표


# a와 b가 속한 그룹을 하나로 합치는 함수
def union(a, b):
    ra = find(a)       # a의 대표
    rb = find(b)       # b의 대표
    if ra != rb:       # 대표가 다르면 (다른 그룹이면)
        parent[rb] = ra  # b 쪽 대표를 a 쪽 대표 밑으로 붙임 → b 그룹 전체가 따라옴


count = n  # 처음엔 학생 수만큼 그룹(종교)이 있음

for _ in range(m):
    line = input().split()
    while not line:              # 빈 줄이 있으면 숫자가 나올 때까지 다시 읽음
        line = input().split()
    i, j = map(int, line)        # i번, j번 학생은 같은 종교

    if find(i) != find(j):       # 아직 다른 그룹이면
        union(i, j)              # 하나로 합치고
        count -= 1               # 그룹이 하나 줄었으니 1 감소
    # 이미 같은 그룹이면 아무것도 안 함

print(count)  # 남은 그룹 수 = 종교의 최대 가지 수
