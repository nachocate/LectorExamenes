#importing wx files
import wx
#import Clase_Sqlite as F 
#import the newly created GUI file
import wxMyFrame5 as mf5
import Sqlite_base as sqlb
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime
import funciones as ff


#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class vCargarPreguntas(mf5.MyFrame5):
	def __init__(self,parent):
		self.idPreg=1
		self.idRes=1
		self.c=sqlb.Sqlite_base('base.db')
		#initialize parent class
		mf5.MyFrame5.__init__(self,parent)
		self.m_grid4.DeleteCols(0,self.m_grid4.GetNumberCols(),True)
		self.m_grid4.DeleteRows(0,self.m_grid4.GetNumberRows(),True)
		#inserto nuevas filas y columnas
		self.m_grid4.AppendCols(2,False)
		self.m_grid4.SetColSize(0,120)
		self.m_grid4.SetColSize(1,150)				
		self.m_grid4.SetColLabelValue(0,'Nombre Categoria')
		self.m_grid4.SetColLabelValue(1,'Cantidad de Preguntas ')
		[val,self.idsCat]=self.c.getIdCategoria()
		lista=[]
		for i in self.idsCat:
			lista.append(self.c.get_NombreCategoria(i))
		self.m_choice1.AppendItems(lista)
		self.Refresh()
		
	def Refresh(self):
		print "llego"
		if(self.m_grid4.GetNumberRows()>0):
			self.m_grid4.DeleteRows(0,self.m_grid4.GetNumberRows(),True)
		
		[val,self.idsCat]=self.c.getIdCategoria()
		n=len(self.idsCat)
		for i in range(0,n):
			[valor,d1]=self.c.getCantPregCategoria((self.idsCat[i]))
			if(valor):
				self.m_grid4.AppendRows(1,False)
				print self.c.getNombreCategoria((self.idsCat[i])),str(d1[0]),str(i)
				self.m_grid4.SetCellValue(self.m_grid4.GetNumberRows()-1,0,self.c.getNombreCategoria((self.idsCat[i])))
				self.m_grid4.SetCellValue(self.m_grid4.GetNumberRows()-1,1,str(d1[0]))
					
		
	def bCargar( self, event ):
		cat_select=self.m_choice1.GetCurrentSelection()
		idSeleccionado=self.idsCat[cat_select]
		path=self.m_filePicker2.GetPath()
		self.nombreArchi=path
		Mat=ff.leerPreguntasFijas(self.nombreArchi)
		cont=1;
		contres=1;
		print "longitud Mat: "+str(len(Mat)/6)
		for i in range(0,len(Mat),6):
			self.c.ins_Pregunta(Mat[i],idSeleccionado)
			idPreg=self.c.getMaxIdPregunta()
			pos=1
			self.c.ins_Respuesta(Mat[i+1],pos,idPreg,1)
			self.c.ins_Respuesta(Mat[i+2],pos+1,idPreg,0)
			self.c.ins_Respuesta(Mat[i+3],pos+2,idPreg,0)
			self.c.ins_Respuesta(Mat[i+4],pos+3,idPreg,0)
			self.c.ins_Respuesta(Mat[i+5],pos+4,idPreg,0)	
		event.Skip()
		self.Refresh()
	
	def bAcepatar( self, event ):
		event.Skip()
	
	def bCancelar( self, event ):
		event.Skip()
	
		
		
		
		