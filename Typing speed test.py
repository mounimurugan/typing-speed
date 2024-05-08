from time import time
print("press enter to start typing or to break a new line")
print("press enter twice to finish typing")
input("------")
wordcount=len(input())
start=time()
text=[]
while True :
    line=input()
    if not line:
        break
        text.append(line)
end=time()
timetaken=round(end-start)
wpm=round(wordcount/timetaken)
print("Wpm:",wpm,"Timetaken:",timetaken)
if wpm < 30:
    print('you should learn the proper typing technique .')
elif wpm < 40:
    print('not bad, but still below average.')
elif wpm < 60:
    print('congratulations! you are above average.')
else:
    print('this is speed required for most jobs you. ')

