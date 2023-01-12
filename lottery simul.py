# -*- coding: utf-8 -*- 
import random
total=0
for j in range(10):
	def mtask(): 	# 1~45 숫자 집합을 자동으로 만들고 랩덤 당첨 집합 변수를 만드는 함수를 생성
		n = 1
		l = [1]

		for i in range(44):
		
			n = n + 1 
			l = l + [n]
		a = random.choice(l)

		l.remove(a) # 중복 출현 방지를 위해 출현 번호를 집합에서 제외

		b = random.choice(l)

		l.remove(b)
		c = random.choice(l)
		
		l.remove(c)
		d = random.choice(l)

		l.remove(d)
		e = random.choice(l)
		l.remove(e)
		f = random.choice(l)
		l.remove(f)
		global ans
		ans = [a, b, c, d, e, f] # 번호 집합 생성
		ans.sort()	# 숫자 크기로 재나열

		
	mtask()
	answer = ans	# 처음 mtask함수로 만들어진 전역변수 ans를 고정 당첨 번호로 지정한다.
	print ("시작....고정 당첨번호 집합은", answer , "입니다.")
	global tan
	tan = [0]
	line=0
	while answer != tan:	# 고정번호집합과 새로 생성된 집합이 나올때 까지 새로운 집합을 만드는 반복문을 실행한다. 
		line=line+1
		
		mtask()
		tan = ans
	total=total+line
	# 시간 측정 변수 생성 
print(total/10)

print ("\n종료 되었습니다.\n고정 번호은",answer,"이며,\n 마찬가지 겟팅 번호는",tan,"이며 총",line,"번 수행 하였습니다.\n그리고 이번 게임의 당첨 확률은 1/", line, " 입니다.")