#importing wx files
import wx
import Clase_Sqlite as F 
#import the newly created GUI file
import gui
 
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime





 
#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class MiVentana(gui.MyFrame1):
	def __init__(self,parent):
		#initialize parent class
		gui.MyFrame1.__init__(self,parent)
		self.Far=F.Sqlite_Farmacia('Sistema_Farmacias.db')
		self.Cargar_Fechas()
		
	def Boton_Farm_Turno( self, event ):
		self.wx_grilla.Show(True)
		ahora = datetime.datetime.now()
		anio=str(ahora.year)
		dia=str(ahora.day)
		mes=str(ahora.month)
		aux=dia+"-"+mes+"-"+anio
		self.Mostrar_Farmacias_de_Turno(aux)
	
	def Boton_Farm_Fecha( self, event ):
		self.wx_grilla.Show(True)
		indice= self.ch_Fechas.GetCurrentSelection() 
		if indice!=-1:
			fecha=self.ch_Fechas.GetString(indice)
			print(fecha)
			self.Mostrar_Farmacias_de_Turno(fecha)	
	def Boton_Farm( self, event ):
		self.wx_grilla.Show(True)
		self.Mostrar_Farmacias();

	def Cargar_Fechas(self):
		l=self.Far.get_Fechas()
		for i in l:
			for j in i:
				print(j)
				self.ch_Fechas.Append(j)
		

		
	def Mostrar_Farmacias(self):
		#borro si hay columnas anteriores
		self.wx_grilla.DeleteCols(0,15,True)
		self.wx_grilla.DeleteRows(0,15,True)
		#inserto nuevas filas y columnas
		l=self.Far.get_Farmacias()
		n=len(l)
		self.wx_grilla.AppendCols(3,False)
		self.wx_grilla.SetColSize(0,120)
		self.wx_grilla.SetColSize(1,150)
		self.wx_grilla.SetColSize(2,70)
		self.wx_grilla.SetColLabelValue(0,'Nombre')
		self.wx_grilla.SetColLabelValue(1,'Direccion')
		self.wx_grilla.SetColLabelValue(1,'Telefono')
		
		self.wx_grilla.AppendRows(n,False)
		for i in range(0,n):
			p=l[i]
			self.wx_grilla.SetCellValue(i,0,str(p[0]))
			self.wx_grilla.SetCellValue(i,1,str(p[1]))
			self.wx_grilla.SetCellValue(i,2,str(p[2]))
		return 0
	def Mostrar_Farmacias_de_Turno(self,fecha):
		#borro si hay columnas anteriores
		self.wx_grilla.DeleteCols(0,15,True)
		self.wx_grilla.DeleteRows(0,15,True)
		
		#inserto nuevas filas y columnas
		l=self.Far.get_Farmacias_de_Turno(fecha)
		filas=len(l)
		if filas==0:
			return 0
		columnas=len(l[0])
		self.wx_grilla.AppendCols(columnas,False)
		self.wx_grilla.SetColLabelValue(0,'Nombre')
		self.wx_grilla.SetColLabelValue(1,'Direccion')
		self.wx_grilla.SetColLabelValue(2,'Telefono')
		self.wx_grilla.SetColSize(0,120)
		self.wx_grilla.SetColSize(1,150)
		self.wx_grilla.SetColSize(2,70)
		self.wx_grilla.AppendRows(filas,False)
		for i in range(0,filas):
			p=l[i]
			self.wx_grilla.SetCellValue(i,0,str(p[0]))
			self.wx_grilla.SetCellValue(i,1,str(p[1]))
			self.wx_grilla.SetCellValue(i,2,str(p[2]))
		return 0
	
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of CalcFrame
frame = MiVentana(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
