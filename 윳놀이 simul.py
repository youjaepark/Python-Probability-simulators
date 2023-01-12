import random
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
my_list = []
counts = {'도': 0, '개': 0, '걸': 0, '윳': 0, '모': 0}
x = np.arange(5)
rot=1000000
def gamestart():
    my_list.clear()
    for i in range(1,5):
        my_list.append(random.randrange(0,2))

for j in range(rot):
    gamestart()
    if my_list.count(0) == 0:
        counts['윳'] += 1
    elif my_list.count(0) == 1:
        counts['도'] += 1
    elif my_list.count(0) == 2:
        counts['개'] += 1
    elif my_list.count(0) == 3:
        counts['걸'] += 1
    else:
        counts['모'] += 1

keylist=list(counts)
valuelist=list(counts.values())
finalvalue = [round(k / rot*100,3) for k in valuelist]
print(finalvalue)
plt.title('윳놀이 확률')
plt.bar(x, finalvalue ,width=0.6,color='red')
plt.xticks(x, keylist)
plt.ylabel('확률(%)')
plt.legend()
plt.show() 



        