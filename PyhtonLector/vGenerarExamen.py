#importing wx files
import wx
#import Clase_Sqlite as F 
#import the newly created GUI file
import wxMyFrame6 as mf6
import Sqlite_base as sqlb
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime
import funciones as ff
import random
import json
import os

#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class vGenerarExamen(mf6.MyFrame6):
	def __init__(self,parent):
		self.c=sqlb.Sqlite_base('base.db')
		#initialize parent class
		mf6.MyFrame6.__init__(self,parent)
		self.idsCat=self.c.get_IdsCategoria()
		self.idsCurso=self.c.getIdCurso()
		lista1=[]
		for i in self.idsCat:
			lista1.append(self.c.get_NombreCategoria(i))
		self.m_choice2.AppendItems(lista1)
		
		lista1=[]
		for i in self.idsCurso:
			lista1.append(self.c.getNombreCurso(i))
		self.m_choice5.AppendItems(lista1)
		
		self.lista=[]
		self.m_grid5.DeleteCols(0,self.m_grid5.GetNumberCols(),True)
		self.m_grid5.DeleteRows(0,self.m_grid5.GetNumberRows(),True)
		#inserto nuevas filas y columnas
	
		self.m_grid5.AppendCols(2,False)
		self.m_grid5.SetColSize(0,120)
		self.m_grid5.SetColSize(1,150)		
		self.m_grid5.SetColLabelValue(0,'Categoria')
		self.m_grid5.SetColLabelValue(1,'Cantidad ')
		
		
		self.m_grid6.DeleteCols(0,self.m_grid6.GetNumberCols(),True)
		self.m_grid6.DeleteRows(0,self.m_grid6.GetNumberRows(),True)
		#inserto nuevas filas y columnas
	
		self.m_grid6.AppendCols(6,False)
		self.m_grid6.SetColSize(0,400)
		self.m_grid6.SetColSize(1,400)
		self.m_grid6.SetColSize(2,400)
		self.m_grid6.SetColSize(3,400)
		self.m_grid6.SetColSize(4,400)
		self.m_grid6.SetColSize(5,400)
		self.m_grid6.SetColLabelValue(0,'Pregunta')
		self.m_grid6.SetColLabelValue(1,'Respuesta 1')
		self.m_grid6.SetColLabelValue(2,'Respuesta 2')
		self.m_grid6.SetColLabelValue(3,'Respuesta 3')
		self.m_grid6.SetColLabelValue(4,'Respuesta 4')
		self.m_grid6.SetColLabelValue(5,'Respuesta 5')
		
		
		self.m_grid7.DeleteCols(0,self.m_grid7.GetNumberCols(),True)
		self.m_grid7.DeleteRows(0,self.m_grid7.GetNumberRows(),True)
		#inserto nuevas filas y columnas
	
		self.m_grid7.AppendCols(2,False)
		self.m_grid7.SetColSize(0,120)
		self.m_grid7.SetColSize(1,150)		
		self.m_grid7.SetColLabelValue(0,'Categoria')
		self.m_grid7.SetColLabelValue(1,'Cantidad ')
		
		print "Probando"
		l= self.c.getRespuestaPreguntaCompuesta(200)
		for i in l:
			if(i[2]==1):
				print i[0],i[1],i[2]
		
	def Refresh5(self):
		if(self.m_grid5.GetNumberRows()>0):
			self.m_grid5.DeleteRows(0,self.m_grid5.GetNumberRows(),True)
		for i in self.lista:
			self.m_grid5.AppendRows(1,False)
			self.m_grid5.SetCellValue(self.m_grid5.GetNumberRows()-1,0,self.c.get_NombreCategoria(i[0]))
			self.m_grid5.SetCellValue(self.m_grid5.GetNumberRows()-1,1,str(i[1]))	
	
	def Refresh6(self):
		if(self.m_grid6.GetNumberRows()>0):
			self.m_grid6.DeleteRows(0,self.m_grid6.GetNumberRows(),True)
	
		data=self.c.getExamenFisicoCompuesto(self.idExamen)
		for i in data:
			vecIdRes=[]
			vecAux=[]
			print i[1],json.loads(i[1])
			vecIdRes=json.loads(i[1])
			ass=self.c.getPregunta(i[0])
			vecAux.append(ass)
			
			for j in vecIdRes:
				print j
				ass=self.c.getRespuesta(j)
				vecAux.append(ass)
				
			print vecAux
			self.m_grid6.AppendRows(1,False)
			self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows()-1,0,str(vecAux[0][0]))
			self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows()-1,1,str(vecAux[1][0]))
			self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows()-1,2,str(vecAux[2][0]))
			self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows()-1,3,str(vecAux[3][0]))
			self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows()-1,4,str(vecAux[4][0]))
			self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows()-1,5,str(vecAux[5][0]))
			self.m_grid6.SetCellTextColour(self.m_grid6.GetNumberRows()-1,int(i[2])+1,wx.Colour(100,100,100))
	
		
	def bCargarPreguntas( self, event ):
		print "Press Cargar"
		#ind=self.m_choice2.GetCurrentSelection()
		idSeleccionado=self.idsCat[self.m_choice2.GetCurrentSelection()]
		cantidadPreguntas=self.m_textCtrl4.GetValue()	
		self.lista.append([idSeleccionado,int(cantidadPreguntas)])
		print self.lista
		self.Refresh5()
		event.Skip()
	
	def bBorrarSeleccionadas( self, event ):
		event.Skip()
	
	def bBorrarTodas( self, event ):
		event.Skip()
	
	def bGenerarExamen( self, event ):
		self.MatDef=[]
		self.RtasCorrectas=[]
		self.c.addExamen(self.m_textCtrl3.GetValue())
		self.nombreExamen=self.m_textCtrl3.GetValue()
		print "este es el valor del getCurrentSelection "+str(self.m_choice5.GetCurrentSelection())
		print "quizas deberia ser este: "+str(self.idsCat[self.m_choice5.GetCurrentSelection()])
		print self.idsCurso,len(self.idsCurso)
		self.idCurso=self.idsCurso[self.m_choice5.GetCurrentSelection()]
		self.idExamen=self.c.getMaxIdExamen()
		cont=1
		for t in self.lista:
			cantidad=t[1]
			categoria=t[0]
			idsPreguntas=self.c.getIdPreguntasCategoria(categoria)
			print "error 1",len(idsPreguntas),cantidad
			idsPregSelec=random.sample(idsPreguntas,cantidad)
			idsRtas=[]
			idsRtasSele=[]
			
			for i in idsPregSelec:
				vDesorden=random.sample([0,1,2,3,4],5)
				matRespuestas=[]				
				matRespuestas= self.c.getRespuestaPreguntaCompuesta(i)
				resp=0
				r=[]
				
				for j in vDesorden:
					r.append(matRespuestas[j][0])
					if matRespuestas[j][3]==1:
						resp=j
				
				self.c.AddExamenFisico(self.idExamen,i,json.dumps(json.dumps(r)),resp,self.idCurso)	
						#idExamen,idPregunta,idsRespuestas,posCorrecta
		self.Refresh6()				
		event.Skip()
	
	def bSeleccionarTodos( self, event ):
		event.Skip()
	
	def bSeleccionados( self, event ):
		event.Skip()
		
	def generarMatDef(self):
		Mat=[]
		self.idExamen=self.c.getMaxIdExamen()
		data=self.c.getExamenFisicoCompuesto(self.idExamen)
		for i in data:
			vecIdRes=[]
			vecAux=[]
			vecIdRes=json.loads(i[1])
			ass=self.c.getPregunta(i[0])
			vecAux.append(ass[0])
			for j in vecIdRes:
				ass=self.c.getRespuesta(j)
				vecAux.append(ass[0])
			Mat.append(vecAux)
		return Mat
	
	def bExportarExamenes( self, event ):
		self.MatDef=[]
		self.MatDef=self.generarMatDef()
		#print "MAT DEF:     ",self.MatDef
		nombre=self.m_textCtrl3.GetValue()
		path=self.m_dirPicker2.GetPath()
		print "---------------------------------------------"
		print self.MatDef
		aux21=path+"/Examenes_"+self.nombreExamen
		os.mkdir( aux21, 0755 );
		
		ff.generarExamenPlano(aux21+"/"+nombre,self.MatDef)
		idsAlumnos=self.c.getIdAlumnoCurso(self.idCurso)
		cantPreg=self.c.getCantidadPreguntas(self.idExamen)
		cantEx=0
		while True:
			if cantPreg>20:
				cantEx=cantEx+1
				cantPreg=cantPreg-20
			else:
				cantEx=cantEx+1
				break
		if idsAlumnos[0]==True:
			
			print len(idsAlumnos),idsAlumnos
			for i in idsAlumnos[1]:
				nombre1=self.c.getNombre(i)
				apellido=self.c.getApellido(i)
				dni=self.c.getDni(i)
				for j in range(1,cantEx+1):
					ff.genExamen("Prueba.png",nombre1,apellido,dni,i,j,aux21+"/")
		print "joya!"
		event.Skip()
	
	def bCancelar( self, event ):
		event.Skip()
	
		
		
		