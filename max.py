print('Max Function')

user_dic = {}
count_user = input("how many numbers are there ? ")
for i in range(int(count_user)):
    user_dic[str(i+1)]= input("Enter number "+str(i+1)+": ")


if int(user_dic["1"]) > int(user_dic["2"]):
    larger = user_dic["1"]
else:
    larger = user_dic["2"]

for i in range(int(count_user)-2):
    if int(larger)>int(user_dic[str(i+3)]):
        larger = larger
    else:
        larger = int(user_dic[str(i+3)])

print(larger)
