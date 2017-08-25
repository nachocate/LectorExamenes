#importing wx files
import wx
#import Clase_Sqlite as F 
#import the newly created GUI file
import wxMyFrame2 as mf2
import Sqlite_base as sqlb
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime
import funciones as ff


#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class vCargarAlumnos(mf2.MyFrame2):
	def __init__(self,parent):
		self.c=sqlb.Sqlite_base('base.db')
		#initialize parent class
		mf2.MyFrame2.__init__(self,parent)
		self.listaIdCurso=self.c.getIdCurso()
		listaAux=[]
		for i in self.listaIdCurso:
			nombre=self.c.getNombreCurso(i)
			print nombre
			listaAux.append(nombre)
			
		self.m_choice3.AppendItems(listaAux)
		self.nombreArchi="none"
		self.m_grid1.DeleteCols(0,self.m_grid1.GetNumberCols(),True)
		self.m_grid1.AppendCols(3,False)
		self.m_grid1.AppendRows(3,False)
		self.m_grid1.SetColSize(0,200)
		self.m_grid1.SetColSize(1,170)
		self.m_grid1.SetColSize(2,150)
		self.m_grid1.SetColLabelValue(0,'Nombre')
		self.m_grid1.SetColLabelValue(1,'Apellido')
		self.m_grid1.SetColLabelValue(2,'Dni')
		self.Refresh(-1)
		#self.Far=F.Sqlite_Farmacia('Sistema_Farmacias.db')
		#self.Cargar_Fechas()
	
	def Refresh(self,idcat):
		if idcat>=0:
			self.listaId=self.c.getIdAlumnoCurso(idcat)
		else:
			self.listaId=[]
		print self.listaId	
		if(self.m_grid1.GetNumberRows()!=0):
			self.m_grid1.DeleteRows(0,self.m_grid1.GetNumberRows(),True)
		n=len(self.listaId)
		if n>0:
			for i in range(0,n):
				self.m_grid1.AppendRows(1,False)
				self.m_grid1.SetCellValue(i,0,self.c.getNombre((self.listaId[i])))
				self.m_grid1.SetCellValue(i,1,self.c.getApellido((self.listaId[i])))
				self.m_grid1.SetCellValue(i,2,self.c.getDni((self.listaId[i])))

	
	def cSeleccionarCurso(self,event):
		pos=self.m_choice3.GetSelection()
		print pos, self.listaIdCurso[pos]
		self.Refresh(self.listaIdCurso[pos])
		event.Skip()
	
	def cArchivoAlumnos( self, event ):
		print("el archivo seleccionado es:")
		path=self.m_filePicker1.GetPath()
		self.nombreArchi=path
		print(path)
		event.Skip()
	
	def cCargarAlumnos( self, event ):
		self.c.del_Alumnos();
		nom ,ape,dni=ff.loadCSV(self.nombreArchi);
		print nom,ape,dni
		print nom[0]
		
		#inserto nuevas filas y columnas
	
		
		#self.m_grid1.AppendRows(n,False)
		for i in range(0,len(nom)):
		#	p=l[i]
			self.c.ins_Alumno(nom[i],ape[i],dni[i],i+1)
		
		pos=self.m_choice3.GetSelection()
		print pos
		self.Refresh(self.listaIdCurso[pos])
		#m_grid.DeleteRows(0,2)
		event.Skip()
		
		
		
		
		