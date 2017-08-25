import wx as wxWid
import time
import datetime
import vCargarAlumnos as vca
import vCorregirExamen as vce
import vPrincipal as vp
import subprocess
import os
from math import *





app = wxWid.App(False)

frame = vp.vPrincipal(None)
frame.Show(True)

app.MainLoop()