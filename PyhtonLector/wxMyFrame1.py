# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul  7 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Corrector Examenes", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button30 = wx.Button( self, wx.ID_ANY, u"Paso 1: Crear Curso", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer57.Add( self.m_button30, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer57, 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Paso 1: Cargar Alumnos", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Paso 2: Generar Examenes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Paso 3: Corregir Examenes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button30.Bind( wx.EVT_BUTTON, self.cCrearCurso )
		self.m_button1.Bind( wx.EVT_BUTTON, self.cCargarAlumnos )
		self.m_button2.Bind( wx.EVT_BUTTON, self.cGenerarExamenes )
		self.m_button3.Bind( wx.EVT_BUTTON, self.cCorregirExamenes )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cCrearCurso( self, event ):
		event.Skip()
	
	def cCargarAlumnos( self, event ):
		event.Skip()
	
	def cGenerarExamenes( self, event ):
		event.Skip()
	
	def cCorregirExamenes( self, event ):
		event.Skip()
	

