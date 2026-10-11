# 빨리 끝나는 회의부터 잡아야 뒤에 회의를 더 넣을 수 있다.

N = int(input())  # 회의 개수

# 회의 정보를 (번호, 시작, 끝) 튜플로 묶어서 저장
meetings = []
for i in range(N):
    num, start, end = map(int, input().split())
    meetings.append((num, start, end))

# 끝나는 시간 기준으로 정렬 (m[2]가 끝나는 시간)
meetings.sort(key=lambda m: m[2])

chosen = []    # 내가 고른 회의 번호들
last_end = 0   # 마지막으로 고른 회의가 끝나는 시간

for num, start, end in meetings:
    # 이전 회의가 끝난 뒤에 시작하면 고를 수 있음
    # 끝 = 시작이면 안 겹치니까 >= 로 비교
    if start >= last_end:
        chosen.append(num)
        last_end = end  # 기준 시간 갱신

# 고른 개수랑 번호 출력
print(len(chosen))
print(*chosen)  # 리스트를 띄어쓰기로 출력
