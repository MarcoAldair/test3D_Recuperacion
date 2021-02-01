"""
Recuperacion 3D de la materia de Graficacion
Marco Aldair De Jesus Caceres
18390579
I5U
"""
import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
""" 
Importante para poder usar la libreria keyboard hay que instalarla mediante pip
con la siguiente linea de codigo
pip install keyboard
"""
import keyboard
import time

#______Coordenadas Globales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=80
yc=40
zc=40

#Plano y linea de sistema
#Aqui declare los arreglos principales pero la ultima posicion la puse en cero ya que ahi
#lo reemplazere con los valores proporcionados por el usuario
x=[40,30,80,0]
y=[60,10,60,0]
z=[-10,10,10,-10]

#Esta funcion se encarga de llenar los arreglos que contienen los valores que se dibujaran en
#la ventana Es por esto que no lo hago desde el incio
def llenarglobales():
    for i in range(len(x)):
        xg.append(x[i]+xc)
        yg.append(y[i]+yc)
        zg.append(z[i]+zc)

#Esta funcion es la encargada de dibujar el triangulo y a su vez es la que se encarga de 
#de verificar si el hitpoint se encuentra fuera o dentro e imprime los mensajes.
def plotPlaneLine(xg,yg,zg,A,A1,A2):
    plt.axis([0,300,150,0])
    plt.axis('on')
    plt.title('Triangulo 3D HitPoint')
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(False)
    #Aqui dibujamos la base del triangulo
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='k')
    #Aqui se dibujan las lineas punteadas de color rojo que conectan con el valor
    #proporcionado por el user
    plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='r',linestyle='dashed')
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='r',linestyle='dashed')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='r',linestyle='dashed')
    plt.scatter(xg[3],yg[3],c='b')

    print(A,A1,A2)
    plt.text(150,20,'Marco Aldair De Jesus Caceres',color='DeepPink')
    plt.text(250,40,'A = '+str(int(A)),color='r')
    plt.text(250,60,'A1 = '+str(int(A1)),color='g')
    plt.text(250,80,'A2 = '+str(int(A2)),color='b')
    if (A1+ A2) > A:
        plt.text(250,100,'Fuera')
    if (A1+ A2) < A:
        plt.text(250,100,'Dentro')

    plt.show()

def hitpoint(x,y,z):
    #Area A
    #Distancia del punto 01
    #Restamos los puntos para obtener las diferencias
    a = x[1] - x[0]
    b = y[1] - y[0]
    c = z[1] - z[0]
    #aqui calculamos la distancia de los puntos con la formula de la distancia
    D01 = sqrt(a*a+b*b+c*c)
    #Distancia del punto 21
    #Restamos los puntos para obtener las diferencias
    a = x[2] - x[1]
    b = y[2] - y[1]
    c = z[2] - z[1]
    D21 = sqrt(a*a+b*b+c*c)
    #Distancia del punto 02
    #Restamos los puntos para obtener las diferencias
    a = x[2] - x[0]
    b = y[2] - y[0]
    c = z[2] - z[0]
    D02 = sqrt(a*a+b*b+c*c)
    #Aqui se calcula el semiperimetro que nos permitira calcular el area del triangulo
    s = (D01+D21+D02)/2
    a = D01
    b = D21
    c = D02
    #Aqui se calcula el area de la base mediante la formula de heron
    A = sqrt(s*(s-a)*(s-b)*(s-c))

    #Area A1(0,1,3)
    #Distancia del punto 01
    #Restamos los puntos para obtener las diferencias
    a = x[1] - x[0]
    b = y[1] - y[0]
    c = z[1] - z[0]
    D01 = sqrt(a*a+b*b+c*c)
    #Distancia del punto 31
    #Restamos los puntos para obtener las diferencias
    a = x[3] - x[1]
    b = y[3] - y[1]
    c = z[3] - z[1]
    D31 = sqrt(a*a+b*b+c*c)
    #Distancia del punto 03
    #Restamos los puntos para obtener las diferencias
    a = x[3] - x[0]
    b = y[3] - y[0]
    c = z[3] - z[0]
    D03 = sqrt(a*a+b*b+c*c)
    #Aqui se calcula el semiperimetro que nos permitira calcular el area del triangulo
    s = (D01+D31+D03)/2
    a = D01
    b = D31
    c = D03
    #Aqui se calcula el A1 de la base mediante la formula de heron
    A1 = sqrt(s*(s-a)*(s-b)*(s-c))
    
    #Area A2(0,3,2)
    #Distancia de los puntos 03
    #Restamos los puntos para obtener las diferencias
    a = x[3] - x[0]
    b = y[3] - y[0]
    c = z[3] - z[0]
    D03 = sqrt(a*a+b*b+c*c)
    #Distancia del punto 02
    #Restamos los puntos para obtener las diferencias
    a = x[2] - x[0]
    b = y[2] - y[0]
    c = z[2] - z[0]
    D02 = sqrt(a*a+b*b+c*c)
    #Distancia del punto 32
    #Restamos los puntos para obtener las diferencias
    a = x[3] - x[2]
    b = y[3] - y[2]
    c = z[3] - z[2]
    D32 = sqrt(a*a+b*b+c*c)
    #Aqui se calcula el semiperimetro que nos permitira calcular el area del triangulo
    s = (D03+D02+D32)/2
    a = D03
    b = D02
    c = D32
    #Aqui se calcula el A2 de la base mediante la formula de heron
    A2 = sqrt(s*(s-a)*(s-b)*(s-c))
    #Retornamos los valores del area calculados
    return A,A1,A2

print('Presione enter para ingresar los valores del hitpoint en caso contrario pulse esc para salir')
while True:
    if keyboard.is_pressed('ENTER'):
        input()
        hx = int(input('coordenada x hitpoint: '))
        hy = int(input('coordenada y hitpoint: '))
        x[3] = hx
        y[3] = hy
        A,A1,A2 = hitpoint(x,y,z)
        llenarglobales()
        plotPlaneLine(xg,yg,zg,A,A1,A2)
        print('Presione enter para ingresar los valores del hitpoint en caso contrario pulse esc para salir')

    if keyboard.is_pressed('esc'):
        break

    