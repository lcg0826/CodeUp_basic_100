# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

n=input()

n=ord(n)
i=ord('a')

while i<=n :
    print(chr(i), end=' ')
    i+=1