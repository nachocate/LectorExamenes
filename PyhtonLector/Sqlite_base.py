import sqlite3




class Sqlite_base:
	
	
	def __init__(self,nombre):
		self.nombre=nombre
		self.conn = sqlite3.connect(nombre)
	def __del__(self):
		self.conn.close()
	
	def getIdAlumnoExamen(self,idExamen):
		c = self.conn.cursor()
		c.execute("select al.id from Alumno al inner join AlumnoCurso ac on al.id=ac.idAlumno where ac.idCurso=( select  ef.idCurso from ExamenFisico ef inner join Examen e on ef.idExamen=e.id where e.id= "+str(idExamen)+"  group by ef.idCurso) group by al.id")
		l=c.fetchall()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		if len(ret)==0:
			return [False, []]
		else:
			return [True,ret]
	def getIdAlumnoDni(self, dni):
		c = self.conn.cursor()
		c.execute("select id from Alumno where dni="+str(dni))
		l=c.fetchall()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		if len(ret)==0:
			return [False, []]
		else:
			return [True,ret]
	
	def getIdExamen(self):
		c = self.conn.cursor()
		c.execute("select id, nombre From Examen")
		l=c.fetchall()
		ret=[]
		for i in l:
			ret.append([i[0],str(i[1])])
		self.conn.commit()
		if len(ret)==0:
			return [False, []]
		else:
			return [True,ret]
		
	def addAlumnoCurso(self,idAlumno,idCurso):
		c = self.conn.cursor()
		stre="insert into AlumnoCurso(idAlumno,idCurso) values ("
		stre=stre+str(idAlumno)+","+str(idCurso)+")"
		print stre		
		c.execute(stre)
		self.conn.commit()
		return True
		
	
	def addCurso(self,nombre):
		c = self.conn.cursor()
		stre="insert into Curso(nombre) values ("
		stre=stre+"'"+nombre+"'"+")"
		print stre		
		c.execute(stre)
		self.conn.commit()
		return True
	def getIdCurso(self):
		c = self.conn.cursor()
		c.execute("select id from Curso")
		l=c.fetchall()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	
	def getIdCategoria(self):
		c = self.conn.cursor()
		c.execute("select id from Categoria")
		l=c.fetchall()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		if len(ret)==0:
			return [False, []]
		else:
			return [True,ret]
	def getCurso(self,id):
		c = self.conn.cursor()
		c.execute("select nombre from Curso where id="+str(id))
		ret=c.fetchone()
		self.conn.commit()
		return ret[0]
	
	
	
	def getCantidadPreguntas(self,idExamen):
		c = self.conn.cursor()
		c.execute('select count() from ExamenFisico where idExamen='+str(idExamen))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]

	def getNombre(self,idal):
		c = self.conn.cursor()
		c.execute('select nombre from Alumno where id='+str(idal))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]
	def getNombreCurso(self,idal):
		c = self.conn.cursor()
		c.execute('select nombre from  Curso where id='+str(idal))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]
	
	def getNombreCategoria(self,idal):
		c = self.conn.cursor()
		c.execute('select nombre from  Categoria where id='+str(idal))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]
	
	def get_NombreCategoria(self,idal):
		c = self.conn.cursor()
		c.execute('select nombre from  Categoria where id='+str(idal))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]
	def getApellido(self,idal):
		c = self.conn.cursor()
		c.execute('select apellido from  Alumno where id='+str(idal))
		l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return l[0][0]
	
	def getIdAlumnoCurso(self,idal):
		c = self.conn.cursor()
		c.execute("select ac.idAlumno from AlumnoCurso ac where ac.idCurso="+str(idal)+" group by ac.idAlumno")
		l=c.fetchall()
		cant=len(l)
		res=[]
		print "getIdAlumnoCurso", l
		if cant>=1:
			retorno=[]
			for i in l:
				retorno.append(i[0])
			print "ID Alumno"
			res.append(True)
			res.append(retorno)
			self.conn.commit()
		else:
			res.append(False)
			res.append([])
			self.conn.commit()
		return res
	
	def getIdPregunta(self,idal):
		c = self.conn.cursor()
		c.execute("select id from Pregunta where idCategoria="+str(idal))
		l=c.fetchall()
		cant=len(l)
		res=[]
		print "getIdPregunta", l
		if cant>=1:
			retorno=[]
			for i in l:
				retorno.append(i[0])
			print "ID Alumno"
			res.append(True)
			res.append(retorno)
			self.conn.commit()
		else:
			res.append(False)
			res.append([])
			self.conn.commit()
		return res
	
	def getCantPregCategoria(self,idal):
		c = self.conn.cursor()
		c.execute("select count(id) from Pregunta where idCategoria="+str(idal)+" group by idCategoria")
		l=c.fetchall()
		cant=len(l)
		res=[]
		print "getIdPregunta", l
		if cant>=1:
			retorno=[]
			for i in l:
				retorno.append(i[0])
			print "ID Alumno"
			res.append(True)
			res.append(retorno)
			self.conn.commit()
		else:
			res.append(False)
			res.append([])
			self.conn.commit()
		return res
	
	
	def getDni(self,idal):
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

	def getIdAlumno(self):
		c = self.conn.cursor()
		c.execute("select id from Alumno")
		l=c.fetchall()
		#l=c.fetchone()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	def get_IdsCategoria(self):
		c = self.conn.cursor()
		c.execute("select id from Categoria")
		l=c.fetchall()
		#l=c.fetchone()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	def getRespuestaPreguntaCompuesta(self,idPre):
		c = self.conn.cursor()
		c.execute("select r.id,r.respuesta, r.pos,r.verdadera from Respuesta r inner join Pregunta p on p.id=r.idPregunta where p.id="+str(idPre))
		l=c.fetchall()
		return l
	def getExamenFisicoCompuesto(self,idExa):
		c = self.conn.cursor()
		c.execute("select idPregunta,idsRespuestas,posCorrecta from ExamenFisico where idExamen="+str(idExa))
		l=c.fetchall()
		return l
		
	def set_Nota(self,idal,nota):
		c = self.conn.cursor()
		c.execute('update Alumno set nota='+str(nota)+' where id='+str(idal))
		#l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return True
	def AddExamenFisico(self,idExamen,idPregunta,vecIdsRtas,pos,idCurso):
		c = self.conn.cursor()
		stre="insert into ExamenFisico(idExamen,idPregunta,idsRespuestas,posCorrecta,idCurso) values ("+str(idExamen)+","+str(idPregunta)+","+vecIdsRtas+","+str(pos)+","+str(idCurso)+")"
		print stre		
		c.execute(stre)
		#l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return True
	
	
	def ins_Alumno(self,nombre,apellido,dni,idcurso):
		c = self.conn.cursor()
		num=self.getMaxNum(idcurso)
		stre="insert into Alumno(nombre,apellido,dni,idCurso,numero) values ("
		stre=stre+"'"+nombre+"'"+','
		stre=stre+"'"+apellido+"'"+','
		stre=stre+"'"+dni+"'"+','
		stre=stre+str(idcurso)+','
		stre=stre+str(num+1)+")"
		print stre		
		c.execute(stre)
		self.conn.commit()
		return True
	
	def getMaxNum(self, idCurso):
		c = self.conn.cursor()
		stre="select CASE WHEN max( numero)  IS NULL THEN 0 ELSE max( numero)  END  from Alumno where idCurso="+str(idCurso)
		print stre		
		c.execute(stre)
		l=c.fetchone()
		self.conn.commit()
		return l[0]
	
	def ins_Pregunta(self,pregunta,idcategoria):
		c = self.conn.cursor()
		stre="insert into Pregunta(pregunta,idCategoria) values ("
		stre=stre+"'"+pregunta+"'"+','
		stre=stre+"'"+str(idcategoria)+"'"+")"
		print stre		
		c.execute(stre)
		#l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return True
	def addExamen(self,nombre):
		c = self.conn.cursor()
		stre="insert into Examen(nombre) values ("
		stre=stre+"'"+nombre+"'"+")"
		print stre		
		c.execute(stre)
		#l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return True
	
	def getMaxIdAlumno(self):
		c = self.conn.cursor()
		c.execute("SELECT  CASE WHEN max( id)  IS NULL THEN 0 ELSE max( id)  END 'max' FROM Alumno")
		#l=c.fetchall()
		l=c.fetchone()
		self.conn.commit()
		return l[0]
	
	def getMaxIdExamen(self):
		c = self.conn.cursor()
		c.execute("SELECT  CASE WHEN max( id)  IS NULL THEN 0 ELSE max( id)  END 'max' FROM Examen")
		#l=c.fetchall()
		l=c.fetchone()
		self.conn.commit()
		return l[0]
	def getMaxIdPregunta(self):
		c = self.conn.cursor()
		c.execute("SELECT  CASE WHEN max(id)  IS NULL THEN 0 ELSE max(id)  END 'max' FROM Pregunta")
		#l=c.fetchall()
		l=c.fetchone()
		self.conn.commit()
		return l[0]
	def getMaxIdRespuesta(self):
		c = self.conn.cursor()
		c.execute("SELECT  CASE WHEN max( id)  IS NULL THEN 0 ELSE max( id)  END 'max' FROM Respuesta")
		#l=c.fetchall()
		l=c.fetchone()
		self.conn.commit()
		return l[0]	
	def getMaxIdExamen(self):
		c = self.conn.cursor()
		c.execute("SELECT  CASE WHEN max( id)  IS NULL THEN 0 ELSE max( id)  END 'max' FROM Examen")
		#l=c.fetchall()
		l=c.fetchone()
		self.conn.commit()
		return l[0]
	
	def getIdPreguntasCategoria(self,idcategoria):
		c = self.conn.cursor()
		c.execute("select id from Pregunta where idCategoria="+str(idcategoria))
		l=c.fetchall()
		#l=c.fetchone()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	
	def getIdRtaCorrecta(self,id):
		c = self.conn.cursor()
		c.execute("select id from Respuesta where idPregunta="+str(id)+" and verdadera=1" )
		l=c.fetchall()
		#l=c.fetchone()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	def getPregunta(self,id):
		c = self.conn.cursor()
		c.execute("select pregunta from Pregunta where id="+str(id))
		l=c.fetchall()
		#l=c.fetchone()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	def getIdRespuestasPregunta(self,id):
		c = self.conn.cursor()
		c.execute("select id from Respuesta where idPregunta="+str(id))
		l=c.fetchall()
		#l=c.fetchone()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	def getRespuesta(self,ids):
		c = self.conn.cursor()
		c.execute("select respuesta from Respuesta where id="+str(ids))
		l=c.fetchall()
		#l=c.fetchone()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	
	def ins_Respuesta(self,respuesta,pos,idpregunta,verdadera):
		c = self.conn.cursor()
		stre="insert into Respuesta(respuesta,pos,idPregunta,verdadera) values ("
		stre=stre+"'"+respuesta+"'"+','
		stre=stre+"'"+str(pos)+"'"+','
		stre=stre+"'"+str(idpregunta)+"'"+','
		stre=stre+"'"+str(verdadera)+"'"+")"
		print stre		
		c.execute(stre)
		#l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return True
	def del_Preguntas(self):
		c = self.conn.cursor()
		stre="delete from Pregunta"
		c.execute(stre)
		self.conn.commit()
		return True
	def del_Respuestas(self):
		c = self.conn.cursor()
		stre="delete from Respuesta"
		c.execute(stre)
		self.conn.commit()
		return True
	
