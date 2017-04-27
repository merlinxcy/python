import tkinter as tk
root=tk.Tk()
a=tk.Entry(root)
a.pack()
show="X"
def ss():
  print a.get()
b=tk.Button(root,text="confirm",command=ss)
b.pack()
a.mainloop()
