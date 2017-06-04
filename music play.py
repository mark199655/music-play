# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:52:03 2017

@author: Administrator
"""
#GUI开发，第一步制作界面，第二步实现功能
#mainloop是一个循环截止，程序写在TK()与mainloop()中间
#API接口：http://s.music.163.com/search/get/?type=1&s=%E6%B5%B7%E9%98%94%E5%A4%A9%E7%A9%BA&limit=9
from Tkinter import *
import tkMessageBox
import urllib
import json
import mp3play
import time
import threading
import random

def music():
    text=entry.get()#将输入框的内容赋值给text
    if not text:
        tkMessageBox.showinfo('温馨提示','请先输入歌曲名或歌手们再点击搜索')
        return   #return的作用：1.返回一个值；2.终止函数
    html=urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=%E6%B5%B7%E9%98%94%E5%A4%A9%E7%A9%BA&limit=9')#%s,s是歌名
    text=json.loads(html)
    music_list=text['result']['songs']
    global url_list
    url_list=[]
    for i in music_list:
        listbox.insert(0,i['name']+'('+i['artists'][0]['name']+')')
        url_list.append(i['audio'])  
    print type(text)
    print '按钮已点击'
def paly():
    index=listbox.curselection()
    filename=r'%s.mp3'%random.randint(1000,9999)
    urllib.urlretrieve(url_list[index],filename)
    mp3=mp3play.load(filename=filename)
    mp3.play()
    mp3.sleep(time.sleep(mp3.seconds()))
    mp3.stop()

def th(event):
    time.sleep(2)
    thr=threading.Thread(targrt=play)
    thr.start()    
    
root=Tk()#实例窗口对象（创建窗口）
root.title('转身李克勤的音乐播放器')#更改标题
root.geometry('+600+300')#前面是窗口大小，mxn，可以不写，默认，乘号是小写的x;后面的第一个+是横坐标，第二个+是纵坐标,坐标位置是距离左上角的位置
entry=Entry(root)#创建一个单行的输入框      布局：显示的方式和位置，布局包括两种：pack和grid
entry.pack()
button=Button(root,text='搜 索',command=music)#实例一个按钮，root是一个子窗口
button.pack()
var=StringVar()
listbox=Listbox(root,width=50,listvariable=var)
listbox.bind('<Double-Button-1>',play)
listbox.pack()
label=Label(root,text='欢迎使用Music播放器',fg='green')
label.pack()
mainloop()#显示窗口,持续显示

