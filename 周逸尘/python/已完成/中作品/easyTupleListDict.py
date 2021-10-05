def CheckIn(obj,tp_or_lst):
    obj=str(obj)
    if obj in tp_or_lst:
        turn=0
        for i in range(len(tp_or_lst)):
            if obj==str(tp_or_lst[turn]):
                return turn
            else:
                turn+=1
        return False
    else:
        turn=0
        try:
            for i in range(len(tp_or_lst)):
                if obj in str(tp_or_lst[turn]):
                    l=tp_or_lst[turn]
                    t=turn
                    turn=0
                    for i in range(len(l)):
                        if obj==str(l[turn]):
                            return t,turn
                        else:
                            turn+=1
                    return False
                else:
                    turn+=1
            return False
        except:
            return False
print('\'w\' in [\'e\',1,1,2,[1,2,3,4,5,6,7,8,\'w\']]:'+str(CheckIn('w',['e',1,1,2,[1,2,3,4,5,6,7,8,'w']])))
def CheckOut(obj,tp_or_lst):
    if CheckIn(obj=obj,tp_or_lst=tp_or_lst)==False:
        return True
    else:
        return False
def OrderDict(obj):
    try:
        lst=list(obj)
    except:
        lst=tuple(obj)
    finally:
        turn=0
        dic={}
        for i in range(len(lst)):
            piece=lst[turn]
            turn+=1
            dic[turn]=piece
        return dic
print('OrderDict(obj=\'abcdefg\')'+str(OrderDict(obj='abcdefg')))
def MoveListTuple(a,n):
    for i in range(n):
        a.append(a.pop(0))
    return a
print('Move(a=[\'a\',\'b\',\'c\',\'d\'],n=3):'+str(MoveListTuple(a=['a','b','c','d'],n=3)))