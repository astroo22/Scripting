#!python3
import os,shutil,zipfile,shelve,pprint
from datetime import date
desktop = 'C:\\Users\\astro\\Desktop'
currentpath = 'C:\\Users\\astro\\Desktop'
clientdatpath ='C:\\Users\\astro\\Desktop\\Client_Data'
libpath = 'C:\\Users\\astro\\AppData\\Local\\Programs\\Python\\Python37\\Lib'
#checks if it exists deletes if it does ~mostly for testing
os.chdir(currentpath)
if(os.path.exists('Client_Data')):
    shutil.rmtree('Client_Data')
#creates directory structure as defined in assignment
os.makedirs('Client_Data')
currentpath = os.path.join(currentpath, 'Client_Data')
os.chdir(currentpath)
os.makedirs('Data')
currentpath = os.path.join(currentpath, 'Data')
print(currentpath)
temp = "prospect_list_8428c2.csv"
#userfile = input("What is the file name and extension for this nonsence")
#variable list
#list of everything imported this time o tits i need to fix this !!!!
l = []
#temp numbers for use in fun percentset() values are irrelavent 
maxv = 100
lowv = 100000
valperPercent = 0
#these are the dictionaries that are used for copyfun d is used for part 1 d2 is for part2
d = {}
d2 = {}
#actual reject list is r ~
r = {}
#kinda obvious
print2screen = False
print2file = False
print2both = False
#These are bool tests that I needed to be global name doesn't really matter its mostly just
#for if this should continue or not
test = True
test2 = True
#basic starting function creates the shelf and the phone module 
def copyfun(filename):
    z =0
    file = open(os.path.join(".\\",filename))
    os.chdir(currentpath)
    for y in file:
        if check(y):
            l.append(y.split(','))
            #print(y)
            d[l[z][0]] = {'Full Name': str(l[z][0]), 'CPhone1': str(l[z][1]), 'caddress': l[z][2], 'ccity': l[z][3], 'cstate': l[z][4], 'czip':l[z][5],'dob':l[z][6] , 'salary':l[z][7], 'Company':l[z][8]}
            d2[l[z][0]] = {'Full Name': str(l[z][0]), 'CPhone1': str(l[z][1]),'caddress': l[z][2], 'ccity': l[z][3], 'cstate': l[z][4], 'czip':l[z][5],'Company':l[z][8],'dob':l[z][6] }
            z += 1
        else:
            print('rejected ' + y)
    shelfFile = shelve.open('Clients')
    shelfFile['Client_Info'] = d
    shelfFile.close()
    pprint.pformat(d2)
    os.chdir(libpath)
    fileObj = open('phone.py','w')
    fileObj.write('d2=' + pprint.pformat(d2) + '\n')
    fileObj.close()
    os.chdir(currentpath)
    percentset()
def check(x):
    x = x.split(',')
    global d
    global r
    dupe = False
    reject = False
    for z in d:
        #print(x[0] + ' ' + str(d[z]['Full Name']))
        if x[0] in str(d[z]['Full Name']):
            #print(x[6] + ' ' + d[z]['dob'])
            if x[6] in d[z]['dob']:
                dupe = True
                #print('dupe = true')
    for z in r:
        if x[0] in r[z]['Full Name']:
            if x[6] in r[z]['dob']:
                reject = True
                print('reject = true')
    if dupe or reject:
        return False
        #print('rejected')
    else:
        return True
#first option on phone part
def phoneSearch1():
    selection = input('Please type as much of the clients name as you can \n')
    selection = selection.lower()
    temp = partialEntry(selection)
    if(temp == 1):
        import phone
        p = phone.d2
        for x in p:
            x2 = x.lower()
            if str(selection) in str(x2):
                print(x + ', ' + p[x]['caddress'] + ', ' + p[x]['ccity'] + ', ' + p[x]['cstate'] + ' ' + p[x]['czip'])
    if temp >1:
        print('Please use the names above to refine your search')
        phoneSearch1()
    if temp == 0:
        print('There were no results found please try again')
        phoneSearch1()
