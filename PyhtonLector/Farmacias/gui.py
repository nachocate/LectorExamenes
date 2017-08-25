# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Farmacias", pos = wx.DefaultPosition, size = wx.Size( 359,534 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Listado De Farmacias", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer13.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer13 )
		self.m_panel1.Layout()
		bSizer13.Fit( self.m_panel1 )
		bSizer12.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.wx_grilla = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.wx_grilla.CreateGrid( 0, 0 )
		self.wx_grilla.EnableEditing( True )
		self.wx_grilla.EnableGridLines( True )
		self.wx_grilla.EnableDragGridSize( False )
		self.wx_grilla.SetMargins( 0, 0 )
		
		# Columns
		self.wx_grilla.AutoSizeColumns()
		self.wx_grilla.EnableDragColMove( False )
		self.wx_grilla.EnableDragColSize( True )
		self.wx_grilla.SetColLabelSize( 30 )
		self.wx_grilla.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.wx_grilla.AutoSizeRows()
		self.wx_grilla.EnableDragRowSize( True )
		self.wx_grilla.SetRowLabelSize( 0 )
		self.wx_grilla.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.wx_grilla.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		bSizer2.Add( self.wx_grilla, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Farmacias de Turno", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button9, 1, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Farmacias", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button10, 1, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Farmacias por Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button11, 1, wx.ALL, 5 )
		
		ch_FechasChoices = []
		self.ch_Fechas = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_FechasChoices, 0 )
		self.ch_Fechas.SetSelection( 0 )
		bSizer11.Add( self.ch_Fechas, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer8, 1, 0, 5 )
		
		
		bSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button9.Bind( wx.EVT_BUTTON, self.Boton_Farm_Turno )
		self.m_button10.Bind( wx.EVT_BUTTON, self.Boton_Farm )
		self.m_button11.Bind( wx.EVT_BUTTON, self.Boton_Farm_Fecha )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Boton_Farm_Turno( self, event ):
		event.Skip()
	
	def Boton_Farm( self, event ):
		event.Skip()
	
	def Boton_Farm_Fecha( self, event ):
		event.Skip()
	

