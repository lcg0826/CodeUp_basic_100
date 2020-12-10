# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

n = int(input())

if n >= 90:
    print('A')
elif 70 <= n <= 89:
    print('B')
elif 40 <= n <= 69:
    print('C')
else:
    print('D')