#required partial entry function
def partialEntry(name):
    import phone
    p = phone.d2
    results =0
    l =[]
    for x in p:
        x2 = x.lower()
        if name in x2:
            results += 1
            l.append(x)
    if results > 1:
        print('Multiple results found')
        for i in len(l):
            print(str(l[i]))
    return results
#second option on phone thing
def phoneSearch2():
    selection = input('What State would you like to search in? \n')
    import phone
    p = phone.d2
    for x in p:
        if str(selection) in p[x]['cstate']:
            print(x + ', ' + p[x]['caddress'] + ', ' + p[x]['ccity'] + ', ' + p[x]['cstate'] + ' ' + p[x]['czip'])
#third option on phone thing
def phoneSearch3():
    selection = input('What company would you like to find? \n')
    import phone
    p= phone.d2
    for x in p:
        if str(selection) in p[x]['Company']:
            print(x + ', ' + p[x]['caddress'] + ', ' + p[x]['ccity'] + ', ' + p[x]['cstate'] + ' ' + p[x]['czip'])      
#fourth option on phone thing
def phoneSearch4():
    print('What region would you like to search in?')
    print('\t Northeast: Connecticut, Maine, Massachusetts, New Hampshire')
    print('\t Northeast:Rhode Island, Vermont, New Jersey, New York, Pennsylvania')
    print('\t Midwest: Illinois, Indiana, Michigan, Ohio, and Wisconsin')
    print('\t Midwest: Iowa, Kansas, Minnesota, Missouri, Nebraska')
    print('\t Midwest: North Dakota, and South Dakota')
    print('\t South: Delaware, Florida, Georgia, Maryland, North Carolina, South Carolina')
    print('\t South: Virginia, District of Columbia, West Virginia, Alabama, Kentucky')
    print('\t South: Mississippi, Tennessee, Arkansas, Louisiana, Oklahoma, and Texas')
    print('\t West: Arizona, Colorado, Idaho, Montana, Nevada, New Mexico')
    print('\t West: Utah, Wyoming, Alaska, California, Hawaii, Oregon, and Washington')
    selection = input('Type "1" for Northeast, "2" for Midwest, "3" for South, "4" for west \n')
    import phone
    p = phone.d2
    if(str(selection) == '1'):
        for x in p:
            if 'ME' or 'NH' or 'MA' or 'CT' or 'NY' or 'PA' or 'NJ' or 'RI' or 'VT' in p[x]['cstate']:
                print(x + ', ' + p[x]['caddress'] + ', ' + p[x]['ccity'] + ', ' + p[x]['cstate'] + ' ' + p[x]['czip']) 
    if(str(selection) == '2'):
        for x in p:
            if 'IL' or 'WI' or 'IN' or 'OH' or 'MI' or 'MN' or 'IA' or 'MO' or 'ND' or 'SD' or 'NE' or 'KS' in p[x]['cstate']:
                print(x + ', ' + p[x]['caddress'] + ', ' + p[x]['ccity'] + ', ' + p[x]['cstate'] + ' ' + p[x]['czip']) 
    if(str(selection) == '3'):
        for x in p:
            if 'OK' or 'TX' or 'LA' or 'AR' or 'MS' or 'AL' or 'FL' or 'GA' or 'SC' or 'NC' or 'TN' or 'KY' or 'WV' or 'VA' or 'MD' or 'DC' or 'DE' in p[x]['cstate']:
                print(x + ', ' + p[x]['caddress'] + ', ' + p[x]['ccity'] + ', ' + p[x]['cstate'] + ' ' + p[x]['czip']) 
    if(str(selection) == '4'):
        for x in p:
            if 'WA' or 'OR' or 'CA' or 'NV' or 'ID' or 'MT' or 'WY' or 'UT' or 'CO' or 'AZ' or 'NM' in p[x]['cstate']:
                print(x + ', ' + p[x]['caddress'] + ', ' + p[x]['ccity'] + ', ' + p[x]['cstate'] + ' ' + p[x]['czip']) 
