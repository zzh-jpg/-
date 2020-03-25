import matplotlib.pyplot as plt
from tkinter import *
from tkinter.scrolledtext import ScrolledText   
from tkinter.messagebox import *   
from tkinter.filedialog import * 
import os
word=open('article.txt')
word=word.read()
alphabet={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','\'','-'}
def word_split(article):
    letter=[]
    word=[]
    for i in article:
        if i.lower() in alphabet:
            letter.append(i.lower())
        elif len(sletter)==0:
            continue
        else:
            x_word=''.join(letter)
            word.append(x_word)
            letter=[]
    return word
words_number=len(words_split)
from collections import Counter
count=Counter(words_split)
max_frequency=[]
for i in range(0,len(frequency)):
    if frequency[i][0] in sample_list:
        frequency[i]=0
    else:
        continue
for item in frequency[:6]: 
    max_frequency.append(item)
import numpy as np
import matplotlib.pyplot as plt
N=6
frequency=[]
xlabels=[]
for i in max_frequency:
    frequency.append(i[1])
    xlabels.append(i[0])
frequency=tuple(frequency)
xlabels=tuple(xlabels)
ind=np.arange(N)
width=0.35
fig,ax=plt.subplots()
plt.title('keywords and frequency')
rects=ax.bar(ind,frequency,width)
ax.set_ylabel('frequency')
ax.set_xlabel('words')
ax.set_xticks(ind)
ax.set_xticklabels(xlabels)
plt.show()
window = Tk()
window.title('Text Editor')
window.geometry('900x700+200+200')   
menubar = Menu(window)    
window['menu'] = menubar   
filemenu = Menu(menubar,tearoff=False)   
menubar.add_cascade(label='文件',menu=filemenu)
filemenu.add_command(label='新建',command=newfile)
filemenu.add_command(label='打开',command=openfile)
filemenu.add_command(label='保存',command=savefile)
filemenu.add_command(label='另存为',command=savethefileas)
editmenu = Menu(menubar,tearoff=False)   
menubar.add_cascade(label='编辑',menu=editmenu)
editmenu.add_command(label='清除',command=clearall)
editmenu.add_command(label='全选',command=selectall)
statusmenu = Menu(menubar,tearoff=False)   
menubar.add_cascade(label='文本状态查看',menu=statusmenu)
statusmenu.add_command(label='文本格式化结果',command=text_format)
statusmenu.add_command(label='单词总数',command=word_number)
statusmenu.add_command(label='词频',command=word_frequency)
statusmenu.add_command(label='高频单词',command=high_frequency_word)
aboutmenu = Menu(menubar,tearoff=False)   
menubar.add_cascade(label='关于',menu=aboutmenu)
aboutmenu.add_command(label='作者',command=author)
aboutmenu.add_command(label='版本',command=version)
toolbar = Frame(window,bg='LightSkyBlue')    
Label(toolbar,text='便捷工具栏：',fg='LightCoral',bg='LightSkyBlue').grid(row=0,column=0)
b1 = Button(toolbar,text='新建',command=newfile,bg='Linen')
b2 = Button(toolbar,text='打开',command=openfile,bg='Linen')
b3 = Button(toolbar,text='保存',command=savefile,bg='Linen')
b4 = Button(toolbar,text='清除',command=clearall,bg='Linen')
b5 = Button(toolbar,text='全选',command=selectall,bg='Linen')
b = [b1,b2,b3,b4,b5]
for i in range(5): 
    b[i].grid(row=0,column=i+1,padx=0,pady=2)
toolbar.pack(fill=X)
window.mainloop()