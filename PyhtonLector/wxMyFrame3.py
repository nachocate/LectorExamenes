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
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Corregir Examenes", pos = wx.DefaultPosition, size = wx.Size( 991,473 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Seleccione el curso a Corregir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		bSizer66.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		m_choice4Choices = []
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		bSizer66.Add( self.m_choice4, 1, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer66, 0, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Cargar Imagenes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer10.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer10.Add( self.m_dirPicker1, 1, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Cargar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button5, 0, wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Corregir Tanda de Examenes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer16.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Corregir examenes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button7, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid2.CreateGrid( 5, 5 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer11.Add( self.m_grid2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Exportar a :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer12.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Exportar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_choice4.Bind( wx.EVT_CHOICE, self.cSeleccionarCurso )
		self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.cDirectorioExamenes )
		self.m_button5.Bind( wx.EVT_BUTTON, self.cCargarExamenes )
		self.m_button7.Bind( wx.EVT_BUTTON, self.cCorregirExamenes )
		self.m_textCtrl1.Bind( wx.EVT_TEXT_ENTER, self.cNombreArchivoExportar )
		self.m_button6.Bind( wx.EVT_BUTTON, self.cExportarExamenes )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cDirectorioExamenes( self, event ):
		event.Skip()
	
	def cCargarExamenes( self, event ):
		event.Skip()
	
	def cCorregirExamenes( self, event ):
		event.Skip()
	
	def cNombreArchivoExportar( self, event ):
		event.Skip()
	
	def cExportarExamenes( self, event ):
		event.Skip()

	def cSeleccionarCurso( self, event ):
		event.Skip()


