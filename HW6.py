import os
import shelve
import pprint
library='C:\\Users\\astro\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\'
os.chdir('C:\\Users\\astro\\Desktop\\')

file = open('.\\data.csv')
l =[]
d ={}
if(os.path.exists('myData.dat')):
    os.remove('myData.dat')
    os.remove('myData.bak')
    os.remove('myData.dir')
temp = file.readlines()
counter =0
for y in temp:
    l.append(y.split(','))
    if(l[counter][3].isupper()):
        #print(l[counter][3])
        d[l[counter][3]]= {'StateC': l[counter][0],'CountryC':l[counter][1],'SateAb':l[counter][2],'numTaxR':l[counter][4],'numExm':l[counter][5],'grossIn':l[counter][6],'wagesNsal':l[counter][7],'div':l[counter][8],'interest':l[counter][9]}
        shelfFile = shelve.open('myData')
        shelfFile['state_info'] = d
        shelfFile.close()
    counter +=1
state_data = shelve.open('mydata')
#print(state_data['state_info'])
d2 ={}
taxtemp = ''
exmtemp = ''
divtemp = ''
inttemp = ''
gostemp = ''
state_list =[]
for y in state_data['state_info']:
    for x in state_data['state_info'][y]['numTaxR']:
        taxtemp += x
        #stateList.append(x.split(','))
    for z in state_data['state_info'][y]['numExm']:
        exmtemp += z
    for q in state_data['state_info'][y]['div']:
        divtemp += q
    for t in state_data['state_info'][y]['interest']:
        inttemp += t
    for p in state_data['state_info'][y]['grossIn']:
        gostemp += p
    tempAvgEXM = float(float(exmtemp)/float(taxtemp))
    tempCapInc = float((float(divtemp)+float(inttemp))/float(gostemp))
    taxtemp = ''
    exmtemp = ''
    divtemp = ''
    inttemp = ''
    gostemp = ''
    d2 = [{y:[tempAvgEXM,tempCapInc]}]
    state_list.append(d2)
state_data.close()
os.chdir(library)
if(os.path.exists('state_data.py')):
    os.remove('state_data.py')
state_data_module = open('state_data.py','w')
state_data_module.write('state_data='+pprint.pformat(state_list)+'\n')
state_data_module.close()
import state_data
exm = 0
cap =0
for x in state_data.state_data:
    for y in x:
        for z in y:
            exm += float(y[str(z)][0])
            cap += float(y[str(z)][1])
print('The average number of exceptions per return is: ' + str(round(float(exm/51),2)))
print('The average amount of capital income to AGI is: ' + str(round(float(cap/51),2)))
