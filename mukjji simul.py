import random
num=int(input("하는 사람 수: "))
option=['묵','찌']
resultlist=[]
count=1
def gamestart():
    resultlist.clear()
    for i in range(1,num+1):
        globals()['person_{}'.format(i)] = random.choice(option)
        resultlist.append(globals()['person_{}'.format(i)])
      
while True:
    gamestart()
    print(resultlist)
    if (resultlist.count('묵') == resultlist.count('찌')):
        print(f'{count}번 만에 끝')
        break
    elif(abs(resultlist.count('묵') - resultlist.count('찌')) == 1):
        print(f'{count}번 만에 끝')
        break
    else:
        count += 1
