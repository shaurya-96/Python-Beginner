


import pandas as pd
from numpy import random


def count(number,start_num, end_num,reps,total):
    '''This function will count how many times a 'number' appeared in random generation of numbers between start_num and end_num, reps corresponds to picking
      up of observations from sample space, total corresponds to number of samples required'''
    final_count=[]
    for a in range(total):
        random.seed(random.randint(total))

        b=[random.randint(start_num,end_num) for x in range(reps)]
        b_count={}

        for i in range(reps):
            if b[i] in b_count.keys():
                b_count[b[i]] = int(b_count[b[i]])+1
            else:
                b_count[b[i]]=1

        if number in b_count.keys():
            final_count.append(b_count[number])
        else:
            final_count.append(0)
    sample_list = ['Sample '+str(a+1) for a in range(total)]
    my_dict = {'Sample number':sample_list,'Frequency':final_count}
    df=pd.DataFrame(my_dict)
    df.set_index('Sample number',inplace=True)
    print(df)

count(12,1,20,100,5)
