#!python3
import os,shutil
#to append a zip file newzip = zipfile.zipfile('new.zip','a')
alpha_string='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
currentpath = 'C:\\Users\\Starkey\\Desktop'

for folderN, subfolder, filename in os.walk('C:\\Users\\Starkey\\Desktop\\folder1'):
    #for i in str(filename).strip('[\']'):
    if '.txt' in str(filename).strip('[\']'):
       temp = os.path.dirname(filename)
       currentpath = os.path.join(currentpath, temp)
       print(currentpath)
        
#def copyfun():
    
    
