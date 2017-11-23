from tkinter import *
import cmath
from tkinter import messagebox

import math

root = Tk()
root.geometry("800x400+240+110")
root.title("Giải Phương Trình Bậc 2")
root.configure(background='green')

a=IntVar()
b=IntVar()
c=IntVar()

Tops = Frame(root, width=750, height=50, bg="powder blue",bd=14, relief="raise")
Tops.pack(side=TOP)
Tops.configure(background='black')

f1= Frame(root, width=650, height=350, bg="powder blue",bd=8, relief="raise")
f1.pack(side=LEFT)

f2= Frame(root, width=50, height=300, bg="powder blue",bd=12, relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1, width=650, height=100, bg="powder blue",bd=12, relief="raise")
f1a.pack(side=TOP)
f1a.configure(background='violet')
f1b=Frame(f1, width=600, height=250, bg="powder blue",bd=12, relief="raise")
f1b.pack(side=BOTTOM)
f1b.configure(background='pink')

lblTitle=Label(Tops,font=('arial',20,'bold'),text="Giải Phuơng Trình - PyThon",fg="red",bd=10,anchor='w')
lblTitle.grid(row=0,column=0)
photo=PhotoImage(file='myTeacher.png')
lbl=Label(Tops,image=photo)
lbl.grid(row=0,column=1)
txtHTKQ=Text(f1b,width=80,height=10, bg='white',bd=10, font=('arial',10,'bold'))
txtHTKQ.grid(row=1,column=0)


def btnXoa():
    txtHTKQ.delete('1.0', END)
    txtDisplay1.delete(0,'end')
    txtDisplay2.delete(0, 'end')
    txtDisplay3.delete(0, 'end')
    txtDisplay1.focus()


def btnex():
    btnex= messagebox.askyesno("Thoát", "Bạn chắc chắn?")
    if btnex > 0:
        root.destroy()
        return

def btnOK():
    aVal = a.get()
    bVal = b.get()
    cVal = c.get()
    txtHTKQ.insert(END, "Phương Trình Đã Cho (" + str(aVal)+")x*x + ("+str(bVal)+")x + ("+str(cVal)+") = 0 \n")
    delta = pow(bVal, 2) - 4 * aVal * cVal
    if(aVal!=0):
        if delta >= 0:
            x_one = (-bVal + math.sqrt(delta)) / (2 * aVal)
            x_two = (-bVal - math.sqrt(delta)) / (2 * aVal)
            if x_one == x_two:
                txtHTKQ.insert(END, "Vì delta = " + str(delta))
                txtHTKQ.insert(END,"=0\n=> Phương Trình Có 1 Nghiệm Duy Nhất là x = "+str(x_two))
            else:
                txtHTKQ.insert(END, "Vì delta = " + str(delta))
                txtHTKQ.insert(END, ">0\n=> Phương Trình Có Hai Nghiệm Phân Biệt:\n+Nghiệm thứ nhất x1 = " + str(x_one) + "\n+Nghiệm thứ hai x2 = " + str(x_two))
        elif delta < 0:
            txtHTKQ.insert(END, "Vì delta = " + str(delta))
            txtHTKQ.insert(END,"<0\n=>Phương Trình Vô Nghiệm")
    else:
        txtHTKQ.insert(END, "Vì a=0 \n=>Phương Trình Bậc Nhất")
        if(bVal==0):
            txtHTKQ.insert(END, "Vì b=0 \n=>Phương Trình Vô Số Nghiệm")
        else:
            x_1=(-cVal) / (bVal)
            txtHTKQ.insert(END, "\n=>Phương Trình Có Nghiệm x = "+str(x_1))

txtDisplay1 = Entry(f1a,font=('arial',10,'bold'),textvariable=a , bd=4, insertwidth=4,bg="powder blue",justify='left')
txtDisplay1.grid(row=0,column=0)
txtDisplay1.delete(0,'end')
txtDisplay1.focus()
lblX2=Label(f1a,font=('arial',10,'bold'),text=" x*x + ",fg="black",bd=4,anchor='w')
lblX2.grid(row=0,column=1)
txtDisplay2 = Entry(f1a,font=('arial',10,'bold'),textvariable=b, bd=4, insertwidth=4,bg="powder blue",justify='left')
txtDisplay2.grid(row=0,column=2)
txtDisplay2.delete(0,'end')
lblX=Label(f1a,font=('arial',10,'bold'),text=" x + ",fg="black",bd=4,anchor='w')
lblX.grid(row=0,column=3)
txtDisplay3 = Entry(f1a,font=('arial',10,'bold'),textvariable=c, bd=4, insertwidth=4,bg="powder blue",justify='left')
txtDisplay3.grid(row=0,column=4)
txtDisplay3.delete(0,'end')
lblc=Label(f1a,font=('arial',10,'bold'),text=" = 0 ",fg="black",bd=4,anchor='w')
lblc.grid(row=0,column=5)

lblKQ=Label(f1b,font=('arial',10,'bold'),text=" Kết Quả",fg="black",bd=2,anchor='w')
lblKQ.grid(row=0,column=0,sticky=W)


btnDel= Button(f2,padx=8, pady=8, bd=7,fg="black",font=('arial',10,'bold'),text="ĐẶT\nLẠI", bg="powder blue",command= btnXoa).grid(row=1,column=0)

btnE= Button(f2,padx=8, pady=8, bd=7,fg="black",font=('arial',8,'bold'),text="Thoát", bg="powder blue",command=btnex).grid(row=2,column=0)

btnOK= Button(f2,padx=16, pady=16, bd=10,fg="red",font=('arial',15,'bold'),text="GIẢI", bg="powder blue",command=btnOK).grid(row=0,column=0)


root.mainloop()