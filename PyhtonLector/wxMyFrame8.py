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
## Class MyFrame8
###########################################################################

class MyFrame8 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 622,345 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer52 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer56 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Indique el archivo con las Categorias", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer56.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_filePicker3 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer56.Add( self.m_filePicker3, 1, wx.ALL, 5 )
		
		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Cargar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.m_button29, 0, wx.ALL, 5 )
		
		
		bSizer52.Add( bSizer56, 0, wx.EXPAND, 5 )
		
		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer68 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid8 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid8.CreateGrid( 5, 5 )
		self.m_grid8.EnableEditing( True )
		self.m_grid8.EnableGridLines( True )
		self.m_grid8.EnableDragGridSize( False )
		self.m_grid8.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid8.EnableDragColMove( False )
		self.m_grid8.EnableDragColSize( True )
		self.m_grid8.SetColLabelSize( 30 )
		self.m_grid8.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid8.EnableDragRowSize( True )
		self.m_grid8.SetRowLabelSize( 80 )
		self.m_grid8.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid8.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer68.Add( self.m_grid8, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer57.Add( bSizer68, 1, wx.EXPAND, 5 )
		
		bSizer69 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button34 = wx.Button( self, wx.ID_ANY, u"Eliminar todas", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer69.Add( self.m_button34, 0, wx.ALL, 5 )
		
		
		bSizer57.Add( bSizer69, 1, wx.EXPAND, 5 )
		
		
		bSizer52.Add( bSizer57, 0, wx.EXPAND, 5 )
		
		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button27 = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.m_button27, 0, wx.ALL, 5 )
		
		self.m_button28 = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.m_button28, 0, wx.ALL, 5 )
		
		
		bSizer52.Add( bSizer58, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer52 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button29.Bind( wx.EVT_BUTTON, self.bCargar )
		self.m_button27.Bind( wx.EVT_BUTTON, self.bGuardar )
		self.m_button28.Bind( wx.EVT_BUTTON, self.bCancelar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def bCargar( self, event ):
		event.Skip()
	
	def bGuardar( self, event ):
		event.Skip()
	
	def bCancelar( self, event ):
		event.Skip()
	

