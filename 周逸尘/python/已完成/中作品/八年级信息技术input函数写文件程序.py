import pickle
def open_file(create_file):
    global lst
    global dic
    try:
        f=open('file.txt','rb')
        f_load=pickle.load(f)
        dic=f_load
        f.close()
    except EOFError:
        pass
    except FileNotFoundError:
        print('找不到文件！')
    except pickle.UnpicklingError:
        print('文件内容被篡改！')
    except:
        print('发生未知错误！')
    lst+=create_file
def close_file():
    global lst
    global dic
    if lst!=[] and lst!=['\0']:
        dic+=lst#确认是否要加方括号
        f=open('file.txt','wb')
        pickle.dump(dic,f)
        f.close()
    else:
        print('输入内容为空！')
def look_file():
    try:
        f=open('file.txt','rb')
        f_load=pickle.load(f)
        print('你的文件内容是：'+str(f_load))
        f.close()
    except EOFError:
        print('文件内容为空！')
    except FileNotFoundError:
        print('找不到文件！')
    except pickle.UnpicklingError:
        print('文件内容被篡改！')
    except:
        print('发生未知错误！')
dic=[]
lst=[]
print('键入\"\\读取\"以读取文件，键入\"\\写入\"以写入文件，键入\"\\终止\"以终止')
create_file=input('创建文件：')
while True:
    if create_file=='\\读取':
        look_file()
        create_file=input('添加：')
    elif create_file=='\\写入':
        close_file()
        create_file=input('创建文件：')
    elif create_file=='\\终止':
        break
    else:
        open_file(create_file)
        create_file=input('添加：')
