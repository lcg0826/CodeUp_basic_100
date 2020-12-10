# 두 가지의 참(1) 또는 거짓(0)이 입력될 때,
# 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.

n, m = map(int, input().split())
b = bool(n)
b1 = bool(m)

if b != b1:
    print(1)
else:
    print(0)