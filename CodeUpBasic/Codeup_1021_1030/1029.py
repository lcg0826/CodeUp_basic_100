# 1029 : [기초-데이터형] 실수 1개 입력받아 그대로 출력하기2(설명)
# 실수 1개를 입력받아 그대로 출력해보자.
# (단, 입력되는 실수의 범위는 +- 1.7*10-308 ~ +- 1.7*10308 이다.) 

# 참고
# float 데이터형을 사용하면 +- 3.4*10-38 ~ +- 3.4*1038 범위의 실수를 저장할 수 있다.
# (float 로 선언하고 %f로 입력 받아 출력하면 된다.)


# 문제에서 원하는 답은 소수점 11번째 자리 까지였다.
n = float(input())
print('%.11f' % n)