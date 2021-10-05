import pickle
lst=[['石头剪刀布',('石头','剪刀','布')],['甲乙丙丁',('甲','乙','丙','丁','戊','庚','辛','壬','癸')]]
f=open('D:\学习\pythonLearning\周逸尘\python\已完成\大作品\\random object.roj.txt','wb')
pickle.dump(lst,f)
f.close()
print(lst)