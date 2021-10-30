gougu_list=[]
mode=2
num_sum1=15
num_sum2=50
num_sum3=50
the_num1=1
the_num2=1
the_num3=1
return_=True
for i in range(num_sum1):
    the_num2=1
    for j in range(num_sum2):
        the_num3=1
        for k in range(num_sum3):
            if the_num1**2+the_num2**2==the_num3**2 and the_num1<=the_num2<=the_num3:
                turn=0
                for l in range(len(gougu_list)):
                    tp=gougu_list[turn]
                    if type(tp)==tuple:
                        numtp=(the_num1,the_num2,the_num3)
                        num_turn=0
                        deviding=()
                        for m in range(3):
                            deviding+=(numtp[num_turn]/tp[num_turn],)
                            num_turn+=1
                        print(deviding)
                        if deviding[0]==deviding[1]==deviding[2]:
                            return_=False
                            break
                        else:
                            return_=True
                            print(True)
                    turn+=1
                if mode==1:
                    gougu_list+=((the_num1,the_num2,the_num3),)
                else:
                    if return_:
                        gougu_list+=((the_num1,the_num2,the_num3),)
            the_num3+=1
        the_num2+=1
    the_num1+=1
print(gougu_list)