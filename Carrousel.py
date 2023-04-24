from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title('Carrousel de Imagenes')
img1=ImageTk.PhotoImage(Image.open('Camino.jpg'))
img2=ImageTk.PhotoImage(Image.open('campo.jpg'))
img3=ImageTk.PhotoImage(Image.open('Ciervo.jpg'))
img4=ImageTk.PhotoImage(Image.open('oscuridad.jpg'))
img5=ImageTk.PhotoImage(Image.open('Space.jpg'))

lista=[img1,img2,img3,img4,img5]

l=Label(root,image=img1)
l.grid(row=0,column=0,columnspan=3)

def adelante(img_num):
    global l
    global btna
    global btnd
    l.grid_forget()
    l= Label(root,image=lista[img_num])
    
    btna= Button(root, text='->',command=lambda:adelante(img_num+1))
    btnd= Button(root, text='<-',command=lambda:atras(img_num-1))
    if img_num == 3:
        btna=Button(root,text='N/A',state=DISABLED)

    l.grid(row=0,column=0,columnspan=3)
    btna.grid(row=1,column=2)
    btnd.grid(row=1,column=0)

def atras(img_num):
    global l
    global btna
    global btnd
    l.grid_forget()
    l= Label(root,image=lista[img_num])
    
    btna= Button(root, text='->',command=lambda:adelante(img_num+1))
    btnd= Button(root, text='<-',command=lambda:atras(img_num-1))
    if img_num == 0:
        btnd=Button(root,text='N/A',state=DISABLED)

    l.grid(row=0,column=0,columnspan=3)
    btna.grid(row=1,column=2)
    btnd.grid(row=1,column=0)



btna=Button(root,text='N/A',state=DISABLED)
btna.grid(row=1,column=0)
btnd=Button(root,text='->',command=lambda: adelante(1))
btnd.grid(row=1,column=2)
root.mainloop()