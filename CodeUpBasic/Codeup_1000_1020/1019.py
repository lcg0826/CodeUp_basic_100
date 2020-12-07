# 1019 : [기초-입출력] 연월일 입력받아 그대로 출력하기
# 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.

year, month, day = input().split('.')
print('%04d' % int(year), end='.')
print('%02d' % int(month), end='.')
print('%02d' % int(day))