# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.

n, m, k = map(int, input().split())

if n % 2 == 0:
    print(n)
if m % 2 == 0:
    print(m)
if k % 2 == 0:
    print(k)