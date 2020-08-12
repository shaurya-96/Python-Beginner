print('Project 7')

lower = []

for i in range(97,123):
    lower.append(chr(i))

upper = []

for i in range(65,91):
    upper.append(chr(i))

sym_ = []

for i in range(35,58):
    sym_.append(chr(i))

var = {'l':lower, 'u':upper, 's':sym_, 'l+u':lower+upper, 'l+s':lower+sym_}

pas_len = input('How long should the password be? ')

pas_case = input('Should it have both uppercase and lower case letters? ')

pas_num = input('Should it include numbers and special symbols too? ')
if pas_num=='yes':
    pas_char = input('How many letters should there be? ')

import random

password = {}
if pas_case=='no' and pas_num=='no':
    print("".join(random.sample(var['l'],int(pas_len))))

elif pas_case=='yes' and pas_num=='no':
    print("".join(random.sample(var['l+u'],int(pas_len))))

elif pas_case=='no' and pas_num=='yes':
    result1 = random.sample(var['s'],int(pas_len)-int(pas_char))
    result2 = random.sample(var['l'],int(pas_char))
    result3 = result1+result2
    print(''.join(random.sample(result3,int(pas_len))))

else:
    result1 = random.sample(var['s'],int(pas_len)-int(pas_char))
    result2 = random.sample(var['l+u'],int(pas_char))
    result3 = result1+result2
    print(''.join(random.sample(result3,int(pas_len))))





#print("".join(password.values()))
