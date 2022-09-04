
import os
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from tkinter import messagebox


a="Arial"
b=10
fn=''
w=Tk()
w.title(f"{fn} NotePad")
def fg(n=0,m=0):
    global a,b
    if n==1:
        text.config(font=(a,5))
        b=5
    elif n==2:
         text.config(font=(a,10))
         b=10
    elif n==3:
         text.config(font=(a,15))
         b=15
    elif n==4:
         text.config(font=(a,20))
         b=20
    elif n==5:
         text.config(font=(a,25))
         b=25
    elif n==6:
         text.config(font=(a,30))
         b=30
    elif n==7:
         text.config(font=(a,35))
         b=35
    elif n==8:
         text.config(font=(a,40))
         b=40
    if  m==1:
        a="Arial"
        text.config(font=("Arial",b))
    elif m==2:
        a="Ink free"
        text.config(font=("Ink free",b))
    elif m==3:
        a="Comic Sans MS"
        text.config(font=("Comic Sans MS",b))
def fg2(k):
    if k==1:
        text.config(font=(a,b),fg="red")
        text["fg"]=="red"
    elif k==2:
        text.config(font=(a,b),fg="green")
    elif k==3:
        text.config(font=(a,b),fg="blue")
    elif k==4:
        text.config(font=(a,b),fg="black")




    

    



        
file=[]
def openf(m):
    print(m)
    global fn
    k=filedialog.askopenfilename(title="open a file",filetypes= (("text files","*.txt"),("all files","*.*")))
    try:
        fn1=os.path.basename(k)
        w.title(f"{fn1[:len(fn1)-4]}-NotPad")
        file.clear()
        file.append(k)
        f= open(k,"r")
        text.delete("1.0", "end-1c")
        text.insert(END,f.read())
        f.close()
    except:
        pass
def savef(m):
    m
    words=text.get("1.0", "end-1c")
    if len(file)!=0:
        try:
            f= open(file[0],"w")
            f.write(str(words))
            f.close() 
        except:
            pass
    else:
        try:
            k=filedialog.asksaveasfilename(defaultextension='.txt',title="save a file",initialfile="Untitled",filetypes= (("Text Document","*.txt"),("all files","*.*")))
            c=open(k,"w")
            c.write(str(words))
            c.close()

        except:
            pass
nll=[]
def nl(m):
    m
    w.title(f"Untitled-NotPad")
    nll.append(0)
    file.clear()
    text.delete("1.0", "end-1c")

def close():
    
    if len(file)!=0 and len(nll)==0:
        f=open(file[0],"r")
        if str(text.get("1.0", "end-1c"))!=str(f.read()):
            ans=messagebox.askyesnocancel("Quit", f"Do you want to save the changes you made to \n {file[0]}?")
            if ans==YES:
                f=open(file[0],"w")
                f.write(str(text.get("1.0", "end-1c")))
                f.close()
                w.destroy()
            elif ans==NO:
                f.close()
                w.destroy()
            else:
                pass
        else:
            w.destroy()
    elif (len(file)==0 and len(nll)!=0) or len(text.get("1.0", "end-1c"))!=0 :
        ans=messagebox.askyesnocancel("Quit", f"Do you want to save the changes you made to Untiteld?")
        if ans==YES:
            words=text.get("1.0", "end-1c")
            try:
                k=filedialog.asksaveasfilename(defaultextension='.txt',title="save a file",initialfile="Untitled",filetypes= (("Text Document","*.txt"),("all files","*.*")))
                c=open(k,"w")
                c.write(str(words))
                c.close()
                w.destroy()
            except:
                pass
        elif ans==NO:
            w.destroy()
        else:
            pass
    else:
        w.destroy()



w.geometry("800x480")
p=PhotoImage(file=r"icon.png")
w.iconphoto(False,p)
F=Frame(w,height=900,width=900)
F.pack()

sb = Scrollbar(F)  
sb.pack(side = RIGHT, fill = Y)  
sb2 = Scrollbar(F,orient='horizontal')  
sb2.pack(side = BOTTOM, fill = X)  


