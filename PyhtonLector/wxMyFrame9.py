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
## Class MyFrame9
###########################################################################

class MyFrame9 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crear Curso", pos = wx.DefaultPosition, size = wx.Size( 452,471 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer58 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Ingrese nombre del curso", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer60.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.m_textCtrl5, 1, wx.ALL, 5 )
		
		self.m_button31 = wx.Button( self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.m_button31, 0, wx.ALL, 5 )
		
		
		bSizer58.Add( bSizer60, 0, wx.EXPAND, 5 )
		
		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer58.Add( bSizer62, 1, wx.EXPAND, 5 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid9 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid9.CreateGrid( 0, 1 )
		self.m_grid9.EnableEditing( True )
		self.m_grid9.EnableGridLines( True )
		self.m_grid9.EnableDragGridSize( False )
		self.m_grid9.SetMargins( 0, 300 )
		
		# Columns
		self.m_grid9.EnableDragColMove( False )
		self.m_grid9.EnableDragColSize( True )
		self.m_grid9.SetColLabelSize( 30 )
		self.m_grid9.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid9.EnableDragRowSize( True )
		self.m_grid9.SetRowLabelSize( 80 )
		self.m_grid9.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid9.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer61.Add( self.m_grid9, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer58.Add( bSizer61, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer58 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button31.Bind( wx.EVT_BUTTON, self.clickAgregarCurso )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def clickAgregarCurso( self, event ):
		event.Skip()
	

