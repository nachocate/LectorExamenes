#importing wx files
import wx
#import Clase_Sqlite as F 
#import the newly created GUI file
import wxMyFrame7 as mf7
import Sqlite_base as sqlb
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime
import funciones as ff
import vCargarCategorias as vcc
import vCargarPreguntas as vcp
import vGenerarExamen as vge


#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class vOpcionesExamenes(mf7.MyFrame7):
	def __init__(self,parent):
		mf7.MyFrame7.__init__(self,parent)
		#self.c=sqlb.Sqlite_base('base.db')
		#initialize parent class

		#self.nombreArchi="none"
		#self.m_grid1.Show(False)
		#self.Far=F.Sqlite_Farmacia('Sistema_Farmacias.db')
		#self.Cargar_Fechas()
	def bCargarCategorias( self, event ):
		#print("cargarAlumnos")
		ventana=vcc.vCargarCategorias(None)
		ventana.Show(True)
		event.Skip()
	
	def bCargarPreguntas( self, event ):
		#print("cargarAlumnos")
		ventana=vcp.vCargarPreguntas(None)
		ventana.Show(True)
		event.Skip()
	
	def bGenerarExamen( self, event ):
		print("cargarAlumnos")
		ventana=vge.vGenerarExamen(None)
		ventana.Show(True)
		event.Skip()
	
	def bCerrar( self, event ):
		self.close()
		event.Skip()
	#def cArchivoAlumnos( self, event ):
	#	event.Skip()
	
		