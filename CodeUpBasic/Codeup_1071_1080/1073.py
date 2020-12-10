# 정수가 순서대로 입력된다.
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
li = list(map(int, input().split()))
for i in li:
    if i == 0:
        break;
    else:
        print(i)
    