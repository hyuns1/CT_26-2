#학생마다 종교 번호를 붙이고, 같은 종교 나오면 번호를 통일
n, m = map(int, input().split())

# religion[i]: i번 학생의 종교 번호. 처음엔 각자 자기 번호
religion = list(range(n + 1))

for t in range(m):
    line = input().split()
    while not line:
        line = input().split()
    i, j = map(int, line)

    a = religion[i]
    b = religion[j]
    if a == b:
        continue  # 이미 같은 종교면 할 일 없음

    # b번 종교를 가진 학생을 전부 a번 종교로 바꿈
    for k in range(1, n + 1):
        if religion[k] == b:
            religion[k] = a

# 서로 다른 종교 번호가 몇 개인지 세기
print(len(set(religion[1:])))

#시간 초과 나옴
