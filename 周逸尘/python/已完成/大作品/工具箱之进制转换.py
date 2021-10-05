import tkinter
import math
import tkinter.messagebox
###########
class Change:
    '程序开始'
    def __init__(self,parent):
        parent.geometry('300x800')
        parent.title('进制转换')
        parent.configure(bg='white')
        lab1=tkinter.Label(parent,text='请输入要开始转换的数',bg='white')
        lab1.pack()
        ent1=tkinter.Entry(parent,bg='lightgray')
        ent1.pack()
        lab3=tkinter.Label(parent,text='请输入你所输数的进制',bg='white')
        lab3.pack()
        ent3=tkinter.Entry(parent,bg='lightgray')
        ent3.pack()
        lab2=tkinter.Label(parent,text='请输入你要转换的进制',bg='white')
        lab2.pack()
        ent2=tkinter.Entry(parent,bg='lightgray')
        ent2.pack()
        btn1=tkinter.Button(parent,text='转换',command=lambda:self.start(parent,ent1.get(),ent2.get(),ent3.get()),bg='white')
        btn1.pack()
    def start(self,parent,num_begin,cal_way,cal_way_from):
        try:
            int(num_begin)
            cal_way=float(cal_way)
            if int(cal_way)!=cal_way:
                tkinter.messagebox.showerror('ERROR!','请输入整数！')
            elif cal_way<2 or cal_way>36 or int(cal_way_from)<2 or int(cal_way_from)>36:
                tkinter.messagebox.showerror('ERROR!','进制只能在2至36范围内！')
            else:
                dic_chinese={2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十',11:'十一',12:'十二',13:'十三',14:'十四',15:'十五',16:'十六',17:'十七',18:'十八',19:'十九',20:'二十',21:'二十一',22:'二十二',23:'二十三',24:'二十四',25:'二十五',26:'二十六',27:'二十七',28:'二十八',29:'二十九',30:'三十',31:'三十一',32:'三十二',33:'三十三',34:'三十四',35:'三十五',36:'三十六'}
                num_out=0
                one_num=0
                count_turn=0
                real_one_int=0
                one_cal=0
                every_letters=list(num_begin)
                count_numbers=len(num_begin)
                plus_or_subtract=1
                ok_to_pack=True
                if '-' in num_begin:
                    plus_or_subtract=-1
                    del(every_letters[0])
                    count_numbers-=1
                for i in range(0,count_numbers):
                    one_num=every_letters[count_numbers-1]
                    if one_num=='A':
                        real_one_int=10
                    elif one_num=='B':
                        real_one_int=11
                    elif one_num=='C':
                        real_one_int=12
                    elif one_num=='D':
                        real_one_int=13
                    elif one_num=='E':
                        real_one_int=14
                    elif one_num=='F':
                        real_one_int=15
                    elif one_num=='G':
                        real_one_int=16
                    elif one_num=='H':
                        real_one_int=17
                    elif one_num=='I':
                        real_one_int=18
                    elif one_num=='J':
                        real_one_int=19
                    elif one_num=='K':
                        real_one_int=20
                    elif one_num=='L':
                        real_one_int=21
                    elif one_num=='M':
                        real_one_int=22
                    elif one_num=='N':
                        real_one_int=23
                    elif one_num=='O':
                        real_one_int=24
                    elif one_num=='P':
                        real_one_int=25
                    elif one_num=='Q':
                        real_one_int=26
                    elif one_num=='R':
                        real_one_int=27
                    elif one_num=='S':
                        real_one_int=28
                    elif one_num=='T':
                        real_one_int=29
                    elif one_num=='U':
                        real_one_int=30
                    elif one_num=='V':
                        real_one_int=31
                    elif one_num=='W':
                        real_one_int=32
                    elif one_num=='X':
                        real_one_int=33
                    elif one_num=='Y':
                        real_one_int=34
                    elif one_num=='Z':
                        real_one_int=35
                    else:
                        try:
                            if num_begin=='\0':
                                tkinter.messagebox.showerror('ERROR!','请输入内容！')
                            else:
                                if one_num=='1' or one_num=='2' or one_num=='3' or one_num=='4' or one_num=='5' or one_num=='6' or one_num=='7' or one_num=='8' or one_num=='9' or one_num=='0':
                                    real_one_int=int(one_num)
                                else:
                                    tkinter.messagebox.showerror('ERROR!','使用了不支持的字符！\n只能输入数字及大写英文字母！')
                        except:
                            pass
                        real_one_int=int(one_num)
                    if real_one_int>=int(cal_way_from):
                        tkinter.messagebox.showerror('ERROR!','使用了该进制不支持的编码！')
                        ok_to_pack=False
                        break
                    else:
                        one_cal=real_one_int*(int(cal_way_from)**count_turn)
                        num_out+=one_cal
                        count_numbers-=1
                        count_turn+=1
                if num_out>=999999999999999:
                    tkinter.messagebox.showerror('ERROR!','输入的数10进制绝对值\n不得大于999999999999998！')
                else:
                    num=num_out
                    turn=0
                    max_number=0
                    square_turn=0
                    num_end=''
                    one_int=None
                    int_one_int=0
                    while True:
                        if num>cal_way**turn:
                            turn+=1
                        elif num==cal_way**turn:
                            num_end=10**turn
                            break
                        else:
                            square_turn=turn-1
                            max_number=cal_way**square_turn
                            one_int=str(math.floor(num/max_number))
                            if one_int=='10':
                                one_int='A'
                            elif one_int=='11':
                                one_int='B'
                            elif one_int=='12':
                                one_int='C'
                            elif one_int=='13':
                                one_int='D'
                            elif one_int=='14':
                                one_int='E'
                            elif one_int=='15':
                                one_int='F'
                            elif one_int=='16':
                                one_int='G'
                            elif one_int=='17':
                                one_int='H'
                            elif one_int=='18':
                                one_int='I'
                            elif one_int=='19':
                                one_int='J'
                            elif one_int=='20':
                                one_int='K'
                            elif one_int=='21':
                                one_int='L'
                            elif one_int=='22':
                                one_int='M'
                            elif one_int=='23':
                                one_int='N'
                            elif one_int=='24':
                                one_int='O'
                            elif one_int=='25':
                                one_int='P'
                            elif one_int=='26':
                                one_int='Q'
                            elif one_int=='27':
                                one_int='R'
                            elif one_int=='28':
                                one_int='S'
                            elif one_int=='29':
                                one_int='T'
                            elif one_int=='30':
                                one_int='U'
                            elif one_int=='31':
                                one_int='V'
                            elif one_int=='32':
                                one_int='W'
                            elif one_int=='33':
                                one_int='X'
                            elif one_int=='34':
                                one_int='Y'
                            elif one_int=='35':
                                one_int='Z'
                            for i in range(-1,square_turn):
                                num_end+=one_int
                                square_turn-=1
                                if one_int=='A':
                                    int_one_int=10
                                elif one_int=='B':
                                    int_one_int=11
                                elif one_int=='C':
                                    int_one_int=12
                                elif one_int=='D':
                                    int_one_int=13
                                elif one_int=='E':
                                    int_one_int=14
                                elif one_int=='F':
                                    int_one_int=15
                                elif one_int=='G':
                                    int_one_int=16
                                elif one_int=='H':
                                    int_one_int=17
                                elif one_int=='I':
                                    int_one_int=18
                                elif one_int=='J':
                                    int_one_int=19
                                elif one_int=='K':
                                    int_one_int=20
                                elif one_int=='L':
                                    int_one_int=21
                                elif one_int=='M':
                                    int_one_int=22
                                elif one_int=='N':
                                    int_one_int=23
                                elif one_int=='O':
                                    int_one_int=24
                                elif one_int=='P':
                                    int_one_int=25
                                elif one_int=='Q':
                                    int_one_int=26
                                elif one_int=='R':
                                    int_one_int=27
                                elif one_int=='S':
                                    int_one_int=28
                                elif one_int=='T':
                                    int_one_int=29
                                elif one_int=='U':
                                    int_one_int=30
                                elif one_int=='V':
                                    int_one_int=31
                                elif one_int=='W':
                                    int_one_int=32
                                elif one_int=='X':
                                    int_one_int=33
                                elif one_int=='Y':
                                    int_one_int=34
                                elif one_int=='Z':
                                    int_one_int=35
                                else:
                                    int_one_int=int(one_int)
                                num-=int_one_int*max_number
                                max_number=cal_way**square_turn
                                one_int=str(math.floor(num/max_number))
                                if one_int=='10':
                                    one_int='A'
                                elif one_int=='11':
                                    one_int='B'
                                elif one_int=='12':
                                    one_int='C'
                                elif one_int=='13':
                                    one_int='D'
                                elif one_int=='14':
                                    one_int='E'
                                elif one_int=='15':
                                    one_int='F'
                                elif one_int=='16':
                                    one_int='G'
                                elif one_int=='17':
                                    one_int='H'
                                elif one_int=='18':
                                    one_int='I'
                                elif one_int=='19':
                                    one_int='J'
                                elif one_int=='20':
                                    one_int='K'
                                elif one_int=='21':
                                    one_int='L'
                                elif one_int=='22':
                                    one_int='M'
                                elif one_int=='23':
                                    one_int='N'
                                elif one_int=='24':
                                    one_int='O'
                                elif one_int=='25':
                                    one_int='P'
                                elif one_int=='26':
                                    one_int='Q'
                                elif one_int=='27':
                                    one_int='R'
                                elif one_int=='28':
                                    one_int='S'
                                elif one_int=='29':
                                    one_int='T'
                                elif one_int=='30':
                                    one_int='U'
                                elif one_int=='31':
                                    one_int='V'
                                elif one_int=='32':
                                    one_int='W'
                                elif one_int=='33':
                                    one_int='X'
                                elif one_int=='34':
                                    one_int='Y'
                                elif one_int=='35':
                                    one_int='Z'
                            break
                    if plus_or_subtract==-1:
                        num_end='-'+num_end
                    if ok_to_pack:
                        lab_end=tkinter.Label(parent,text=str(num_begin)+'（'+str(dic_chinese[int(cal_way_from)])+'进制）'+'='+str(num_end)+'（'+str(dic_chinese[cal_way])+'进制）',bg='white')
                        lab_end.pack()
        except ValueError:
            tkinter.messagebox.showerror('ERROR!','请输入整数！')
###########
root=tkinter.Tk()
change=Change(root)
###########
root.mainloop()