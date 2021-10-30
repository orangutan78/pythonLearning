letters='abcdefghijklmnopqrstuvwxyz'
def ILovePY(the_name):
    the_name=the_name()
    if the_name=='PY' or the_name=='py':
        turn=-1
        for i in range(len(letters)):
            turn+=1
            if letters[turn]=='p' or letters[turn]=='y':
                continue
            else:
                print('I hate:'+letters[turn])
    else:
        raise NameError('名字错误：'+the_name)
def IHateSZX(the_name):
    the_name=the_name()
    if the_name=='szx' or the_name=='SZX':
        print('I hate SZX!!!!!')
    else:
        raise NameError('名字错误：'+the_name)
the_order=input('mode:')
#if the_order==1:
@ILovePY
def create_an_input1():
    name=input('name:')
    return name
'''elif the_order==2:
    @IHateSZX
    def create_an_input2():
        return input('name:')'''