# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10
# 
# 
# 참고
# 예를 들어 1 3 이 입력되면 1을 23(8)배 하여 출력한다.

n, m = map(int, input().split())
print(n << m)