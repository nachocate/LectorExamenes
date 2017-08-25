#importing wx files
import wx
#import Clase_Sqlite as F 
#import the newly created GUI file
import wxMyFrame8 as mf8
import Sqlite_base as sqlb
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime
import funciones as ff


#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class vCargarCategorias(mf8.MyFrame8):
	def __init__(self,parent):
		self.c=sqlb.Sqlite_base('base.db')
		#initialize parent class
		mf8.MyFrame8.__init__(self,parent)
		#m_grid3
		#self.m_textCtrl2self.m_grid2.Show(True)
		self.m_grid8.DeleteCols(0,self.m_grid8.GetNumberCols(),True)
		self.m_grid8.DeleteRows(0,self.m_grid8.GetNumberRows(),True)
		#inserto nuevas filas y columnas
	
		self.m_grid8.AppendCols(2,False)
		self.m_grid8.SetColSize(0,120)
		self.m_grid8.SetColSize(1,150)
				
		self.m_grid8.SetColLabelValue(0,'Id')
		self.m_grid8.SetColLabelValue(1,'Nombre Categoria')
		self.m_grid8.Show(False)
		
	def bCargar( self, event ):
		self.c.del_Categoria()
		self.m_grid8.Show(True)
		path=self.m_filePicker3.GetPath()
		self.nombreArchi=path
		self.c.del_Alumnos();
		nom=ff.loadCSVCategoria(self.nombreArchi);
		print nom
		#self.m_grid8.DeleteCols(0,self.m_grid8.GetNumberCols(),True)
		#self.m_grid8.DeleteRows(0,self.m_grid8.GetNumberRows(),True)
		#inserto nuevas filas y columnas
	
		self.m_grid8.AppendRows(len(nom),False)
		for i in range(0,len(nom)):
		#	p=l[i]
			self.c.ins_Categoria(nom[i],i+1)
			self.m_grid8.SetCellValue(i,0,str(i+1))
			self.m_grid8.SetCellValue(i,1,nom[i])
		event.Skip()
		
	def bGuardar( self, event ):
		self.Destroy()
		event.Skip()
	
	def bCancelar( self, event ):
		self.Destroy()
		event.Skip()
	

		
		
		