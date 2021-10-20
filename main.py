scorex=[]
namex=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    scorex.append(score)
    namex.append(name)

i = min(scorex)
flag = True
while flag:
    if i in scorex:
        namex.pop(scorex.index(i))
        scorex.pop(scorex.index(i))
    else:
        flag=False
t=min(scorex)
names=[]
flag=True

count =scorex.count(t)

for _ in range (count):
    names.append(namex[scorex.index(t)])
    namex.pop(scorex.index(t))
    scorex.pop(scorex.index(t))
names.sort()
for i in names:
    print i
    
