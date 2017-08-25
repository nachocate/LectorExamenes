#importing wx files
import wx
#import Clase_Sqlite as F 
#import the newly created GUI file
import wxMyFrame1 as mf1
 
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime
import vCargarAlumnos as vca
import vCorregirExamen as vce
import vOpcionesExamenes as voe
import vCrearCurso as vcc

#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class vPrincipal(mf1.MyFrame1):
	def __init__(self,parent):
		mf1.MyFrame1.__init__(self,parent)
		
		
	def cCargarAlumnos( self, event ):
		print("cargarAlumnos")
		ventana=vca.vCargarAlumnos(None)
		ventana.Show(True)
		event.Skip()
	
	def cGenerarExamenes( self, event ):
		print("cGenerarExamenes")
		ventana=voe.vOpcionesExamenes(None)
		ventana.Show(True)

		event.Skip()
	
	def cCorregirExamenes( self, event ):
		print("cCorregirExamenes")
		ventana=vce.vCorregirExamen(None)
		ventana.Show(True)
		event.Skip()
	def cCrearCurso( self, event ):
		print("cCorregirExamenes")
		ventana=vcc.vCrearCurso(None)
		ventana.Show(True)
		event.Skip()