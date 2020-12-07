# 1025 : [기초-입출력] 정수 1개 입력받아 나누어 출력하기(설명)
# 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.

n = input()

print('[%d]' % (int(n[0]) * 10000))
print('[%d]' % (int(n[1]) * 1000))
print('[%d]' % (int(n[2]) * 100))
print('[%d]' % (int(n[3]) * 10))
print('[%d]' % (int(n[4]) * 1))

# 모범답안
n=input()

print("["+str(int(n[0])*10000)+"]")
print("["+str(int(n[1])*1000)+"]")
print("["+str(int(n[2])*100)+"]")
print("["+str(int(n[3])*10)+"]")
print("["+str(int(n[4]))+"]")
