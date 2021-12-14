import numpy as np
import time
import pandas as pd
from tkinter import *
from tkinter import ttk
import PIL.Image
import PIL.ImageTk
import math
import os

class interf:
    def __init__(self,ventana):
        #inicializamos la ventana 
        self.ventana=ventana
        self.ventana.title("prueba 1")



#-----------------------Datf-----------------------------------


dfprueba=pd.read_excel('D:\Documentos\Inteligencia Artificial\Tercer Corte\interfaz\Bares_Restaurantes.xlsx')
dfturisticos=pd.read_excel('D:\Documentos\Inteligencia Artificial\Tercer Corte\interfaz\Atractivos_turisticos_v2.xlsx')

####----Guarda una copida del dataFrame original----#########
dfprueb=dfprueba.copy()
dfturist=dfturisticos.copy()

#######---Restaurantes y Bares---####
dfprueb['Especialidad']=dfprueb['Especialidad'].fillna(value="0")
dfprueb['Comida_rapida']=dfprueb['Comida_rapida'].fillna(value="0")
dfprueb['Gourmet']=dfprueb['Gourmet'].fillna(value="0")
dfprueb['Familiar']=dfprueb['Familiar'].fillna(value="0")
dfprueb['Tematico']=dfprueb['Tematico'].fillna(value="0")
dfprueb['Buffet']=dfprueb['Buffet'].fillna(value="0")

######---Atractivos Turisticos--#####
dfturist['recreacion']=dfturist['recreacion'].fillna(value="0")
dfturist['deporte']=dfturist['deporte'].fillna(value="0")
dfturist['historico']=dfturist['historico'].fillna(value="0")
dfturist['cultural']=dfturist['cultural'].fillna(value="0")
dfturist['arquitectura']=dfturist['arquitectura'].fillna(value="0")
dfturist['zona_verde']=dfturist['zona_verde'].fillna(value="0")
dfturist['artistico']=dfturist['artistico'].fillna(value="0")
dfturist['vista']=dfturist['vista'].fillna(value="0")
dfturist['compras']=dfturist['compras'].fillna(value="0")
dfturist['recorrido']=dfturist['recorrido'].fillna(value="0")

#eliminar datos duplicados 
dfprueb=dfprueb.drop_duplicates(['Nombre Establecimiento'],keep='first')
dfprueb=dfprueb.reset_index(drop=True)

dfturist=dfturist.drop_duplicates(['Nombre'],keep='first')
dfturist=dfturist.reset_index(drop=True)

###conversion Restaurantes y Bares
dfprueb['Especialidad']=dfprueb['Especialidad'].astype('float64')
dfprueb['Comida_rapida']=dfprueb['Comida_rapida'].astype('float64')
dfprueb['Gourmet']=dfprueb['Gourmet'].astype('float64')
dfprueb['Familiar']=dfprueb['Familiar'].astype('float64')
dfprueb['Tematico']=dfprueb['Tematico'].astype('float64')
dfprueb['Buffet']=dfprueb['Buffet'].astype('float64')

###Conversion atractivos turisticos
dfturist['recreacion']=dfturist['recreacion'].astype('float64')
dfturist['deporte']=dfturist['deporte'].astype('float64')
dfturist['historico']=dfturist['historico'].astype('float64')
dfturist['cultural']=dfturist['cultural'].astype('float64')
dfturist['arquitectura']=dfturist['arquitectura'].astype('float64')
dfturist['zona_verde']=dfturist['zona_verde'].astype('float64')
dfturist['artistico']=dfturist['artistico'].astype('float64')
dfturist['vista']=dfturist['vista'].astype('float64')
dfturist['compras']=dfturist['compras'].astype('float64')
dfturist['recorrido']=dfturist['recorrido'].astype('float64')

#--------------------------------------------------------------
#raiz
ventana_inicial=Tk()

vactualini1=StringVar()
vactualini2=StringVar()
vactualini3=StringVar()
vactualini4=StringVar()

ventana_inicial.title("BSR")
ventana_inicial.geometry("650x850")

ventana_inicial.config(relief="sunken",bd=8)

frame0=Frame(ventana_inicial)
frame0.pack()
frame0.configure(width=500,height=1080, cursor="star")

labelPunt1=Label(frame0, text="")
labelPunt1.pack(anchor=CENTER, padx=15)
labelPunt1.config(fg="orange",    # Foreground 
             font=("Consolas",50))