#deletes client
def removeClient():
    selection = input('Please type in as much of the name of client you want to remove as you can \n')
    selection = selection.lower()
    temp = partialEntry(selection)
    global r
    if(temp == 1):
        import phone
        p = phone.d2
        for x in p:
            x2 = x.lower()
            if str(selection) in str(x2):
               # print(p[x]['Full Name'])
                r[str(p[x]['Full Name'])] = { 'Full Name': str(p[x]), 'dob': str(p[x]['dob'])}
                #print('deleting ' + str(p[x]))
                del p[x]
                break
        #print(r)
    if(temp > 1):
        print('Please use the names above to refine your search')
        removeClient()
    if(temp == 0):
        print('There were no results found please try again')
        removeClient()
    
#base menu function yes it has an e after the U i know dont @me
def menuefun():
    print('Type the number of your selection')
    print('1. for Reports ')
    print('2. for phone directory')
    print('3. for importing')
    selection = input('4. for deletion \n')
    print()
    if str(selection) == '1':
        reportsFunction()
        menue1()
    if str(selection) == '2':
        menue2()
    if str(selection) == '3':
        menue3()
    if str(selection) == '4':
        removeClient()
        menuefun()
#YES I CONTINUED THE MISSPELLING CAUSE I CAN
#made a function just so i could recursively call it
def menue2():
    print('1. Look up a single person')
    print('2. Look up everyone in a specific state')
    print('3. Look up everyone in a specific company')
    selection = input('4. Look up everyone in a specific region\n')
    if str(selection) == '1':
        phoneSearch1()
    if str(selection) == '2':
        phoneSearch2()
    if str(selection) == '3':
        phoneSearch3()
    if str(selection) == '4':
        phoneSearch4()
#same as above
def menue1():
    print('1. Browse Data')
    print('2. Creep Salaries by % compared to others')
    print('3. Statistics by age')
    selection = input('4. Creep Salaries by location \n')
    if str(selection) == '1':
        firstSelection()
    if str(selection) == '2':
        secondSelection()
    if str(selection) == '3':
        thirdSelection()
    if str(selection) == '4':
        fourthSelection()
def menue3():
    print('Please place the file on your desktop')
    os.chdir(desktop)
    filename = input('What is the name of the file including extension \n')
    temp = os.path.join(desktop,filename)
    if(os.path.exists(temp)):
        copyfun(temp)
    else:
        print('Couldn\'t find the file please try again')
        menue3()
    os.chdir(currentpath)
#function that just does some base math at the start for calculating average
#answers used in fourthSelection()
def percentset():
    data = shelve.open('Clients')
    global maxv
    global lowv
    global valperPercent
    for x in data['Client_Info']:
        tempval =str(data['Client_Info'][x]['salary'])
        if(tempval != 'salary'):
            if float(tempval) > maxv:
                maxv = float(tempval)
            if float(tempval) < lowv:
                lowv = float(tempval)
    valperPercent = (maxv - lowv)/100
    data.close()
#first selection       
def firstSelection():
    data = shelve.open('Clients')
    selection = input('What company, state or city are you searching in? \n')
    ls = []
    temp = ""
    if print2file or print2both:
        os.chdir(clientdatpath)
        filename = str(selection) + 'SearchAt' + str(date.today())
        file = open(filename, "w")
        os.chdir(currentpath)
    for x in data['Client_Info']:
        if (selection in data['Client_Info'][x]['ccity']) or (selection in data['Client_Info'][x]['cstate']) or (selection in data['Client_Info'][x]['Company']):
            if(print2screen):
                print(str(data['Client_Info'][x]['Full Name'].strip('\':,')) + ' Works at: ' + str(data['Client_Info'][x]['Company']).strip('\':,\\n') + ' Makes: $' + str(data['Client_Info'][x]['salary']).strip('\':,\\n'))
            if(print2file):
                file.write(str(data['Client_Info'][x]['Full Name'].strip('\':,')) + ' Works at: ' + str(data['Client_Info'][x]['Company']).strip('\':,\\n') + ' Makes: $' + str(data['Client_Info'][x]['salary']).strip('\':,\\n') + '\n')
            if(print2both):
                file.write(str(data['Client_Info'][x]['Full Name'].strip('\':,')) + ' Works at: ' + str(data['Client_Info'][x]['Company']).strip('\':,\\n') + ' Makes: $' + str(data['Client_Info'][x]['salary']).strip('\':,\\n')+ '\n')
                print(str(data['Client_Info'][x]['Full Name'].strip('\':,')) + ' Works at: ' + str(data['Client_Info'][x]['Company']).strip('\':,') + ' Makes: $' + str(data['Client_Info'][x]['salary']).strip('\':,'))
    data.close()
    file.close()
