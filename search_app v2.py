#!/usr/bin/env python
import tkinter as tk
import threading
from tkinter import scrolledtext
import string
import os
import sys
from tkinter import ttk

class mapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.stopvar=0
        
        self.var=tk.StringVar()
        self.minsize(height=700,width=1200)
        self.configure(bg="light green")
        av = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        self.la1=tk.Label(self,text="You have these Directories in your PC:",bg="light green")
        self.la1.place(x=290,y=10)
        self.combo=ttk.Combobox(self,values=av)
        self.combo.current(0)
        self.combo.place(x=580,y=10)
        
        self.la2=tk.Label(self,text="Enter file(or folder) name",bg='light green')
        self.la2.place(x=50,y=70)
        self.ent=tk.Entry(self,textvariable=self.var)
        self.ent.place(x=200,y=70)
        self.txtbox = scrolledtext.ScrolledText(self, width=140, height=30)
        self.txtbox.place(x=30,y=100)
        self.var.trace("w",self.func2) 
        self.a=tk.Button(self,text="GO",state=tk.DISABLED,command=self.go)
        self.b1=tk.Button(self,text="stop",command=self.stop)
        self.b1.place(x=490,y=40)
        ctk=0
        self.a.place(x=360,y=70)
        self.t3=threading.Thread(target = self.stop)
        self.t3.start()
    def stop(self):
        
        self.stopvar=1#these two lines are creating error
        self.configure(bg="light green")
        self.la1.config(bg="light green")
        self.la2.config(bg="light green")
        
        
    def func2(self,*args):
        ctr=0
        
        if(self.var.get()!=""):
            ctr+=1
        if ctr==1:
            self.a.place_forget()
            self.a.config(state=tk.NORMAL)
            self.a.place(x=360,y=70)
        else:
            self.a.place_forget()
            self.a.config(state=tk.DISABLED)
            self.a.place(x=360,y=70)
    def go(self):
        self.la1.config(bg="yellow")
        self.la2.config(bg="yellow")
        self.configure(bg="yellow")
        self.stopvar=0
        try:
            self.txtbox.delete(1.0,tk.END)
        except:
            pass
        z=str(self.combo.get())+"\\"
        
        lis3=[]
        req = str(self.var.get())
        
        
        def func(path,lis3,req):
            if self.stopvar==1:
                return 0
            else:
                pass
            dirs=list()
            
            #self.var.trace("w",self.func2)
            
            path1, dirs1, files = next(os.walk(path))
            for i in dirs1:
                m=path+"\\"+i
                try:
                    path1, dirs2, files2 = next(os.walk(m))
                    dirs.append(i)
                except:
                    continue
    
    
            if path not in lis3:
                lis3.append(path)
        
            else:
                pass
    
    
            if len(dirs)==0 and len(files)==0:
                str=path
                str1=list(str[::-1])
                lis2=list()
                ctr=0
                for i in str1:
                    if i!='\\' and ctr==0:
        
                        pass
                    elif(ctr==1):
                        lis2.append(i)    
                    elif i=='\\':
            
                        ctr+=1
        
    
                    else:
                        pass
                lis2=''.join(lis2)
                lis2=lis2[::-1]
                path=lis2
                self.t1=threading.Thread(target = func,args=(path,lis3,req))#func(path,lis3,req)
                try:
                    if self.stopvar == 0:
                        self.t1.start()
                    else:
                        return 0
                except:
                    pass
                
            else:
                if len(files)!=0:
                    for i in files:
                
                        m=path+"\\"+i
                        if m not in lis3:
                            if req in i:
                                u=m+"\n"
                                
                                if self.stopvar==0:
                                    #print(u)
                                    self.txtbox.insert(tk.END,u)
                                else:
                                    return 0
                                
                            else:
                                pass
                            lis3.append(m)
                        else:
                    
                            continue
                else:
                    pass
                if len(dirs)!=0:
                    for i in dirs:
                        m=path+"\\"+i
                
                
                        if m not in lis3:
                            if i==req:
                                
                                u=m+"\n"
                                
                                if self.stopvar==0:
                                    #print(u)
                                    self.txtbox.insert(tk.END,u)
                                else:
                                    return 0
                            else:
                                pass
                            lis3.append(m)
                            self.t2=threading.Thread(target = func,args=(m,lis3,req))#func(m,lis3,req)
                            try:
                                if self.stopvar==0:
                                    if i!="__pycache__":
                                        self.t2.start()
                                else:
                                    return 0
                            except:
                                pass
                            
                        else:
                            str=m
                            str1=list(str[::-1])
                            lis2=list()
                            ctr=0
                            for j in str1:
                                if j!='\\' and ctr==0:
        
                                    pass
                                elif(ctr==1):
                                    lis2.append(j)    
                                elif j=='\\':
            
                                    ctr+=1
        
    
                                else:
                                    pass
                            lis2=''.join(lis2)
                            lis2=lis2[::-1]
                            path=lis2
                            continue
        func(z,lis3,req)
        
if __name__ == "__main__": 
    app=mapp()
    app.mainloop()