######IMAGEN#######

im = PIL.Image.open("D:\Documentos\Inteligencia Artificial\Tercer Corte\interfaz\logov1.png").resize((300,300))
photo = PIL.ImageTk.PhotoImage(im)

labelimg0=Label(frame0, image=photo)
labelimg0.image = photo  # keep a reference!
#labelimg0.config(bg="green")
labelimg0.pack()


#######LECTURA DE DATOS 3 OPCIONES#####
frame1=Frame(ventana_inicial)
frame1.pack(fill="x")
frame1.config(height=200)

# labelsitio1=Label(frame1,text="Sitios Turisticos ")
# labelsitio1.grid(row=1, column=2,pady=(10,10))

labelPunt1=Label(frame1, text="Seleccione tres sitios turisticos previamente visitados\n y por favor puntuelos/califiquelos")
labelPunt1.grid(row=1, column=2,pady=(10,10))
labelPunt1.config(fg="orange",    # Foreground 
             font=("Consolas",13))
             


# labelpunt1=Label(frame1,text="Puntuacion")
# labelpunt1.grid(row=1, column=3,padx=(0,10),pady=(10,0))

labelPunt1=Label(frame1, text="Puntuación\n 0/10")
labelPunt1.grid(row=1, column=3,pady=(10,0))
labelPunt1.config(fg="orange",    # Foreground 
             font=("Consolas",13))

###############sitio1################
sitios=dfprueb['Nombre Establecimiento'].tolist()
turisticos=dfturist['Nombre'].tolist()

sitio1=ttk.Combobox(frame1,state="readonly",values=sitios)
opci1 = sitio1
sitio1.current(0)
sitio1.config(width=80,heigh=30)
sitio1.grid(row=2 , column=2,padx=10,pady=5)



puntua1=Entry(frame1, textvariable=vactualini1,width=5)
puntua1.grid(row=2,column=3,padx=(0,10),pady=5)

# puntua1 = Label(ventana_inicial, text='calificación 1').pack()
# puntua1 = Entry(frame1, textvariable=puntua1,width=5)

#//-------------------------------------- segundo sitio

sitio2=ttk.Combobox(frame1,state="readonly",values=sitios)
sitio2.current(0)
sitio2.config(width=80,heigh=30)
sitio2.grid(row=4 , column=2,padx=10,pady=5)

puntua2=Entry(frame1, textvariable=vactualini2,width=5)
puntua2.grid(row=4,column=3,padx=(0,10),pady=5)

#//-------------------------------------- tercer sitio

sitio3=ttk.Combobox(frame1,state="readonly",values=turisticos)
sitio3.current(0)
sitio3.config(width=80,heigh=30)
sitio3.grid(row=6, column=2,padx=10,pady=5)

puntua3=Entry(frame1, textvariable=vactualini3,width=5)
puntua3.grid(row=6,column=3,padx=(0,10),pady=5)

#//-------------------------------------- cuarto sitio

sitio4=ttk.Combobox(frame1,state="readonly",values=turisticos)
sitio4.current(0)
sitio4.config(width=80,heigh=30)
sitio4.grid(row=8, column=2,padx=10,pady=5)

puntua4=Entry(frame1, textvariable=vactualini4,width=5)
puntua4.grid(row=8,column=3,padx=(0,10),pady=5)

##################################################--borrar
def borrar():
    vactualini1.set('')
    vactualini2.set('')
    vactualini3.set('')
    vactualini4.set('')


