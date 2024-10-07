# 입력 받기
r_max, g_max, b_max = map(int, input().split())

# 색상 조합 리스트 초기화
colors = []

# 모든 조합 생성
for r in range(r_max):
    for g in range(g_max):
        for b in range(b_max):
            colors.append((r, g, b))

# 색상 조합 출력
for color in colors:
    print(color[0], color[1], color[2])

# 총 색상 수 출력
print(len(colors))
