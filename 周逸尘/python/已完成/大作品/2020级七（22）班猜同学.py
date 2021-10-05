import tkinter
class 开始:
    '猜同学'
    txt='现在是数学英语B班的吗？'
    x1=0
    x2=0
    x3=0
    x4=0
    x5=0
    x6=0
    x7=0
    turn=0
    wf='你猜的人是：'
    e=0
    t=0
    restart=0
    def __init__(self,parent):
        parent.title('七个问题之内猜出同学')
        parent.geometry('300x1000')
        l1=tkinter.Label(parent,text='请选择WEMS七（22）班同学的信息')
        l1.pack()
        b1=tkinter.Button(parent,text='是',command=lambda:self.start(1,parent))
        b1.pack()
        b2=tkinter.Button(parent,text='否',command=lambda:self.start(2,parent))
        b2.pack()
        b3=tkinter.Button(parent,text='重来',command=lambda:self.begin(0,0,0,0,0,0,0,parent))
        b3.pack()
        l2=tkinter.Label(parent,text=self.txt)
        l2.pack()
        self.begin(0,0,0,0,0,0,0,parent)
    def start(self,x,parent):
        self.turn=self.turn+1
        if self.turn==1:
            self.x1=x
        elif self.turn==2:
            self.x2=x
        elif self.turn==3:
            self.x3=x
        elif self.turn==4:
            self.x4=x
        elif self.turn==5:
            self.x5=x
        elif self.turn==6:
            self.x6=x
        elif self.turn==7:
            self.x7=x
        if self.e==100:
            self.x1=100
        self.begin(self.x1,self.x2,self.x3,self.x4,self.x5,self.x6,self.x7,parent)
    def end(self,parent):
        self.e=100
        self.restart=1
    def begin(self,a1,a2,a3,a4,a5,a6,a7,parent):
        txt=self.txt
        if a1==0:
            self.txt='现在是数学英语B班的吗？'
            self.x1=0
            self.x2=0
            self.x3=0
            self.x4=0
            self.x5=0
            self.x6=0
            self.x7=0
            self.turn=0
            self.wf='你猜的人是：'
            self.e=0
            if self.restart==1:
                ls=tkinter.Label(tk,text='################\n现在是数学英语B班的吗？')
                ls.pack()
        elif a1==1:
            if a2==0:
                txt='是男生吗？'
            elif a2==1:
                if a3==0:
                    txt='是前两排的吗？'
                elif a3==1:
                    if a4==0:
                        txt='是第一排的吗？'
                    elif a4==1:
                        if a5==0:
                            txt='跑步快吗？'
                        elif a5==1:
                            if a6==0:
                                txt='是“大明星”吗？'
                            elif a6==1:
                                txt=self.wf+'林熙皓'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'叶力熠'
                                self.end(parent)
                        elif a5==2:
                            if a6==0:
                                txt='胖吗？'
                            elif a6==1:
                                txt=self.wf+'翁翌翔'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'叶钊辰'
                                self.end(parent)
                    elif a4==2:
                        if a5==0:
                            txt='有特殊的外号或称谓吗？（众所周知的）'
                        elif a5==1:
                            if a6==0:
                                txt='足球踢得很好吗？'
                            elif a6==1:
                                txt=self.wf+'马天佑'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'林炜淳'
                                self.end(parent)
                        elif a5==2:
                            if a6==0:
                                txt='戴眼镜吗？'
                            elif a6==1:
                                txt=self.wf+'林锐'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'朱嘉轩'
                                self.end(parent)
                elif a3==2:
                    if a4==0:
                        txt='是三~五排的吗？'
                    elif a4==1:
                        if a5==0:
                            txt='是课代表吗？'
                        elif a5==1:
                            if a6==0:
                                txt='是科学课代表吗？'
                            elif a6==1:
                                txt=self.wf+'胡程皓'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'李大米'
                                self.end(parent)
                        elif a5==2:
                            if a6==0:
                                txt='美术好吗？'
                            elif a6==1:
                                txt=self.wf+'吴宇轩'
                                self.end(parent)
                            elif a6==2:
                                if a7==0:
                                    txt='外号含“长”吗？'
                                elif a7==1:
                                    txt=self.wf+'季家昌'
                                    self.end(parent)
                                elif a7==2:
                                    txt=self.wf+'单钜响'
                                    self.end(parent)
                    elif a4==2:
                        if a5==0:
                            txt='胖吗？'
                        elif a5==1:
                            if a6==0:
                                txt='戴眼镜吗？'
                            elif a6==1:
                                txt=self.wf+'郑皓轩'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'汤宸铭'
                                self.end(parent)
                        elif a5==2:
                            if a6==0:
                                txt='被组过好几对CP吗？'
                            elif a6==1:
                                txt=self.wf+'邵虹宇'
                                self.end(parent)
                            elif a6==2:
                                if a7==0:
                                    txt='体育好吗？'
                                elif a7==1:
                                    txt=self.wf+'周睿'
                                    self.end(parent)
                                elif a7==2:
                                    txt=self.wf+'邵虹宇'
                                    self.end(parent)
            elif a2==2:
                if a3==0:
                    txt='是前三排的吗？'
                if a3==1:
                    if a4==0:
                        txt='有班级里的职务吗？'
                    elif a4==1:
                        if a5==0:
                            txt='是三个课代表之一吗？'
                        elif a5==1:
                            if a6==0:
                                txt='是领读员吗？'
                            elif a6==1:
                                txt=self.wf+'黄许庆'
                                self.end(parent)
                            elif a6==2:
                                if a7==0:
                                    txt='音乐好吗？'
                                elif a7==1:
                                    txt=self.wf+'彭悦'
                                    self.end(parent)
                                elif a7==2:
                                    txt=self.wf+'滕满满'
                                    self.end(parent)
                        elif a5==2:
                            txt=self.wf+'胡了了'
                            self.end(parent)
                    elif a4==2:
                        if a5==0:
                            txt='是杠精吗？'
                        elif a5==1:
                            if a6==0:
                                txt='上课经常吃东西吗？'
                            elif a6==1:
                                txt=self.wf+'余沁萱'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'王拉雅'
                                self.end(parent)
                        elif a5==2:
                            if a6==0:
                                txt='社会很好吗？'
                            elif a6==1:
                                txt=self.wf+'林嘉涵'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'姚汝娴'
                                self.end(parent)
                elif a3==2:
                    if a4==0:
                        txt='有班级里的职务吗？'
                    elif a4==1:
                        if a5==0:
                            txt='是英语课代表吗？'
                        elif a5==1:
                            if a6==0:
                                txt='是领读员吗？'
                            elif a6==1:
                                txt=self.wf+'管心绮'
                                self.end(parent)
                            elif a6==2:
                                if a7==0:
                                    txt='爱跳舞吗？'
                                elif a7==1:
                                    txt=self.wf+'金栩如'
                                    self.end(parent)
                                elif a7==2:
                                    txt=self.wf+'李吟然'
                                    self.end(parent)
                        elif a5==2:
                            if a6==0:
                                txt='曾当过班长吗？'
                            elif a6==1:
                                txt=self.wf+'郑江辰'
                                self.end(parent)
                            elif a6==2:
                                if a7==0:
                                    txt='和ZZL组过CP吗？'
                                elif a7==1:
                                    txt=self.wf+'周子琪'
                                    self.end(parent)
                                elif a7==2:
                                    txt=self.wf+'潘怡悦'
                                    self.end(parent)
                    elif a4==2:
                        if a5==0:
                            txt='唱歌很好吗？'
                        elif a5==1:
                            if a6==0:
                                txt='声音尖锐吗？'
                            elif a6==1:
                                txt=self.wf+'柳珩珩'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'沈子璇'
                                self.end(parent)
                        elif a5==2:
                            if a6==0:
                                txt='美术特别好吗？'
                            elif a6==1:
                                txt=self.wf+'唐林湘祺'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'夏若曦'
                                self.end(parent)
        elif a1==2:
            if a2==0:
                txt='现在是英语A班的吗？'
            elif a2==1:
                if a3==0:
                    txt='现在是数学A班的吗？'
                elif a3==1:
                    if a4==0:
                        txt='会弹钢琴吗？'
                    elif a4==1:
                        if a5==0:
                            txt='绰号含颜色吗？'
                        elif a5==1:
                            txt=self.wf+'黄思随'
                            self.end(parent)
                        elif a5==2:
                            txt=self.wf+'蔡欣恬'
                            self.end(parent)
                    elif a4==2:
                        if a5==0:
                            txt='是男生吗？'
                        elif a5==1:
                            if a6==0:
                                txt='经常说文明话吗？'
                            elif a6==1:
                                txt=self.wf+'林敬皓'
                                self.end(parent)
                            elif a6==2:
                                txt=self.wf+'周逸尘'
                                self.end(parent)
                        elif a5==2:
                            txt=self.wf+'叶心妍'
                            self.end(parent)
                elif a3==2:
                    if a4==0:
                        txt='是男生吗？'
                    elif a4==1:
                        txt=self.wf+'郑超'
                        self.end(parent)
                    elif a4==2:
                        if a5==0:
                            txt='绰号和历史有关吗？'
                        elif a5==1:
                            txt=self.wf+'吴以帖'
                            self.end(parent)
                        elif a5==2:
                            txt=self.wf+'戴智妍'
                            self.end(parent)
            elif a2==2:
                if a3==0:
                    txt='是中山班的吗？'
                elif a3==1:
                    if a4==0:
                        txt='是男生吗？'
                    elif a4==1:
                        if a5==0:
                            txt='自恋吗？'
                        elif a5==1:
                            txt=self.wf+'朱知临'
                            self.end(parent)
                        elif a5==2:
                            txt=self.wf+'徐粱哲'
                            self.end(parent)
                elif a3==2:
                    if a4==0:
                        txt='转学了吗？'
                    elif a4==1:
                        txt=self.wf+'林弈铭'
                        self.end(parent)
                    elif a4==2:
                        txt=self.wf+'黄奕乔'
                        self.end(parent)
        self.txt=txt
        self.t=1
        if a1==3:
            self.t=0
        if a1!=0 and self.t==1:
            le=tkinter.Label(parent,text=txt)
            le.pack()
tk=tkinter.Tk()
START=开始(tk)
tk.mainloop()