#second option 
def secondSelection():
    data = shelve.open('Clients')
    selection = input('What % of salaries are you looking for? \n')
    temp = valperPercent * float(selection)
    temp = maxv - temp
    if print2file or print2both:
        os.chdir(clientdatpath)
        filename = 'The top ' + selection + '% of slaries ' + str(date.today())
        file = open(filename, "w")
        os.chdir(currentpath)
    print('Here are the Salaries of the people in the top ' + str(selection) + '%. \n')
    for x in data['Client_Info']:
        if(str(data['Client_Info'][x]['salary']) != 'salary'):
            if float(data['Client_Info'][x]['salary']) >= temp:
                if(print2screen):
                    print(str(data['Client_Info'][x]['Full Name'].strip('\':,')) + ' salary of: ' + str(data['Client_Info'][x]['salary']).strip('\':,'))
                if(print2file):
                    file.write(str(data['Client_Info'][x]['Full Name'].strip('\':,')) + ' salary of: ' + str(data['Client_Info'][x]['salary']).strip('\':,') + '\n')
                if(print2both):
                    print(str(data['Client_Info'][x]['Full Name'].strip('\':,')) + ' salary of: ' + str(data['Client_Info'][x]['salary']).strip('\':,'))
                    file.write(str(data['Client_Info'][x]['Full Name'].strip('\':,')) + ' salary of: ' + str(data['Client_Info'][x]['salary']).strip('\':,')+ '\n')
                
    data.close()
#third option
def thirdSelection():
    data = shelve.open('Clients')
    lessthan20 =0
    between20n30 =0
    between30n40 =0
    between40n50 =0
    over50 =0
    if print2file or print2both:
        os.chdir(clientdatpath)
        filename = 'AgeRange4Clients' + str(date.today())
        file = open(filename, "w")
        os.chdir(currentpath)
    for x in data['Client_Info']:
        if(str(data['Client_Info'][x]['dob']) != 'dob'):
            dob = str(data['Client_Info'][x]['dob'])
            l2 =[]
            l2.append(dob.split('/'))
            temp = findAge(date(int(l2[0][2]),int(l2[0][0]),int(l2[0][1])))
            if temp <20:
                lessthan20 += 1
            if 30>temp>=20:
                between20n30 += 1
            if 40>temp>=30:
                between30n40 += 1
            if 50>temp>=40:
                between40n50 += 1
            if temp>50:
                over50 += 1
    if(print2screen):
        print('Clients less than 20 years of age: ' + str(lessthan20))
        print('Clients at least 20 years old but less than 30 years old: ' + str(between20n30))
        print('Clients at least 30 years old but less than 40 years old: ' + str(between30n40))
        print('Clients at least 40 years old but less than 50 years old: ' + str(between40n50))
        print('Clients 50 years or older: ' + str(over50))
    if(print2file):
        file.write('Clients less than 20 years of age: ' + str(lessthan20)+ '\n')
        file.write('Clients at least 20 years old but less than 30 years old: ' + str(between20n30)+ '\n')
        file.write('Clients at least 30 years old but less than 40 years old: ' + str(between30n40)+ '\n')
        file.write('Clients at least 40 years old but less than 50 years old: ' + str(between40n50)+ '\n')
        file.write('Clients 50 years or older: ' + str(over50))
    if(print2both):
        print('Clients less than 20 years of age: ' + str(lessthan20))
        print('Clients at least 20 years old but less than 30 years old: ' + str(between20n30))
        print('Clients at least 30 years old but less than 40 years old: ' + str(between30n40))
        print('Clients at least 40 years old but less than 50 years old: ' + str(between40n50))
        print('Clients 50 years or older: ' + str(over50))
        file.write('Clients less than 20 years of age: ' + str(lessthan20) + '\n')
        file.write('Clients at least 20 years old but less than 30 years old: ' + str(between20n30)+ '\n')
        file.write('Clients at least 30 years old but less than 40 years old: ' + str(between30n40)+ '\n')
        file.write('Clients at least 40 years old but less than 50 years old: ' + str(between40n50)+ '\n')
        file.write('Clients 50 years or older: ' + str(over50))
    data.close()
