import os
import openpyxl
from  tkinter import *
import tkinter as tk
from tkinter import filedialog

ventana = Tk()

ventana.title("Generador de Excel")

ventana.geometry("750x365")
ventana.maxsize(750,365)
ventana.minsize(750,365)

marco= Frame(ventana,width=735,height=350)
marco.config(
    bg="white",
    bd=2,
)
marco.pack(padx=5 , pady=6)

marco.pack_propagate(FALSE)
texto=Label(marco,text="Expecifique una ruta: ")
texto.config(
    bg="white",
    font=("Arial",14)
)

datos=StringVar()
texto.pack(anchor=CENTER,side=LEFT)
campo_txt=Entry(marco)
campo_txt.config(
    width=65,font=("Arial",10),
    border=2,
    textvariable=datos
    
)

def abrirCarpeta():

    raiz=tk.Tk()
    raiz.withdraw()
    ruta_archivos=filedialog.askdirectory()
    datos.set(ruta_archivos)


def getdatos():


    ruta=str(datos.get())

    rutaAbsoluta =os.path.abspath(ruta)

    texto=""
    nºArchivos=0
    cantidad_archivos={}
    contador=1
    contador_archivos=0
    excel=openpyxl.Workbook()
    hoja = excel.active
    total_vueltas = sum([len(directorio) for _, directorio, _ in os.walk(rutaAbsoluta)])
    contador_vueltas = 0

    for raiz,directorios,archivos in os.walk(rutaAbsoluta):
        for i in directorios:
            contador+=1
            texto=str(os.path.join(raiz,i))
            hoja["A"+str(contador)]=texto
        for e in archivos:
                nºArchivos=len(archivos)
                contador_archivos+=1
                cantidad_archivos[raiz]= nºArchivos
                contador+=1
                texto=str(os.path.join(raiz,e))
                hoja["A"+str(contador)]=texto
        if contador_vueltas == total_vueltas - 1:
            hoja["J" + str(contador)] = str(cantidad_archivos[raiz])
        contador_vueltas += 1
    excel.save("Datos.xlsx")

campo_txt.pack(anchor=CENTER,side=LEFT)
btn=Button(marco)
btn.config(
  text="Buscar",
  height=2,
  width=8,
  cursor="hand2" ,
  bg="grey",
  fg="white",
  command=abrirCarpeta
  
)

btn.pack(side=LEFT,anchor=E)
btn_excel=Button(marco)
btn_excel.config(
  text="Generar Excel",
  height=2,
  width=12,
  cursor="hand2" ,
  bg="grey",
  fg="white",
  command=getdatos
)
btn_excel.place(x=375,y=215)
ventana.mainloop()
