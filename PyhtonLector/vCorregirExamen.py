#importing wx files
import wx
#import Clase_Sqlite as F 
#import the newly created GUI file
import wxMyFrame3 as mf3
import Sqlite_base as sqlb
import funciones as ff
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime
import os

#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class vCorregirExamen(mf3.MyFrame3):
	def __init__(self,parent):
		mf3.MyFrame3.__init__(self,parent)
		self.c=sqlb.Sqlite_base('base.db')
		self.Archivos=[]
		self.m_grid2.Show(True)
		self.m_grid2.DeleteCols(0,self.m_grid2.GetNumberCols(),True)
		self.m_grid2.DeleteRows(0,self.m_grid2.GetNumberRows(),True)
		#inserto nuevas filas y columnas
		print "get idExamen",self.c.getIdExamen()
		aux=self.c.getIdExamen() #ME traigo el id y el nombre del examen
		listaAux=[]
		self.listaIdExamen=[]
		if(aux[0]):
			for i in aux[1]:
				self.listaIdExamen.append(i[0])
				nombre=i[1]
				listaAux.append(nombre)
		#self.listaIdExamen=self.c.getIdExamen()
		
		#for i in self.listaIdExamen:
		#	nombre=self.c.getNombreExamen(i)
		#	print nombre
		#	listaAux.append(nombre)
			
		self.m_choice4.AppendItems(listaAux)
		
		
		self.m_grid2.AppendCols(4,False)
		#self.m_grid2.AppendRows(len(ids),False)
		self.m_grid2.AppendRows(10,False)
		self.m_grid2.SetColSize(0,200)
		self.m_grid2.SetColSize(1,80)
		self.m_grid2.SetColSize(2,100)
		self.m_grid2.SetColSize(3,100)
		
		self.m_grid2.SetColLabelValue(0,'Id')
		self.m_grid2.SetColLabelValue(1,'Nombre')
		self.m_grid2.SetColLabelValue(2,'Apellido')
		self.m_grid2.SetColLabelValue(3,'Dni')

		
		
		#self.Refresh(-1)
		#self.m_grid2.AppendRows(n,False)
		
	def Refresh(self,idExamen):
		res=[]
		if idExamen>=0:
			print "llego con idExamen ",idExamen
			res=self.c.getIdAlumnoExamen(idExamen)
			print res
			if res[0]:
				self.listaId=res[1]
				print "lista id=",self.listaId
			else:
				self.listaId=[]
		else:
			self.listaId=[]
		print self.listaId	
		if(self.m_grid2.GetNumberRows()!=0):
			self.m_grid2.DeleteRows(0,self.m_grid2.GetNumberRows(),True)
			print "deberia eliminar"
		
		cantXhoja=10
		cantPreg=self.c.getCantidadPreguntas(idExamen)
		print "la cantidad de preguntas es ",cantPreg
		hojas=round(cantPreg/cantXhoja)
		if (cantPreg-hojas*cantXhoja>0):
			hojas=hojas+1
		print "la cantidad de hojas es de ",hojas
		
		#self.m_grid2.AppendRows(len(ids),False)
		
		for i in range(0,int(hojas)):
					self.m_grid2.AppendCols(1,False)
					self.m_grid2.SetColSize(4+i,20)
					self.m_grid2.SetColLabelValue(4+i,'H'+str(i+1))
		self.m_grid2.SetColLabelValue(0,'Id')
		self.m_grid2.SetColLabelValue(1,'Nombre')
		self.m_grid2.SetColLabelValue(2,'Apellido')
		self.m_grid2.SetColLabelValue(3,'Dni')


		
		for i in self.listaId:
			self.m_grid2.AppendRows(1,False)
			self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,0,str(i))
			self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,1,self.c.getNombre(i))
			self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,2,self.c.getApellido(i))
			self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,3,self.c.getDni(i))
			#self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,4,"10")
			#Color True verde
			#self.m_grid2.SetCellBackgroundColour(self.m_grid2.GetNumberRows()-1, 4,wx.Colour(100,255,100))
			#Color False rojo
			self.m_grid2.SetCellBackgroundColour(self.m_grid2.GetNumberRows()-1, 4,wx.Colour(150,20,20))
			#self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,4,str(self.c.getNota(i)))

				
	

	def cSeleccionarCurso(self,event):
		pos=self.m_choice4.GetSelection()
		print "List chioce:"
		print self.listaIdExamen
		print "pos", pos
		print self.listaIdExamen[pos]
		#self.Refresh(self.listaIdExamen[pos])
		self.Refresh3(self.listaIdExamen[pos])
		event.Skip()

	
	def cDirectorioExamenes( self, event ):
		path=self.m_dirPicker1.GetPath()
		#self.nombreArchi=path
		print(path)
		event.Skip()
	
	def cCargarExamenes( self, event ):
		path=self.m_dirPicker1.GetPath()
		#self.nombreArchi=path
		print(path)
		#f = wx.wxFindFirstFile("/home/*.*");
		#f = os.listdir("/home")
		f = os.listdir(path)
		for i in f:
			print path+'/'+i
			self.Archivos.append(path+'/'+i)
		event.Skip()
	
	def cCorregirExamenes( self, event ):
		
		self.idExamen=self.listaIdExamen[self.m_choice4.GetSelection()]
		#ids=self.c.get_Ids()
		posCorrectas=[]
		aux=self.c.getIdPosCorrecta(self.idExamen)
		if aux[0]:
			posCorrectas=aux[1]
		
		
		
		aux=self.c.getIdExamen()
		idsExamenes=[]
		if aux[0]:
			idsExamenes=aux[1]
		idsAlumnos=[]
		aux=self.c.getIdAlumnoExamen(self.idExamen)
		if aux[0]:
			idsAlumnos=aux[1]
			
			
		for i in self.Archivos:
			idAlumno,Hoja,idExamenOb,rta=ff.CorregirExamen1(i)
			#idAlu,idExa,rta=ff.CorregirExamen(i)
			print "Id Alumno: "+str(idAlumno);
			#print "id Examen: "+str(idExamenOb)
			#print "id Hoja: "+str(Hoja)
			print "Las respuestas son:"
			print rta
			correctas=0
			#getCantPreguntasHoja(idExamen,hoja)
			cantPreg=self.c.getCantPreguntasHoja(self.idExamen,idExamenOb)
			for j in range(0,cantPreg):
				if(posCorrectas[j]==rta[j]):
					correctas=correctas+1
			if  idAlumno in idsAlumnos:
				print "El alumno existe y el examen es el correcto. Se Actualiza"
				self.c.updateExamenAlumno(self.idExamen,idAlumno,Hoja,correctas)
				#self.c.updateExamenAlumno(self.idExamen,idAlumno,idExamenOb,correctas)
			else:
				print "El examen no es el correcto o el Alumno no esta presente en el examen seleccionado."
			print "-------------------------------------------------"
		self.Refresh3(self.idExamen)		
		event.Skip()
	
	def cNombreArchivoExportar( self, event ):
		event.Skip()
	
	def cExportarExamenes( self, event ):
		#archExp=self.GetText()
		ids=self.c.get_Ids()
		idx=[]
		nombre=[]
		apellido=[]
		dni=[]
		nota=[]
		for ii in range(0,len(ids)):
			i=ids[ii]
			idx.append(str(i))
			nombre.append(self.c.get_Nombre(i))
			apellido.append(self.c.get_Apellido(i))
			dni.append(self.c.get_Dni(i))
			nota.append(str(self.c.get_Nota(i)))
		ff.saveCSV("Salida.csv",idx,nombre,apellido,dni,nota)
		event.Skip()

	def ActualizarGrilla(self,idExamen):
		mat=[]
		totalPreguntas=self.c.getCantPreguntas(idExamen)
		print "totalPreguntas=",totalPreguntas
		cantidadHojas=self.c.getCantHojas(idExamen)
		print "cantidadHojas",cantidadHojas
		resultadoParcial=self.c.getResultadoParcialTodosExamenAlumno(idExamen)
		print "......... Resultado Parcial........",len(resultadoParcial)
		for i in resultadoParcial:
			print i
			listaAuxiliar1=[]
			listaAuxiliar2=[]
			listaAuxiliar1.append(self.c.getNombre(i[0])+" "+self.c.getApellido(i[0]))
			for j in range(1,cantidadHojas+1):#de la 1 a la 21 son 20 hojas
				listaAuxiliar2.append(self.c.getCorregida(idExamen,i[0],j))
			listaAuxiliar1.append(listaAuxiliar2)
			listaAuxiliar1.append(i[2])
			listaAuxiliar1.append(i[3])
			notaParcial=(10*(float(i[2])/float(totalPreguntas)))
			listaAuxiliar1.append(notaParcial)
			mat.append(listaAuxiliar1)
		#mat= nombreApellido|[Hoja 1,Hoja2,..]|cantidadPregCorrectas|HojasCorregidas|NotaParcial
		return mat
			
		
	def Refresh3(self,idExamen):
		res=[]
		if idExamen>=0:
			if(self.m_grid2.GetNumberCols()!=0):
				self.m_grid2.DeleteCols(0,self.m_grid2.GetNumberCols(),True)
				self.m_grid2.AppendCols(4,False)
				self.m_grid2.SetColSize(0,200)
				self.m_grid2.SetColSize(1,80)
				self.m_grid2.SetColSize(2,100)
				self.m_grid2.SetColSize(3,100)


			if(self.m_grid2.GetNumberRows()!=0):
				self.m_grid2.DeleteRows(0,self.m_grid2.GetNumberRows(),True)


			mat=self.ActualizarGrilla(idExamen)
			print "imprimi mat"
			for i in mat:
				print i
			for i in range(0,self.c.getCantHojas(idExamen)):
					self.m_grid2.AppendCols(1,False)
					self.m_grid2.SetColSize(4+i,20)
					self.m_grid2.SetColLabelValue(4+i,'H'+str(i+1))
			self.m_grid2.SetColLabelValue(0,'Alumno')
			self.m_grid2.SetColLabelValue(1,'Correctas')
			self.m_grid2.SetColLabelValue(2,'H Corregidas')
			self.m_grid2.SetColLabelValue(3,'Nota Parcial')
			print "comienza el i mat"
			for i in mat:
				print i[0]
				self.m_grid2.AppendRows(1,False)
				self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,0,str(i[0]))
				self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,1,str(i[2]))
				self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,2,str(i[3]))
				self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,3,str(round(i[4],2)))
				cont_j=0
				for j in i[1]:
					if(j==1):
						self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,4+cont_j,str(j))
						self.m_grid2.SetCellBackgroundColour(self.m_grid2.GetNumberRows()-1,4+cont_j,wx.Colour(100,255,100))
					else:
						self.m_grid2.SetCellValue(self.m_grid2.GetNumberRows()-1,4+cont_j,"N/A")
						self.m_grid2.SetCellBackgroundColour(self.m_grid2.GetNumberRows()-1,4+cont_j,wx.Colour(150,20,20))					
					cont_j=cont_j+1
		else:
			if(self.m_grid2.GetNumberRows()!=0):
				self.m_grid2.DeleteRows(0,self.m_grid2.GetNumberRows(),True)
				self.m_grid2.DeleteCols(0,self.m_grid2.GetNumberCols(),True)