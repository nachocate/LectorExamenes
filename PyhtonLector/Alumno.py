
class Alumno:
	def __init__(self, nombre,apellido,dni,iden):
		self.nombre=nombre
		self.apellido=apellido
		self.dni=dni
		self.iden=iden
		self.nota=-1;

	def asignarNota(self,nota):
		self.nota=nota
		return self.nota ,True
	def csvFila(self):
		return str(self.iden)+","+self.nombre+","+self.apellido+","+self.dni+","+str(self.nota)
	def getNombre(self):
		return self.nombre
	def getApellido(self):
		return self.apellido
	def getDni(self):
		return self.dni
	def getId(self):
		return self.iden
	def getNota(self):
		return self.nota
