# https://blog.naver.com/gohongfight/223396869788 정리한 내용
# 예시 동전문제
def coin_change(money):
    coins = [500, 100, 50, 10]
    count = 0
    for coin in coins:
        cnt = money // coin  # 해당 동전으로 거슬러 줄 수 있는 개수
        count += cnt
        money %= coin
        print(f"{coin}원 동전: {cnt}개")
    print(f"총 동전 개수: {count}개")


# 사용 예시
coin_change(1260)
# 500원 동전: 2개
# 100원 동전: 2개
# 50원 동전: 1개
# 10원 동전: 1개
# 총 동전 개수: 6개
