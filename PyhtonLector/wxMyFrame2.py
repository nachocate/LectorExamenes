# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul  7 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cargar Alumnos", pos = wx.DefaultPosition, size = wx.Size( 777,346 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer63 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Seleccione el Curso", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer63.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer63.Add( self.m_choice3, 1, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer63, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Selecciones el archivo de alumnos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer6.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer6.Add( self.m_filePicker1, 1, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Cargar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer64 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer64.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer64, 1, wx.EXPAND, 5 )
		
		bSizer65 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button33 = wx.Button( self, wx.ID_ANY, u"Borrar Todos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button33.Hide()
		bSizer65.Add( self.m_button33, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer65, 0, 0, 5 )
		
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_choice3.Bind( wx.EVT_CHOICE, self.cSeleccionarCurso )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.cArchivoAlumnos )
		self.m_button4.Bind( wx.EVT_BUTTON, self.cCargarAlumnos )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cArchivoAlumnos( self, event ):
		event.Skip()
	
	def cCargarAlumnos( self, event ):
		event.Skip()
	
	def cSeleccionarCurso( self, event ):
		event.Skip()
