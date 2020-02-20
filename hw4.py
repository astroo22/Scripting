#! python3
# -*- coding: cp1252 -*-
import random

ew=("Quisiera:Ayer:cambiarle:conocí:el:un:final"
               ":cielo:al:sin:cuento|Las:sol|Y:barras:un:y"
               ":hombre:los:sin:tragos:suelo|Un:han:santo:"
               "sido:en:testigo|De:prision|Y:el:una:dolor:"
               "canción:que:triste:me:sin:causaste:dueño|Y:"
               "y:conocí:to':tus:lo:ojos:que:negros|Y:hiciste"
               ":ahora:conmigo|Un:sí:infeliz:que:en:no:el:"
               "puedo:amor,:vivir:que:sin:aun:ellos:no:yo|"
               "Le:te:pido:supera|Que:al:ahora:cielo:camina"
               ":solo:solo:un:sin:deseo|Que:nadie:en:por:tus"
               ":todas:ojos:las:yo:aceras|Preguntándole:pueda"
               ":a:vivir|He:Dios:recorrido:si:el:en:mundo:verdad"
               ":entero|te:el:vengo:amor:a:existe|:decir|")
list0 =[]

list1 = []
flist1 = []
list2 = []
flist2 = []
finalL = []
for i in str(len(ew)):
    list0.append(ew.split(':'))
for i in range(0, len(list0[0]),2):
    list1.append(list0[0][i])
    list2.append(list0[0][i+1])
for i in range(len(list1)):
    #flist1.append(list1[i].split('|'))
    if '|' in str(list1[i]):
        flist1.append(list1[i].split('|'))
        print(str(flist1[i][0]), end=' ')
        print()
        print(str(flist1[i][1]), end=' ')
    else:
        flist1.append(list1[i])
        print(str(flist1[i]),end=' ')
print()
for i in range(len(list2)):
    if '|' in str(list2[i]):
        flist2.append(list2[i].split('|'))
        print(str(flist2[i][0]), end =' ')
        print()
        print(str(flist2[i][1]), end =' ')
    else:
        flist2.append(list2[i])
        print(str(flist2[i]), end= ' ')
print()
for x in flist1:
    for y in flist2:
        if x == y and x not in str(finalL):
            finalL.append(x)
print('words that are in both songs: ')           
for x in range(len(finalL)):
    print(str(finalL[x]))