m1=Menu(w)
w.config(menu=m1)
m2=Menu(m1,tearoff=0)
m3=Menu(m1,tearoff=0)
m4=Menu(m1,tearoff=0)
m5=Menu(m1,tearoff=0)


sub_m=Menu(m3,tearoff=0)
sub_m2=Menu(m3,tearoff=0)
sub_m3=Menu(m3,tearoff=0)
sub_m4=Menu(m3,tearoff=0)
sub_m5=Menu(m3,tearoff=0)

c=0
def ch():
    global c
    if c%2==0:
        text["wrap"]=NONE
        c+=1
    else:
        text["wrap"]=WORD
        c+=1

        
        
text=Text(F,width=1000,height=1000,font=(20),yscrollcommand = sb.set,xscrollcommand = sb2.set,undo=True)

def c23():
    if True:
        pass


m1.add_cascade(label="File",menu=m2)
m1.add_cascade(label="Edit",menu=m5)

m1.add_cascade(label="Format",menu=m3)
m3.add_checkbutton(label="word wrap",command=ch)
m3.add_separator()
m1.add_cascade(label="Help",menu=m4)
m3.add_cascade(label="Font size",menu=sub_m)
m3.add_cascade(label="Font style",menu=sub_m4)
m3.add_cascade(label="Font color",menu=sub_m5)
m3.add_separator()

m3.add_cascade(label="Theme",menu=sub_m2)
m5.add_command(label="Undo",accelerator="Ctrl+Z",command=text.edit_undo )
m5.add_separator()
m5.add_command(label="Cut",accelerator="Ctrl+X", command=lambda:w.focus_get().event_generate('<<Cut>>'))
m5.add_command(label="Copy",accelerator="Ctrl+C", command=lambda:w.focus_get().event_generate('<<Copy>>'))
m5.add_command(label="Paste",accelerator="Ctrl+V", command=lambda:w.focus_get().event_generate('<<Paste>>'))







a=5

sub_m4.add_command(label="Arial",command=lambda : fg(m=1))
sub_m4.add_command(label="Ink free",command=lambda : fg(m=2))
sub_m4.add_command(label="Helvetica",command=lambda : fg(m=3))

sub_m5.add_command(label="red",command=lambda : fg2(1))
sub_m5.add_command(label="green",command=lambda : fg2(2))
sub_m5.add_command(label="blue",command=lambda : fg2(3))
sub_m5.add_command(label="black",command=lambda : fg2(4))

m2.add_command(label="new",accelerator="Ctrl+N",command=lambda : nl(0))
m2.add_command(label="open",accelerator="Ctrl+O",command=lambda : openf(0))
m2.add_command(label="save",accelerator="Ctrl+S",command=lambda : savef(0))
m2.add_separator()
m2.add_command(label="Exit",command=close)

m4.add_command(label="About NotePad")





def theme(n):
    if n==1:
        text["bg"]="light yellow"
    elif n==2:
        text["bg"]="light blue"
    elif n==3:
        text["bg"]="light green"
    elif n==4:
        text["bg"]="black"


sub_m.add_command(label="5", command=lambda : fg(1))
sub_m.add_command(label="10",command=lambda : fg(2))
sub_m.add_command(label="15",command=lambda :fg(3))
sub_m.add_command(label="20",command=lambda : fg(4))
sub_m.add_command(label="25",command=lambda : fg(5))
sub_m.add_command(label="30",command= lambda :fg(6))
sub_m.add_command(label="35",command= lambda :fg(7))
sub_m.add_command(label="40",command= lambda :fg(8))



sub_m2.add_command(label="yellow",command=lambda : theme(1))
sub_m2.add_command(label="blue",command=lambda : theme(2))
sub_m2.add_command(label="green",command=lambda : theme(3))
sub_m2.add_command(label="black",command= lambda :theme(4))


text.pack()
sb.config( command = text.yview ) 
sb2.config( command = text.xview ,orient='horizontal')  







w.bind_all('<Control-Key-o>',openf)
w.bind_all('<Control-Key-s>',savef)
w.bind_all('<Control-Key-n>',nl)
w.protocol("WM_DELETE_WINDOW",close)

w.mainloop()