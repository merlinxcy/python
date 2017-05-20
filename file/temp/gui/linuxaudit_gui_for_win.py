from Tkinter import *
import hashlib
import sys
#!-*- coding: utf-8 -*-
md5=hashlib.md5()
md5.update("11")
pwd=md5.hexdigest()
mainflag=0
def show():
    global mainflag
    print pwd
    u=str(username_input.get())
    p=str(password_input.get())
    md5=hashlib.md5()
    md5.update(p)
    pp=md5.hexdigest()
    print u
    print p
    print pp
    if pwd==pp:
        print "login in"
        #root.close()#?
        #root.quit()#quit the loop next time will show again
        root.destroy()#close the login windows and start up the
        #root.withdraw()
        mainflag=1
    else:
        print "login out"

        
def scrollcall(moveto,pos):#smart
    log1.yview(moveto,pos)
    log2.yview(moveto,pos)
    log3.yview(moveto,pos)
    log4.yview(moveto,pos)
    log5.yview(moveto,pos)
    
    
    
######################################login###############################
root=Tk()
root.resizable(False,False)
#height,width
root.geometry('500x300+500+200')
root.title('Linux Log Audit')
title_label=Label(root,pady=25,text='Linux Log Audit Login',font=('',17,''))
title_label.grid()
frame=LabelFrame(root)
frame.grid(padx=500/5-10,pady=300/5-52,sticky=N+W+E+S)
username_label=Label(frame,text="Username",font=('Helvetica',12,'bold'))
password_label=Label(frame,text="Password",font=('Helvetica',12,'bold'))
username_input=Entry(frame,font=('',12,'bold'),borderwidth=3,highlightcolor='black',relief='sunken',width=15)
password_input=Entry(frame,show='*',font=('',12,'bold'),borderwidth=3,highlightcolor='black',relief='sunken',width=15)
confirm_button=Button(frame,text="Confirm",font=('Helvetica',15,'bold'),command=show)
exit_button=Button(frame,text="   Exit   ",font=('Helvetica',15,'bold'),command=lambda: sys.exit(0))
#grid
username_label.grid(padx=10,pady=10,row=0,column=0,sticky=W)
username_input.grid(padx=10,pady=10,row=0,column=1,sticky=W)
password_label.grid(padx=10,pady=10,row=1,column=0,sticky=W)
password_input.grid(padx=10,pady=10,row=1,column=1,sticky=W)
confirm_button.grid(padx=20,pady=20,row=3,column=0,ipadx=5,ipady=5)
exit_button.grid(padx=5,pady=20,row=3,column=1,ipadx=5,ipady=5)

#tupian
#root.iconbitmap('')
root.mainloop()
print mainflag

######################################main###############################
main=Tk()
main.resizable(False,False)
main.geometry('960x560+300+200')
main.title('linux log audit')
##frame
titleframe=Frame(main)
buttonframe=Frame(main)
confframe=LabelFrame(main,text='Audit Configure')
logframe=Frame(main)
titleframe.grid(sticky=W+N,row=0,column=0)
buttonframe.grid(sticky=W+N,row=1,column=0)
confframe.grid(sticky=W+N,row=2,column=0,padx=10,ipadx=30,ipady=30)
logframe.grid(sticky=W+N,row=3,column=0)
##titleframe
title=Label(titleframe,text='  Linux     Log     Audit',font=('',15,''))
#buttonframe
button1=Button(buttonframe,text='Start audit')
button2=Button(buttonframe,text='Stop audit')
button3=Button(buttonframe,text='Kernel Mode')
button4=Button(buttonframe,text='')
button5=Button(buttonframe,text='               ')
button6=Button(buttonframe,text='   Exit   ')
title.grid(row=0,column=0)
button1.grid(row=1,column=0,sticky=W,padx=10)
button2.grid(row=1,column=1,sticky=W,padx=10)
button3.grid(row=1,column=2,sticky=W,padx=10)
button4.grid(row=2,column=0,sticky=W,padx=10)
button5.grid(row=2,column=1,sticky=W,padx=10)
button6.grid(row=2,column=2,sticky=W,padx=10)
#confframe
time_label=Label(confframe,text='Time Conf')
user_label=Label(confframe,text='User Conf')
level_label=Label(confframe,text='Level Conf')
action_label=Label(confframe,text='Action Conf')
key_label=Label(confframe,text='Key Filter')
time_input=Entry(confframe,width=10)
user_input=Entry(confframe,width=10)
level_input=Entry(confframe,width=10)
action_input=Entry(confframe,width=10)
key_input=Entry(confframe,width=10)
change_button=Button(confframe,text='Change')
nochange_button=Button(confframe,text='No Change')
time_label.grid(row=0,column=0,sticky=W,padx=25)
time_input.grid(row=0,column=1,sticky=W)
user_label.grid(row=1,column=0,sticky=W,padx=25)
user_input.grid(row=1,column=1,sticky=W)
level_label.grid(row=2,column=0,sticky=W,padx=25)
level_input.grid(row=2,column=1,sticky=W)
action_label.grid(row=3,column=0,sticky=W,padx=25)
action_input.grid(row=3,column=1,sticky=W)
key_label.grid(row=4,column=0,sticky=W,padx=25)
key_input.grid(row=4,column=1,sticky=W)
change_button.grid(row=5,column=0,pady=10)
nochange_button.grid(row=5,column=1,pady=10)
#logframe
label1=Label(logframe,text='Day')
label2=Label(logframe,text='Time')
label3=Label(logframe,text='User')
label4=Label(logframe,text='Proc')
label5=Label(logframe,text='Info')
bar=Scrollbar(logframe,command=scrollcall)
log1=Listbox(logframe,yscrollcommand=bar.set,width=6)
log2=Listbox(logframe,yscrollcommand=bar.set,width=10)
log3=Listbox(logframe,yscrollcommand=bar.set,width=8)
log4=Listbox(logframe,yscrollcommand=bar.set,width=20)
log5=Listbox(logframe,yscrollcommand=bar.set,width=70)
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)
label4.grid(row=0,column=3)
label5.grid(row=0,column=4)
log1.grid(row=1,column=0)
log2.grid(row=1,column=1)
log3.grid(row=1,column=2)
log4.grid(row=1,column=3)
log5.grid(row=1,column=4)
bar.grid(row=1,column=5,ipady=67,sticky=W)
for i in range(0,100):#insert data
    log1.insert(END,i)
    log2.insert(END,i)
    log3.insert(END,i)
    log4.insert(END,i)
    log5.insert(END,i)
if mainflag==1:
    main.mainloop()