def recomendar():
    #tomar los datos de los combobox
    print(f"el primero es:{sitio1.get()}")
    print(f"el segundo es:{sitio2.get()}")
    #print(f"el tercero es:{sitio3.get()}")
    aux1= float(vactualini1.get())
    aux2= float(vactualini2.get())
    #aux3= float(vactualini3.get())
    print(f"el primer valor es :{aux1}")
    print(f"el tipo de datos es:{type(aux1)}")
    restusua={'Nombre Establecimiento':[sitio1.get(),sitio2.get()],'calificacion':[aux1,aux2]}
    dfusuario=pd.DataFrame(restusua)
    print(f"el dataf del usuario es \n:{dfusuario}")
    #asigno clasificacion 
    clasif=dfprueb[dfprueb['Nombre Establecimiento'].isin(dfusuario['Nombre Establecimiento'].tolist())]
    print(f"el dataf del usuario clasificado es \n:{clasif}")
    dfusuario2=pd.merge(clasif,dfusuario)
    sologenero=dfusuario2.drop('SUBCATEGORIA',1).drop('RNT',1).drop('Nombre Establecimiento',1).drop('DIRECCION COMERCIAL',1).drop('LOCALIDAD',1).drop('BARRIO',1).drop('calificacion',1)
    perfil=sologenero.transpose().dot(dfusuario2['calificacion'])
    clasiftot=dfprueb.drop('SUBCATEGORIA',1).drop('RNT',1).drop('Nombre Establecimiento',1).drop('DIRECCION COMERCIAL',1).drop('LOCALIDAD',1).drop('BARRIO',1)
    #clasiftot=dfprueb.drop('Nombre Establecimiento',1).drop('DIRECCION COMERCIAL',1).drop('BARRIO',1)
    recomendar=((clasiftot*perfil).sum(axis=1))/(perfil.sum())
    aux=pd.concat([dfprueb, recomendar], axis=1,)
    aux=aux.sort_values([0],ascending=False)
    fin=aux.reset_index(drop=True)
    r.set(f"{fin.loc[:2,'Nombre Establecimiento':'DIRECCION COMERCIAL']}")

def recomendar_dos():
    print(f"el primero es:{sitio3.get()}")
    print(f"el segundo es:{sitio4.get()}")

    aux3= float(vactualini1.get())
    aux4= float(vactualini2.get())

    print(f"el primer valor es :{aux3}")
    print(f"el tipo de datos es:{type(aux3)}")
    restusuaV1={'Nombre':[sitio3.get(),sitio4.get()],'calificacion':[aux3,aux4]}

    dfusuarioV1=pd.DataFrame(restusuaV1)
    print(f"el dataf del usuario es \n:{dfusuarioV1}")

    clasifUser=dfturist[dfturist['Nombre'].isin(dfusuarioV1['Nombre'].tolist())]
    print(f"el dataf del usuario clasificado es \n:{clasifUser}")

    dfusuarioV2=pd.merge(clasifUser,dfusuarioV1)
    genero= dfusuarioV2.drop('ID',1).drop('Codigo',1).drop('Nombre',1).drop('Direccion',1).drop('Tipo de Patrimonio',1).drop('Nombre Propietario1',1).drop('Direccion Propietario1',1).drop('Correo Propietario1',1).drop('Telefono',1)

    perfilV2=genero.transpose().dot(dfusuarioV2['calificacion'])

    clasiftotV1=dfturist.drop('ID',1).drop('Codigo',1).drop('Nombre',1).drop('Direccion',1).drop('Tipo de Patrimonio',1).drop('Nombre Propietario1',1).drop('Direccion Propietario1',1).drop('Correo Propietario1',1).drop('Telefono',1)

    recomendarV1 =((clasiftotV1*perfilV2).sum(axis=1))/(perfilV2.sum())
    auxV1=pd.concat([dfturist, recomendarV1], axis=1,)
    auxV1=auxV1.sort_values([0],ascending=False)
    finV1=auxV1.reset_index(drop=True)
    res.set(f"{finV1.loc[:2,'Nombre':'Direccion']}")


  


   
    
#se hace la conversion
puntua1 = StringVar()
puntua2 = StringVar()
puntua3 = StringVar()
r = StringVar()
res = StringVar()


Label(ventana_inicial).pack() 

#########----BOTON----#########
botoniniciar=Button(ventana_inicial, text="Recomendar Sitios", command=lambda:[recomendar(),recomendar_dos()],  width=15, height=3, background="#FBB03B",relief="flat", overrelief="raised").pack()



prueba = Button(ventana_inicial, textvariable=r,height=4,width=85,state=DISABLED, justify=CENTER)
prueba.place(x=15,y=660)

prueba_dos=Button(ventana_inicial, textvariable=res,height=4,width=85,state=DISABLED, justify=CENTER)
prueba_dos.place(x=15,y=730)

Label(ventana_inicial).pack() # Separador


#ejecutamos el blucle infinito 
ventana_inicial.mainloop()

#dfprueba=pd.read_excel('datas/Bares_Restaurantes (2).xlsx')


