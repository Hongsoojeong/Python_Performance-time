import time, random

def sum(A, n):
	start=time.time()
	List_1=list()  # 리스트 A
	List_2=list()() # 리스트 B
	for i in range(0,n):
		A=random.randrange(1,101)
		List_1.append(A)
		# 리스트 A에 랜덤 정수 값 n개 채움
	for i in range(0,n):
			for j in range(0,i+1):
					List_2[i][j]+=List_1[i]
	return start;
	
	# code here

n=int(input())
# n = 1 이상 5000 이하 정수 값 입력
start=time.time()
print(time.time()-start)
# sum 함수 호출 + 시간 측정
# 함수의 수행시간을 출력