def findAge(birthday):
    today = date.today()
    age = today.year - birthday.year -((today.month,today.day)<(birthday.month,birthday.day))
    return age
#fourth option
def fourthSelection():
    data = shelve.open('Clients')
    sum1 =0
    num =0
    avg = 0
    test1 = True
    test2 = False
    while test1:
        selection = input('Would you like the average salary by company, state or by both? (type: "c","s" or "b") \n')
        if(selection == 'c'):
            selection2 = input('What company would you like to search? (Please make sure to capitalize the first letter) \n')
            for x in data['Client_Info']:
                if selection2 in str(data['Client_Info'][x]['Company']):
                    sum1 += float(data['Client_Info'][x]['salary'])
                    num += 1
            test2 = True
        elif(selection == 's'):
            selection2 = input('What state would you like to search? (Please use the abbreviation ex: OK) \n')
            for x in data['Client_Info']:
                if selection2 in str(data['Client_Info'][x]['cstate']):
                    sum1 += float(data['Client_Info'][x]['salary'])
                    num += 1
            test2 = True
        elif(selection == 'b'):
            selection2 = input('What company would you like to search? (Please make sure to capitalize the first letter) \n')
            selection3 = input('What state would you like to search? (Please use the abbreviation ex: OK) \n')
            for x in data['Client_Info']:
                if selection2 in str(data['Client_Info'][x]['Company']) and (selection3 in str(data['Client_Info'][x]['cstate'])):
                    sum1 += float(data['Client_Info'][x]['salary'])
                    num += 1
            test2 = True
        else:
            print('Sorry couldn\'t understand your selection please try again')
        if test2:
            if print2file or print2both:
                os.chdir(clientdatpath)
                if selection == 'b':
                    filename = 'AvgSalary4' + selection2 + 'IN' + selection3 + str(date.today())
                else:
                    filename = 'AvgSalary4' + selection2 + str(date.today())
                file = open(filename, "w")
                os.chdir(currentpath)
            avg = sum1/num
            if(print2screen):
                print('The average salary based on your selection is: $' + str(avg))
            if(print2file):
                file.write('The average salary based on your selection is: $' + str(avg))
            if(print2both):
                print('The average salary based on your selection is: $' + str(avg))
                file.write('The average salary based on your selection is: $' + str(avg))
            test1 = False
def reportsFunction():
    tempselect = input('Would you like to print this to a file to the screen or both? (please type "f" "s" or "b") \n')
    global print2file
    global print2screen
    global print2both
    if tempselect == 'f':
        print2file = True
    if tempselect == 's':
        print2screen = True
    if tempselect == 'b':
        print2both = True
        
copyfun(os.path.join(desktop,temp))
while test:
    #userInput = input("If you would like to import some data please place it on your desktop and type in the file name now otherwise type no")
    #if userInput != 'no':
     #   copyfun(userInput)
    #if userInput == 'no':
     #   test = False
    menuefun()
    userInput = input('To exit please type yes. To continue hit enter')
    if userInput == 'yes':
        test = False
    
    
    
    
    #THINGS FOR TOMORROW. FINISH ADDING THE PRINT NONSENSE TO PT 3 AND PT 4 AND TEST PT 2,3,4 THEN DO THE PHONE DIRECTORY ETC 
    #if(print2screen):
    #if(print2file):
    #if(print2both):
