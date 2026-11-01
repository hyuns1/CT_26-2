x1, y1, x2, y2 = map(int, input().split())  # 박스 P
x3, y3, x4, y4 = map(int, input().split())  # 박스 Q

# 겹침 길이
w = min(x2, x4) - max(x1, x3)  # 가로 겹침
h = min(y2, y4) - max(y1, y3)  # 세로 겹침

if w < 0 or h < 0:        # 한 방향이라도 떨어지면 null
    print("NULL")
elif w == 0 and h == 0:   # 가로세로 둘 다 닿기만 함
    print("POINT")
elif w == 0 or h == 0:    # 한 방향만 닿기만 함
    print("LINE")
else:                     # 둘 다 겹침
    print("FACE")
