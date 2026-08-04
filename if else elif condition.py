a=int(input("enter age:"))

if(a>=18):
    print("you can vote")

elif(a<0):
    print("you enter nagetive age")

elif(a==0):
    print("you enter invalid age")
else:
    print("you cannot vote")