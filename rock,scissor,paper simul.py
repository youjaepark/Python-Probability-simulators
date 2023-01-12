import random
rpclist=["rock","paper","scissor"]
equal=0
rot=1000000
for i in range(rot):
    person1= random.choice(rpclist)
    person2= random.choice(rpclist)
    person3= random.choice(rpclist)
    person4= random.choice(rpclist)
    resultlist=[person1,person2,person3,person4]
    if person1==person2==person3==person4:
        equal+=1
    elif "scissor" in resultlist:
        if "rock" in resultlist:
            if "paper" in resultlist:
                equal+=1
pro=equal/rot*100
print(round(pro,3))

    