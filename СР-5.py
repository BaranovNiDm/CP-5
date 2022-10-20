b=0
chis10=int(input("введите число в десятичной системе счисления: "))
while b<1:
    sys=int(input("введите систему счисления (2 или 8): "))
    if int(sys)==2 or int(sys)==8:
        break
    else:
        print('пожалуйста, не пытайтесь ввести не 2 или 8')
        continue
a=[]
while chis10 > 0:
    a.append(int(chis10%sys))
    chis10=chis10//sys
while len(a)<8:
    a.append(0)
konecnoe=''
for i in range(1,len(a)+1):
    konecnoe=konecnoe+str(a[-i])
print(konecnoe)






    

  
        
    
        
