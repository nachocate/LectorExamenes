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
		self.m_grid4.SetColLabelValue(0,'Cantidad de Preguntas ')
		self.m_grid4.Show(False)
		#self.m_choice1=wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,["hola"], 0 )
		self.idsCat=self.c.get_IdsCategoria()
		lista=[]
		for i in self.idsCat:
			lista.append(self.c.get_NombreCategoria(i))
		self.m_choice1.AppendItems(lista)
		#self.m_choice1.Create(self, parent,["gika","gika","gika"])
		#for i in range(0,5):
		#	self.m_choice1.SetString(i,"hola")
		
		
	def bCargar( self, event ):
		cat_select=self.m_choice1.GetCurrentSelection()
		idSeleccionado=self.idsCat[cat_select]
		print idSeleccionado
		self.m_grid4.Show(True)
		path=self.m_filePicker2.GetPath()
		self.nombreArchi=path
		Mat=ff.leerPreguntasFijas(self.nombreArchi)
		#self.m_grid4.AppendRows(len(self.idsCat),False)
		cont=1;
		contres=1;
		print "longitud Mat: "+str(len(Mat)/6)
		for i in range(0,len(Mat),6):
			#self.m_grid4.AppendRows(1,False)
			self.c.ins_Pregunta(Mat[i],self.idPreg,idSeleccionado)
			self.c.ins_Respuesta(Mat[i+1],self.idRes,self.idPreg,1)
			self.idRes=self.idRes+1
			self.c.ins_Respuesta(Mat[i+2],self.idRes,self.idPreg,0)
			self.idRes=self.idRes+1
			self.c.ins_Respuesta(Mat[i+3],self.idRes,self.idPreg,0)
			self.idRes=self.idRes+1
			self.c.ins_Respuesta(Mat[i+4],self.idRes,self.idPreg,0)
			self.idRes=self.idRes+1
			self.c.ins_Respuesta(Mat[i+5],self.idRes,self.idPreg,0)
			self.idRes=self.idRes+1
			self.idPreg=self.idPreg+1
		self.m_grid4.AppendRows(1,False)
		self.m_grid4.SetCellValue(self.m_grid4.GetNumberRows()-1,0,self.c.get_NombreCategoria(idSeleccionado))
		self.m_grid4.SetCellValue(self.m_grid4.GetNumberRows()-1,1,str(len(Mat)/6))
		
		event.Skip()
	
	def bAcepatar( self, event ):
		event.Skip()
	
	def bCancelar( self, event ):
		self.c.del_Respuestas()
		self.c.del_Preguntas()
		event.Skip()
	
		
		
		
		