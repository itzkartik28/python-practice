marks1=int(input("enter marks1:"))

marks2=int(input("enter marks2:"))

marks3=int(input("enter marks3:"))

marks4=int(input("enter marks4:"))

marks5=int(input("enter marks5:"))

marks6=int(input("enter marks6:"))

marks7=int(input("enter marks7:"))

marks8=int(input("enter marks8:"))

marks9=int(input("enter marks9:"))

total_percentage = (100*(marks1+marks2+marks3+marks4+marks5+marks6+marks7+marks8+marks9))/900

if(total_percentage>=35 and marks1>=35 and marks2>=35 and marks3>=35 and marks4>=35 and marks5>=35 and marks6>=35 and marks7>=35 and marks8>=35 and marks9>=35):
    print("you passed:",total_percentage)
else:
    print("no you are fail:",total_percentage)
