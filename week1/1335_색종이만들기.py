#한가지 색이면 한 장으로 세고 섞여 있으면 4조각으로 잘라서 똑같이 반복


N = int(input())
paper = [] # 종이를 2차원 리스트로 저장
for i in range(N):
    row = list(map(int, input().split()))
    paper.append(row)

count = [0, 0]  # count[0]: 하얀색, count[1]: 파란색
"""
x : 시작 행
y : 시작 열
size : 한 변의 길이
"""

# (x, y)에서 시작하는 size×size 영역이 전부 같은 색인지 확인
def same(x, y, size):
    color = paper[x][y] # 왼쪽 위 칸을 기준 색으로
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                return False 
    return True 

def solve(x, y, size):
  
    if same(x, y, size):
        color = paper[x][y]
        count[color] += 1
        return

  # 섞여 있으면 반으로 잘라서 4조각 각각 다시 확인
    half = size // 2
    solve(x, y, half)
    solve(x, y + half, half)
    solve(x + half, y, half)
    solve(x + half, y + half, half)

solve(0, 0, N)
print(count[0])
print(count[1])
