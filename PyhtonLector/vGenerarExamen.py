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


#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class vGenerarExamen(mf6.MyFrame6):
	def __init__(self,parent):
		self.c=sqlb.Sqlite_base('base.db')
		#initialize parent class
		mf6.MyFrame6.__init__(self,parent)
		#self.Far=F.Sqlite_Farmacia('Sistema_Farmacias.db')
		#self.Cargar_Fechas()
		self.idsCat=self.c.get_IdsCategoria()
		lista1=[]
		for i in self.idsCat:
			lista1.append(self.c.get_NombreCategoria(i))
		self.m_choice2.AppendItems(lista1)
		self.lista=[]
		self.m_grid5.DeleteCols(0,self.m_grid5.GetNumberCols(),True)
		self.m_grid5.DeleteRows(0,self.m_grid5.GetNumberRows(),True)
		#inserto nuevas filas y columnas
	
		self.m_grid5.AppendCols(2,False)
		self.m_grid5.SetColSize(0,120)
		self.m_grid5.SetColSize(1,150)
				
		self.m_grid5.SetColLabelValue(0,'Categoria')
		self.m_grid5.SetColLabelValue(1,'Cantidad ')
		self.m_grid5.Show(False)
		
		
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
		self.m_grid6.Show(False)

		
		self.m_grid7.DeleteCols(0,self.m_grid7.GetNumberCols(),True)
		self.m_grid7.DeleteRows(0,self.m_grid7.GetNumberRows(),True)
		#inserto nuevas filas y columnas
	
		self.m_grid7.AppendCols(2,False)
		self.m_grid7.SetColSize(0,120)
		self.m_grid7.SetColSize(1,150)
				
		self.m_grid7.SetColLabelValue(0,'Categoria')
		self.m_grid7.SetColLabelValue(1,'Cantidad ')
		self.m_grid7.Show(False)

		
	
	def bCargarPreguntas( self, event ):
		self.m_grid5.Show(True)
		ind=self.m_choice2.GetCurrentSelection()
		idSeleccionado=self.idsCat[ind]
		cantidadPreguntas=self.m_textCtrl4.GetValue()
		
		self.m_grid5.AppendRows(1,False)
		self.m_grid5.SetCellValue(self.m_grid5.GetNumberRows()-1,0,self.c.get_NombreCategoria(idSeleccionado))
		self.m_grid5.SetCellValue(self.m_grid5.GetNumberRows()-1,1,cantidadPreguntas)
		self.lista.append([idSeleccionado,int(cantidadPreguntas)])
		event.Skip()
	
	def bBorrarSeleccionadas( self, event ):
		event.Skip()
	
	def bBorrarTodas( self, event ):
		event.Skip()
	
	def bGenerarExamen( self, event ):
		self.MatDef=[]
		self.RtasCorrectas=[]
		self.m_grid6.Show(True)
		self.idExamen=1
		cont=1
		print self.lista
		for t in self.lista:
			cantidad=t[1]
			categoria=t[0]
			idsPreguntas=self.c.getIdPreguntasCategoria(categoria)
			print "ids de las Preguntas"
			print idsPreguntas

			idsPregSelec=random.sample(idsPreguntas,cantidad)
			print idsPregSelec
			idsRtas=[]
			idsRtasSele=[]
			for i in idsPregSelec:
				respuesta=self.c.getIdRespuestasPregunta(i)
				idsRtas.append(respuesta)
				idsRtasSele.append(random.sample(respuesta,5))
			print "Respuestas"
			print idsRtas
			print "Respuestas Mezcladas"
			print idsRtasSele
			for j in range(0,len(idsPregSelec)):
				self.m_grid6.AppendRows(1,False)
				pregunta=self.c.getPregunta(idsPregSelec[j])
				idrtaCorrecta=self.c.getIdRtaCorrecta(idsPregSelec[j])
				print "rta correcta"
				print idrtaCorrecta
				print pregunta[0]
				self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows()-1,0,pregunta[0])
				self.MatDef.append(pregunta[0])
				for k in range(0,5):
					aux=idsRtasSele[j]
					resp=self.c.getRespuesta(aux[k])
					self.m_grid6.SetCellValue(self.m_grid6.GetNumberRows()-1,k+1,resp[0])
					self.MatDef.append(resp[0])
					if(aux[k]==idrtaCorrecta[0]):
						self.m_grid6.SetCellTextColour(self.m_grid6.GetNumberRows()-1,k+1,wx.Colour(100,20,20))
						self.RtasCorrectas.append([k+1,aux[k]])
						self.c.AddExamenFisico(cont,self.idExamen,idsPregSelec[j],'"'+str(aux)+'"',k+1)	
						cont=cont+1
						
		event.Skip()
	
	def bSeleccionarTodos( self, event ):
		event.Skip()
	
	def bSeleccionados( self, event ):
		event.Skip()
	
	def bExportarExamenes( self, event ):
		nombre=self.m_textCtrl3.GetValue()
		path=self.m_dirPicker2.GetPath()
		ff.generarExamenPlano(path+"/"+nombre,self.MatDef)
		idsAlumnos=self.c.get_Ids()
		cantPreg=self.c.getCantidadPreguntas(self.idExamen)
		cantEx=0
		while True:
			if cantPreg>20:
				cantEx=cantEx+1
				cantPreg=cantPreg-20
			else:
				cantEx=cantEx+1
				break
		
		for i in idsAlumnos:
			nombre1=self.c.get_Nombre(i)
			apellido=self.c.get_Apellido(i)
			dni=self.c.get_Dni(i)
			for j in range(1,cantEx+1):
				ff.genExamen("Prueba.png",nombre1,apellido,dni,i,j)
		event.Skip()
	
	def bCancelar( self, event ):
		event.Skip()
	
		
		
		