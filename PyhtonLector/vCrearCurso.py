#importing wx files
import wx
#import Clase_Sqlite as F 
#import the newly created GUI file
import wxMyFrame9 as mf9
import Sqlite_base as sqlb
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime
import funciones as ff


#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class vCrearCurso(mf9.MyFrame9):
	def __init__(self,parent):
		self.c=sqlb.Sqlite_base('base.db')
		
		self.lista=[]
		self.listaId=[]
		self.listaId=self.c.getIdCurso()
		for i in self.listaId:
			self.lista.append(self.c.getCurso(i))
		#self.lista.append("categoria 1")
		#initialize parent class
		mf9.MyFrame9.__init__(self,parent)
		self.Refresh(self.lista)
		self.m_grid9.SetColLabelValue(0,'Nombre de Curso')
		self.m_grid9.SetColSize(0,200)
		
	def Refresh(self,lista):
		if(self.m_grid9.GetNumberRows()!=0):
			self.m_grid9.DeleteRows(0,self.m_grid9.GetNumberRows(),True)
		n=len(lista)
		if n>0:
			for i in range(0,n):
				self.m_grid9.AppendRows(1,False)
				lista[i]
				self.m_grid9.SetCellValue(i,0,lista[i])

	def clickAgregarCurso( self, event ):
		nombre=self.m_textCtrl5.GetValue()
		print nombre
		#self.c.addCurso(nombre)
		self.lista=self.c.addCurso(nombre)
		self.listaId=self.c.getIdCurso()
		self.lista=[]
		for i in self.listaId:
			self.lista.append(self.c.getCurso(i))		
		self.Refresh(self.lista)
		event.Skip()

		
		