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
		ids=self.c.get_Ids()
		self.m_grid2.Show(True)
		self.m_grid2.DeleteCols(0,self.m_grid2.GetNumberCols(),True)
		self.m_grid2.DeleteRows(0,self.m_grid2.GetNumberRows(),True)
		#inserto nuevas filas y columnas
	
		
		self.m_grid2.AppendCols(5,False)
		self.m_grid2.AppendRows(len(ids),False)
		self.m_grid2.SetColSize(0,120)
		self.m_grid2.SetColSize(1,150)
		self.m_grid2.SetColSize(2,70)
		self.m_grid2.SetColSize(3,70)
		self.m_grid2.SetColSize(4,70)
		
		self.m_grid2.SetColLabelValue(0,'Id')
		self.m_grid2.SetColLabelValue(1,'Nombre')
		self.m_grid2.SetColLabelValue(2,'Apellido')
		self.m_grid2.SetColLabelValue(3,'Dni')
		self.m_grid2.SetColLabelValue(4,'Nota')
		
		#self.m_grid2.AppendRows(n,False)
		for ii in range(0,len(ids)):
			i=ids[ii]
			nombre=self.c.get_Nombre(i)
			apellido=self.c.get_Apellido(i)
			dni=self.c.get_Dni(i)
			notaa=self.c.get_Nota(i)
			print i,nombre,apellido,dni,notaa
			self.m_grid2.SetCellValue(ii,0,str(i))
			self.m_grid2.SetCellValue(ii,1,nombre)
			self.m_grid2.SetCellValue(ii,2,apellido)
			self.m_grid2.SetCellValue(ii,3,dni)
			self.m_grid2.SetCellValue(ii,4,str(notaa))
			
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
		ids=self.c.get_Ids()
		self.m_grid2.Show(True)
		self.m_grid2.DeleteCols(0,self.m_grid2.GetNumberCols(),True)
		self.m_grid2.DeleteRows(0,self.m_grid2.GetNumberRows(),True)
		#inserto nuevas filas y columnas
	
		
		self.m_grid2.AppendCols(5,False)
		self.m_grid2.AppendRows(len(ids),False)
		self.m_grid2.SetColSize(0,120)
		self.m_grid2.SetColSize(1,150)
		self.m_grid2.SetColSize(2,70)
		self.m_grid2.SetColSize(3,70)
		self.m_grid2.SetColSize(4,70)
		
		self.m_grid2.SetColLabelValue(0,'Id')
		self.m_grid2.SetColLabelValue(1,'Nombre')
		self.m_grid2.SetColLabelValue(2,'Apellido')
		self.m_grid2.SetColLabelValue(3,'Dni')
		self.m_grid2.SetColLabelValue(4,'Nota')
		
		
		for i in self.Archivos:
			idAlu,idExa,rta=ff.CorregirExamen(i)
			print "--------- id Alumno: "+str(idAlu)+" ------------"
			print "id Examen: "+str(idExa)
			print rta
			
			nota=10
			if ff.exist(idAlu,ids):
				print "Estado: el alumno existe." 
				self.c.set_Nota(idAlu,nota)
			else:
				print "Estado: el alumno existe."
			print "-------------------------------------------------"
		#self.m_grid2.AppendRows(n,False)
		for ii in range(0,len(ids)):
			i=ids[ii]
			nombre=self.c.get_Nombre(i)
			apellido=self.c.get_Apellido(i)
			dni=self.c.get_Dni(i)
			notaa=self.c.get_Nota(i)
			
			print i,nombre,apellido,dni,notaa
			self.m_grid2.SetCellValue(ii,0,str(i))
			self.m_grid2.SetCellValue(ii,1,nombre)
			self.m_grid2.SetCellValue(ii,2,apellido)
			self.m_grid2.SetCellValue(ii,3,dni)
			self.m_grid2.SetCellValue(ii,4,str(notaa))

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

