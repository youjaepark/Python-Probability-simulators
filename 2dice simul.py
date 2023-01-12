#모듈 가져오기
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#기본 세팅
sumdicelist1=[]
sumdicelist2=[]
valuelist1=[]
valuelist2=[]
answerwaylist=[2,3,4,5,6,7,8,9,10,11,12]
originaldice=[1,2,3,4,5,6]
strangedice1=[1,2,2,3,3,4]
strangedice2=[1,3,4,5,6,8]
barwidth=0.4
x = np.arange(len(answerwaylist))
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
loopnumber=int(input('실행횟수를 입력하세요: '))
#일반주사위 굴리기
for i in range(loopnumber):
    dice1=random.choice(originaldice)
    dice2=random.choice(originaldice)
    sumdicelist1.append(dice1+dice2)
    sumdice1=0
for k in range(2,13,1):
    numberofn1=sumdicelist1.count(k)
    ratio1= numberofn1/loopnumber*100
    valuelist1.append(ratio1)
#이상한 주사위 굴리기
for j in range(loopnumber):
    dice3=random.choice(strangedice1)
    dice4=random.choice(strangedice2)
    sumdicelist2.append(dice3+dice4)
    sumdice2=0
for l in range(2,13,1):
    numberofn2=sumdicelist2.count(l)
    ratio2= numberofn2/loopnumber*100
    valuelist2.append(ratio2)
graphxvalue1=np.round(valuelist1,2)
graphxvalue2=np.round(valuelist2,2)


#그래프그리기
plt.title('주사위 두개의 눈의 합 분포도')
plt.xlabel('2개의 주사위 눈의 합')
plt.ylabel('비율(%)')
plt.bar(x, graphxvalue1, color='red', align='edge',width=barwidth,label='일반 주사위')
plt.bar(x+barwidth, graphxvalue2, color='blue', align='edge',width=barwidth,label='이상한 주사위')
plt.xticks(x+barwidth, answerwaylist)
plt.legend()
plt.show()