#	def del_Alumnos(self):
#		c = self.conn.cursor()
#		stre="delete from Alumno"
#		c.execute(stre)
#		self.conn.commit()
#		return True
	def del_Categoria(self):
		c = self.conn.cursor()
		stre="delete from Categoria"
		c.execute(stre)
		self.conn.commit()
		return True
	def ins_Categoria(self,nombre,ids):
		c = self.conn.cursor()
		stre="insert into Categoria(nombre) values ("
		stre=stre+"'"+nombre+"'"
		stre=stre+")"
		print stre		
		c.execute(stre)
		#l=c.fetchall()
		#l=c.fetchone()
		self.conn.commit()
		return True
	def addHoja(self,idExamen,numero,cantidad):
		c = self.conn.cursor()
		c.execute("insert into Hoja(numero,idExamen,cantidad) values("+str(numero)+","+str(idExamen)+","+str(cantidad)+")")
		#l=c.fetchall()
		l=c.fetchone()
		self.conn.commit()
		return True

	def getCantidadHoja(self,idExamen,numero):
		c = self.conn.cursor()
		c.execute("select cantidad from Hoja where idExamen="+str(idExamen)+" and numero="+str(numero))
		#l=c.fetchall()
		l=c.fetchone()
		self.conn.commit()
		return l[0]
	def getInfoHoja(self,idExamen):
		c = self.conn.cursor()
		c.execute("select id,numero,cantidad from Hoja where idExamen="+str(idExamen))
		l=c.fetchall()
		ret=[]
		for i in l:
			ret.append(i[0])
		self.conn.commit()
		return ret
	def addRespuestaAlumno(self,idAlumno,idExamen,idHoja):
		c = self.conn.cursor()
		l=c.fetchone()
		self.conn.commit()
		return True
	#-------------------------------------------------------------------------------------------
	def addExamenAlumno(self,idExamen,idAlumno,hoja,totalPreg):
		c = self.conn.cursor()
		c.execute("insert into ExamenAlumno (idExamen,idAlumno,hoja,totalPreg) values ("+str(idExamen)+","+str(idAlumno)+","+str(hoja)+","+str(totalPreg)+")")
		self.conn.commit()
		return True
	def updateExamenAlumno(self,idExamen,idAlumno,hoja,correctas):
		c = self.conn.cursor()
		c.execute("update ExamenAlumno set correctas="+str(correctas)+", corregida="+str(1)+" where idExamen="+str(idExamen)+" and idAlumno="+str(idAlumno)+" and hoja="+str(hoja))
		self.conn.commit()
		return True
	def getCorregida(self,idExamen,idAlumno,hoja):
		c = self.conn.cursor()
		c.execute("select corregida from ExamenAlumno where idExamen="+str(idExamen)+" and idAlumno="+str(idAlumno)+" and hoja="+str(hoja))
		l=c.fetchone()
		self.conn.commit()
		return l[0]	
	def getCorrectas(self,idExamen,idAlumno,hoja):
		c = self.conn.cursor()
		c.execute("select correctas from ExamenAlumno where idExamen="+str(idExamen)+" and idAlumno="+str(idAlumno)+" and hoja="+str(hoja))
		l=c.fetchone()
		self.conn.commit()
		return l[0]
	
	def getResultadoParcialExamenAlumno(self,idExamen):
		c = self.conn.cursor()
		cons="select idAlumno, idExamen,sum(correctas),sum(corregida) from ExamenAlumno where idExamen="
		cons=cons+str(idExamen)+" and corregida=1 group by idAlumno"
		c.execute(cons)
		l=c.fetchall()
		#ret=[]
		#for i in l:
		#	ret.append([i[0])
		self.conn.commit()
		return l
	def getResultadoParcialTodosExamenAlumno(self,idExamen):
		c = self.conn.cursor()
		cons="select idAlumno, idExamen,sum(correctas),sum(corregida) from ExamenAlumno where idExamen="
		cons=cons+str(idExamen)+" group by idAlumno"
		c.execute(cons)
		l=c.fetchall()
		#ret=[]
		#for i in l:
		#	ret.append([i[0])
		self.conn.commit()
		return l

	def getResultadoFinalExamenAlumno(self,idExamen,cantHojas):
		c = self.conn.cursor()
		cons="select idAlumno, idExamen,sum(correctas),sum(corregida) from ExamenAlumno where idExamen="+str(idExamen)+" and corregida=1"
		cons=cons+" group by idAlumno having sum(corregida) ="+str(cantHojas)
		c.execute(cons)
		l=c.fetchall()
		#ret=[]
		#for i in l:
		#	ret.append([i[0])
		self.conn.commit()
		return l
	def getCantPreguntas(self,idExamen):
		c = self.conn.cursor()
		c.execute("select count(idPregunta) from ExamenFisico where idExamen="+str(idExamen))
		l=c.fetchone()
		self.conn.commit()
		return l[0]
	def getCantPreguntasHoja(self,idExamen,hoja):
		c = self.conn.cursor()
		c.execute("select totalPreg from ExamenAlumno where idExamen="+str(idExamen)+" and hoja="+str(hoja)+" group by idExamen")
		l=c.fetchone()
		self.conn.commit()
		return l[0]
	
	def getCantHojas(self,idExamen,pregPorExam=20):
		print "llego get cant hojas"
	
		totalPreg=self.getCantPreguntas(idExamen)
		print "total preguntas:",totalPreg
		print "preguntas por examen",pregPorExam
		cant=totalPreg/pregPorExam
		if(totalPreg%pregPorExam>0):
			cant=cant+1	
		print "cantidad de hojas",cant
		return cant

	def getIdPosCorrecta(self,idExamen):
		c = self.conn.cursor()
		c.execute("select posCorrecta from ExamenFisico where idExamen="+str(idExamen)+" order by id asc")
		l=c.fetchall()
		ret=[]
		for i in l:
			ret.append([i[0]])
		self.conn.commit()
		if len(ret)==0:
			return [False, []]
		else:
			return [True,ret]

