# 정수가 순서대로 입력된다.

li = list(map(int, input().split()))

for i in li:
    if i == 0:
        break;
    else:
        print(i)
    