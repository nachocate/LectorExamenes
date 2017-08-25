import numpy as np
import cv2
import math as m
import csv
import Alumno as alu
import sys
import unicodedata
import codecs
from docx import Document
from docx.shared import Inches
from docx.shared import Pt

def genExamen(path,nombre, apellido,dni,idAlumno,idExamen):
	img=cv2.imread(path)
	alto, ancho, canales = img.shape;
	img=cv2.resize(img,(500, 800), interpolation = cv2.INTER_CUBIC)
	alto, ancho, canales = img.shape;
	img_g = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	ret,img_g = cv2.threshold(img_g,200,255,cv2.THRESH_BINARY_INV)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,"Nombre y Apellido: "+nombre+" "+apellido,(30,20),font,0.3,(0,0,0),1,1)
	cv2.putText(img,"Dni: "+dni,(30,35), font,0.3,(0,0,0),1,1)
	cv2.putText(img,"Hoja: "+str(idExamen),(30,50), font,0.3,(0,0,0),1,1)
	alt=109
	despIni=270
	inc=15.8
	l=[]
	
	idAlumnoBinario=bin(idAlumno)[2:].zfill(12)
	idExamenBinario=bin(idExamen)[2:].zfill(12)

	
	
	for i in range(0,12):
		if idExamenBinario[i]=='1':
			l.append([despIni+inc*i,alt])
	for k in l:
		x=k[1]
		y=k[0]
		for i in range(0,12):
			for j in range(0,11):
				img[int(x+i),int(y+j)]=[0,0,0]
	
	
	alt=151
	l=[]
	for i in range(0,12):
		if idAlumnoBinario[i]=='1':
			l.append([despIni+inc*i,alt])
	for k in l:
		x=k[1]
		y=k[0]
		for i in range(0,12):
			for j in range(0,11):
				img[int(x+i),int(y+j)]=[0,0,0]
	
	inc=15
	l=[]
	l=range(20*(idExamen-1)+1,(20*(idExamen-1)+21))
	for i in range(0,20):
		cv2.putText(img,str(l[i])+")",(15,int(203+ 28.4*i)), font,0.3,(0,0,0),1,1)
	cv2.imwrite(nombre+apellido+str(idExamen)+'.png',img)

genExamen("Prueba.png","Ignacio","Catena","35652655",10,1)