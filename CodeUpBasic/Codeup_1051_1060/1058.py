# 두 개의 참(1) 또는 거짓(0)이 입력될 때,
# 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.

n, m = map(int, input().split())
b = bool(n)
b1 = bool(m)

if b == False and b1 == False:
    print(1)
else:
    print(0)