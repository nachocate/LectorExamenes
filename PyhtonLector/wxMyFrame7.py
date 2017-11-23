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
## Class MyFrame7
###########################################################################

class MyFrame7 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Opciones generar examenes", pos = wx.DefaultPosition, size = wx.Size( 340,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer44 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Para generar el examen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer45.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		
		bSizer44.Add( bSizer45, 0, wx.EXPAND, 5 )
		
		bSizer48 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Cargar Categorias", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer48.Add( self.m_button23, 0, wx.ALL, 5 )
		
		
		bSizer44.Add( bSizer48, 0, wx.EXPAND, 5 )
		
		bSizer49 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Cargar las preguntas en cada Categoria", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer49.Add( self.m_button24, 0, wx.ALL, 5 )
		
		
		bSizer44.Add( bSizer49, 0, wx.EXPAND, 5 )
		
		bSizer50 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Generar Examen", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.m_button25, 0, wx.ALL, 5 )
		
		
		bSizer44.Add( bSizer50, 0, wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button26.Hide()
		bSizer51.Add( self.m_button26, 0, wx.ALL, 5 )
		
		
		bSizer44.Add( bSizer51, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer44 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button23.Bind( wx.EVT_BUTTON, self.bCargarCategorias )
		self.m_button24.Bind( wx.EVT_BUTTON, self.bCargarPreguntas )
		self.m_button25.Bind( wx.EVT_BUTTON, self.bGenerarExamen )
		self.m_button26.Bind( wx.EVT_BUTTON, self.bCerrar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def bCargarCategorias( self, event ):
		event.Skip()
	
	def bCargarPreguntas( self, event ):
		event.Skip()
	
	def bGenerarExamen( self, event ):
		event.Skip()
	
	def bCerrar( self, event ):
		event.Skip()
	

