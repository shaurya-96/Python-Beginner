print('Project 6: Acronym')



sen = input('Enter text: ')
num_space = sen.count(' ')
sen_var = dict()
for i in range(1,num_space+2) :
        sen_var[i]= sen[0][0].upper()
        num_space1 = sen.count(' ')
        if num_space1!=0 :
            space= sen.index(' ')+1
            sen = sen[space:]
        else:
            sen_var[i] = sen[0][0].upper()


for i in range(1,num_space+2):
    sen_var[i]=sen_var[i]+"."

result = sen_var.values()
result1 = ''.join(result)
print(result1)
