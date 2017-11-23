# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame6
###########################################################################

class MyFrame6 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1311,682 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Nombre del Examen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer28.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		bSizer67 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Seleccione el curso destinado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		bSizer67.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		m_choice5Choices = []
		self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		bSizer67.Add( self.m_choice5, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer67, 0, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Seleccione Categoria", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer29.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer29.Add( self.m_choice2, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Cantidad de Preguntas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer29.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Cargar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button15, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer29, 0, wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid5 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid5.CreateGrid( 1, 5 )
		self.m_grid5.EnableEditing( True )
		self.m_grid5.EnableGridLines( True )
		self.m_grid5.EnableDragGridSize( False )
		self.m_grid5.SetMargins( 20, 100 )
		
		# Columns
		self.m_grid5.EnableDragColMove( False )
		self.m_grid5.EnableDragColSize( True )
		self.m_grid5.SetColLabelSize( 30 )
		self.m_grid5.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid5.EnableDragRowSize( True )
		self.m_grid5.SetRowLabelSize( 80 )
		self.m_grid5.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid5.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer40.Add( self.m_grid5, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer30.Add( bSizer40, 0, wx.EXPAND, 5 )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Borrar Seleccionada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button16.Hide()
		bSizer41.Add( self.m_button16, 0, wx.ALL, 5 )
		
		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Borrar todas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button17.Hide()
		bSizer41.Add( self.m_button17, 0, wx.ALL, 5 )
		
		
		bSizer30.Add( bSizer41, 1, 0, 5 )
		
		
		bSizer27.Add( bSizer30, 0, wx.EXPAND, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Para generar el examen apriete Generar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer31.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Generar Examen", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_button18, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer31, 0, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Detalle del examen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer32.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer32, 0, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid6.CreateGrid( 1, 6 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 100 )
		
		# Columns
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 30 )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelSize( 80 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer33.Add( self.m_grid6, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer33, 0, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Selección de alumnos para dicho examen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.Hide()
		
		bSizer34.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid7 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid7.CreateGrid( 5, 5 )
		self.m_grid7.EnableEditing( True )
		self.m_grid7.EnableGridLines( True )
		self.m_grid7.EnableDragGridSize( False )
		self.m_grid7.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid7.EnableDragColMove( False )
		self.m_grid7.EnableDragColSize( True )
		self.m_grid7.SetColLabelSize( 30 )
		self.m_grid7.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid7.EnableDragRowSize( True )
		self.m_grid7.SetRowLabelSize( 80 )
		self.m_grid7.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid7.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid7.Hide()
		
		bSizer42.Add( self.m_grid7, 0, wx.ALL, 5 )
		
		
		bSizer35.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		bSizer44 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Todos los de la lista", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button19.Hide()
		
		bSizer44.Add( self.m_button19, 0, wx.ALL, 5 )
		
		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Solo seleccionados", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button20.Hide()
		
		bSizer44.Add( self.m_button20, 0, wx.ALL, 5 )
		
		
		bSizer35.Add( bSizer44, 1, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer35, 0, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Seleccione un directorio o capeta donde se generaran los examenes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.Hide()
		
		bSizer36.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer36, 0, wx.EXPAND, 5 )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Seleccionar Ubicación donde guardar los examenes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer37.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer37.Add( self.m_dirPicker2, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer37, 0, wx.EXPAND, 5 )
		
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Guardar Exámenes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer38.Add( self.m_button21, 0, wx.ALL, 5 )
		
		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button22.Hide()
		bSizer38.Add( self.m_button22, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer38, 0, wx.EXPAND, 5 )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer27.Add( bSizer39, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer27 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button15.Bind( wx.EVT_BUTTON, self.bCargarPreguntas )
		self.m_button16.Bind( wx.EVT_BUTTON, self.bBorrarSeleccionadas )
		self.m_button17.Bind( wx.EVT_BUTTON, self.bBorrarTodas )
		self.m_button18.Bind( wx.EVT_BUTTON, self.bGenerarExamen )
		self.m_button19.Bind( wx.EVT_BUTTON, self.bSeleccionarTodos )
		self.m_button20.Bind( wx.EVT_BUTTON, self.bSeleccionados )
		self.m_button21.Bind( wx.EVT_BUTTON, self.bExportarExamenes )
		self.m_button22.Bind( wx.EVT_BUTTON, self.bCancelar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def bCargarPreguntas( self, event ):
		event.Skip()
	
	def bBorrarSeleccionadas( self, event ):
		event.Skip()
	
	def bBorrarTodas( self, event ):
		event.Skip()
	
	def bGenerarExamen( self, event ):
		event.Skip()
	
	def bSeleccionarTodos( self, event ):
		event.Skip()
	
	def bSeleccionados( self, event ):
		event.Skip()
	
	def bExportarExamenes( self, event ):
		event.Skip()
	
	def bCancelar( self, event ):
		event.Skip()
	

