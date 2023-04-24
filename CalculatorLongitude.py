from tkinter import *
from tkinter import ttk

def calcular(*args):
    seleccion=dropdown.get()
    if(seleccion == "Pies"):
        try:
            value=float(valor.get())
            m=int(0.3048 * value * 1000 + 0.5)/10000
            metros.set(m)
        except ValueError:
            metros.set("ERROR")
   
    elif(seleccion== "Yardas"):
        try:
            value=float(valor.get())
            m=int(0.9144 * value )
            metros.set(m)
        except ValueError:
            metros.set("ERROR")
   
    elif(seleccion== "Millas"):
        try:
            value=float(valor.get())
            m=int(1609.344 * value)
            metros.set(m)
        except ValueError:
            metros.set("ERROR")
   
    elif(seleccion== "Km"):
        try:
            value=float(valor.get())
            m=int(1000 * value )
            metros.set(m)
        except ValueError:
            metros.set("ERROR")

root=Tk()
root.title('Conversor de Longitud')
root.maxsize(415,100)
root.minsize(415,100)
root.geometry("415x100")
frame=Frame(root,pady=3,padx=12)
frame.grid(column=0,row=0)

# pies=StringVar()
# yardas=StringVar()
# millas=StringVar()
# km=StringVar()

dropdown= ttk.Combobox(
    frame,
    state="readonly",
    values=["Pies","Yardas","Millas","Km"]
)

dropdown.grid(column=1,row=0)

valor= StringVar()
valores_input=Entry(frame,width=17,textvariable=valor)
valores_input.grid(column=3,row=0)


metros=StringVar()
Label(frame,textvariable=metros).grid(column=1,row=1)


Button(frame,text='Calcular',command=calcular).grid(column=2 ,row=2)

Label(frame,text='El valor Elegido').grid(column=0,row=0)
Label(frame,text='es igual a ').grid(column=0,row=1)
Label(frame,text='metros').grid(column=2,row=1)

root.bind("<Return>",calcular)
root.mainloop()
