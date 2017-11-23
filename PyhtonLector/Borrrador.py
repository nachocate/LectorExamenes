#importing wx files
import wx
#import Clase_Sqlite as F 
#import the newly created GUI file
import wxMyFrame3 as mf3
import Sqlite_base as sqlb
import funciones as ff
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import time
import datetime
import os

i="/home/nacho/LectorExamenes/PyhtonLector/ImagenesPrueba/FacundoRolon2.png"
a,b,~,d=ff.CorregirExamen1(i)
print a,b,c,d