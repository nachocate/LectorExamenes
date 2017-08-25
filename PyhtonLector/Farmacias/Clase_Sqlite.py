import sqlite3




class Sqlite_Farmacia:
	def __init__(self,nombre):
		self.nombre=nombre
		self.conn = sqlite3.connect(nombre)
	def __del__(self):
		self.conn.close()
	
	
	def get_Fechas(self):
		c = self.conn.cursor()
		c.execute('select fecha_inicio from fecha_turno')
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l
		
	
	
	def get_Farmacias(self):
		c = self.conn.cursor()
		c.execute('select nombre, direccion, telefono from farmacia')
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l
		
		
	def get_Farmacias_de_Turno(self,fec):
		c = self.conn.cursor()
		fecha="'"+fec+"'"
		consulta=("select F.nombre,F.direccion,F.telefono  from fecha_turno R inner join turno T on T.id=R.id_turno  inner join grupo G on  G.id_turno = T.id  inner join farmacia F on F.id= G.id_farmacia where fecha_inicio="+fecha)
		c.execute(consulta)
		l=c.fetchall()
		self.conn.commit()
		return l



		
#c=Sqlite_Farmacia('Farmacia.dbo')
#print(c.get_Cant_Farmacias())	
#l=c.get_Farmacias()
#for i in l:
#	print(str(i[0])+ " " +i[1]) 
#c.get_Farmacias_de_Turno("2-10-2010")
