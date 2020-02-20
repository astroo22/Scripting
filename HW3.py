#! python3
import random

basicList = []
tempList = []
number = random.randint(0,9)
i=0
thing = 'false'
while i<10:
    basicList.append(input('Please enter ' + str(10-i) + ' more things \n'))
    #basicList.append('cat' + str(i))
    i+=1
print(basicList)
if len(basicList) == 10:
    print('list has 10 items. true')

one = basicList[0]
basicList[0] = basicList[9]
basicList[9] = one
print('First 3')
print(basicList[:3])
print('Last 3')
print(basicList[-3:]) 
print('Full list')
print(basicList[:10])
for i in basicList:
    if any("cat" in s for s in basicList):
        thing = 'true'
print('There is a cat in this list. ' + thing)
marvel = input('Please name you favorite marvel character ')
basicList.insert(number,marvel)
print('The ' + marvel + ' is at index ' + str(number))
for i in range(len(basicList)):
    try:
        int(basicList[i])
        tempList.append(basicList[i])
    except Exception:
       continue
tempList.sort()
print(tempList)
basicList = tuple(basicList)
try:
    basicList[0] = 'cat'
except Exception as e:
    print('Tuples are immutable!')
print(basicList)
