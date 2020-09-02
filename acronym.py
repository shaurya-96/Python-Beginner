print('Project 6: Acronym')



inp = input('Enter Sentence: ')

li = inp.split() 

ini = {} #Empty Dictionary

for i in range(len(li)):
    ini[i+1] = li[i][0]
    ini[i+1] = ini[i+1].upper()+'.'

result = ini.values()

result1 = ''.join(result)

print(result1)

