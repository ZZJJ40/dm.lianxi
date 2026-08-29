import tkinter as tk
from tkinter import messagebox
def nei_1():
    entry.insert(tk.INSERT,'1')
def nei_2():
    entry.insert( tk.INSERT,'2')
def nei_3():
    entry.insert( tk.INSERT,'3')
def nei_4():
    entry.insert( tk.INSERT,'4')
def nei_5():
    entry.insert( tk.INSERT,'5')
def nei_6():
    entry.insert( tk.INSERT,'6')
def nei_7():
    entry.insert( tk.INSERT,'7')
def nei_8():
    entry.insert( tk.INSERT,'8')
def nei_9():
    entry.insert( tk.INSERT,'9')
def nei_0():
    entry.insert( tk.INSERT,'0')
def nei_jia():
    entry.insert( tk.INSERT,'+')
def nei_jian():
    entry.insert( tk.INSERT,'-')
def nei_cheng():
    entry.insert( tk.INSERT,'*')
def nei_chu():
    entry.insert( tk.INSERT,'/')
def nei_qingchu():
    entry.delete( 0,tk.END)
def nei_shan():
    pos = entry.index(tk.INSERT)
    if pos > 0:
        entry.delete(pos - 1)
def nei_kuohao():
    entry.insert( tk.INSERT,'()')
    entry.icursor(entry.index(tk.INSERT) - 1)
def nei_xiaoshu():
    entry.insert( tk.INSERT,'.')
def nei_quyu():
    entry.insert( tk.INSERT,'%')
def queren():
    shizi = entry.get()
    if shizi=='':
        messagebox.showwarning('错误','请先输入式子！！！')
        return
    try:
        jieguo = eval(shizi)
        messagebox.showinfo('结果',f'{shizi}={jieguo}')
        entry.delete(0, tk.END)
        entry.insert(0, jieguo)
    except ZeroDivisionError:
        messagebox.showwarning('错误','除数不能为0！！！')
    except:
        messagebox.showwarning('错误','请输入正常式子！！！')
root = tk.Tk()
root.title('计算机_升级版')
root.geometry('500x500')
entry = tk.Entry(root,
                 width=20,
                 font=('微软雅黑',30))
entry.grid(pady=20,padx=20,row=0,column=0)
top = tk.Frame(root)
top.grid(pady=20)
top1 = tk.Frame(root)
top1.grid(pady=20)
top2 = tk.Frame(root)
top2.grid(pady=20)
top3 = tk.Frame(root)
top3.grid(pady=20)
btn_1 = tk.Button(top,
                  text='1',
                  width=10,
                  command=nei_1)
btn_1.pack(side='left',padx=10)
btn_2 = tk.Button(top,
                  text='2',
                  width=10,
                  command=nei_2)
btn_2.pack(side='left',padx=10)
btn_3 = tk.Button(top,
                  text='3',
                  width=10,
                  command=nei_3)
btn_3.pack(side='left',padx=10)
btn_4 = tk.Button(top1,
                  text='4',
                  width=10,
                  command=nei_4)
btn_4.pack(side='left',padx=10)
btn_5 = tk.Button(top1,
                  text='5',
                  width=10,
                  command=nei_5)
btn_5.pack(side='left',padx=10)
btn_6 = tk.Button(top1,
                  text='6',
                  width=10,
                  command=nei_6)
btn_6.pack(side='left',padx=10)
btn_7 = tk.Button(top2,
                  text='7',
                  width=10,
                  command=nei_7)
btn_7.pack(side='left',padx=10)
btn_8 = tk.Button(top2,
                  text='8',
                  width=10,
                  command=nei_8)
btn_8.pack(side='left',padx=10,)
btn_9 = tk.Button(top2,
                  text='9',
                  width=10,
                  command=nei_9)
btn_9.pack(side='left',padx=10)
btn_qingchu = tk.Button(top3,
                        text='清除',
                        width=10,
                        command=nei_qingchu)
btn_qingchu.pack(side='left',padx=10)
btn_0 = tk.Button(top3,
                  text='0',
                  width=10,
                  command=nei_0)
btn_0.pack(side='left',padx=10)
btn_shan = tk.Button(top3,
                    text='删除',
                     width=10,
                     command=nei_shan)
btn_shan.pack(side='left',padx=10)
btn_jia = tk.Button(top,
                    text='+',
                    width=10,
                    command=nei_jia)
btn_jia.pack(side='left',padx=10)
btn_jian = tk.Button(top1,
                     text='-',
                     width=10,
                     command=nei_jian)
btn_jian.pack(side='left',padx=10)
btn_cheng = tk.Button(top2,
                      text='*',
                      width=10,
                      command=nei_cheng)
btn_cheng.pack(side='left',padx=10)
btn_chu = tk.Button(top3,
                    text='/',
                    width=10,
                    command=nei_chu)
btn_chu.pack(side='left',padx=10)
btn_mi = tk.Button(top,
                   text='( )',
                   width=10,
                   command=nei_kuohao)
btn_mi.pack(side='left',padx=10)
btn_zchu = tk.Button(top1,
                     text='.',
                     width=10,
                     command=nei_xiaoshu)
btn_zchu.pack(side='left',padx=10)
btn_quyu = tk.Button(top2,
                     text='%',
                     width=10,
                     command=nei_quyu)
btn_quyu.pack(side='left',padx=10)
btn_queren = tk.Button(top3,
                       text='确认',
                       width=10,
                       command=queren)
btn_queren.pack(side='left',padx=10)
root.mainloop()




















