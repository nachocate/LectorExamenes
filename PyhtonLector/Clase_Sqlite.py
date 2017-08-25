import sqlite3




class Sqlite_Farmacia:
	def __init__(self,nombre):
		self.nombre=nombre
		self.conn = sqlite3.connect(nombre)
	def __del__(self):
		self.conn.close()
	
	
	def get_Nombre(self,idal):
		c = self.conn.cursor()
		c.execute('select nombre from  Alumno where id='+str(idal))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]
	def get_Apellido(self,idal):
		c = self.conn.cursor()
		c.execute('select apellido from  Alumno where id='+str(idal))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]
		
	def get_Dni(self,idal):
		c = self.conn.cursor()
		c.execute('select dni from  Alumno where id='+str(idal))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]
	def get_Nota(self,idal):
		c = self.conn.cursor()
		c.execute('select nota from  Alumno where id='+str(idal))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]

	def get_Ids(self):
		c = self.conn.cursor()
		c.execute("select id from Alumno")
		l=c.fetchall()
		#l=c.fetchone()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	def set_Nota(self,idal,nota):
		c = self.conn.cursor()
		c.execute('update Alumno set nota='+str(nota)+' where id='+str(idal))
		#l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return True
	def ins_Alumno(self,nombre,apellido,dni):
		c = self.conn.cursor()
		stre="insert into Alumno(nombre,apellido,dni) values ("
		stre=stre+"'"+nombre+"'"+','
		stre=stre+"'"+apellido+"'"+','
		stre=stre+"'"+dni+"'"+")"
		print stre		
		c.execute(stre)
		#l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return True
	def del_Alumnos(self):
		c = self.conn.cursor()
		stre="delete from Alumno"
		c.execute(stre)
		self.conn.commit()
		return True


		
#c=Sqlite_Farmacia('base.db')
#print c.ins_Alumno("nacho","cate","123565")
#ids=c.get_Ids()
#print ids

#c.del_Alumnos()
#ids=c.get_Ids()
#print ids


#print c.ins_Alumno("nacho","cate","123565")

#print c.get_Nombre(1)
#print c.get_Apellido(1)
#print c.get_Dni(1)
#print c.set_Nota(1,10)
#print c.get_Nota(1)

