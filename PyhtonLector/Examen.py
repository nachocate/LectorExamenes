import random

class Respuesta:
	def __init__(self,idRta,idPregunta,res,esV):
		self.res=res
		self.idRta=idRta
		self.idPregunta=idPregunta
		self.esV=esV
	def getRta(self):
		return self.res
	def getIdrta(self):
		return self.idRta
	def setIdrta(self,idrta):
		self.idRta=idrta
	def setRes(self,Res):
		self.res=Res
	def getIdPregunta(self):
		return self.idPregunta
	def getEsVerdadera(self):
		return self.esV
	
	def setIdPregunta(self,ids):
		self.idPregunta=ids
	
class Categoria:
	def __init__(self,idCategoria, nombre):
		self.nombre=nombre
		self.idCategoria=idCategoria
	def getNombre(self):
		return self.nombre
	def getId(self):
		return self.idCategoria
	
	
class Pregunta:
	def __init__(self,idpreg, pregunta,idCategoria):
		self.pregunta=pregunta
		self.idCategoria=idCategoria
		self.idPregunta=idpreg		
	def getPregunta(self):
		return self.pregunta
	def getIdCategoria(self):
		return self.idCategoria
	def getIdPregunta(self):
		return self.idPregunta


class Examen:
	def __init__(self,idexamen, nombre):
		self.nombre=nombre
		self.idExamen=idexamen
	def getNombre(self):
		return self.nombre
	def getIdExamen(self):
		return self.idExamen
	def setNombre(self,nom):
		self.nombre=nom
	def setIdExamen(self,id):
		self.idExamen=id

class ExamenFisico:
	def __init__(self,idExamen, idPregunta,pos):
		self.idExamen=idExamen
		self.idPregunta=idPregunta
		self.Pos=pos
	def getIdExamen(self):
		return self.idExamen
	def getIdPregunta(self):
		return self.idPregunta
	def getPos(self):
		return self.Pos
def serchPregunta(vecPreg,idPreg):
	for i in vecPreg:
		if i.getIdPregunta()==idPreg:
			return [True,i]
	return [False,-1]
	
def serchRta(vecRta,idPreg):
	rta=[]
	for i in vecRta:
		if i.getIdPregunta()==idPreg:
			rta.append(i)
		
	return [len(rta),rta]
def makeExamen(vecExFisico,vecPreg,vecRta,idExamen):
	rta=[]
	for i in vecExFisico:
		rtaParcial=[]
		idPreg=i.getIdPregunta()
		print idPreg
		[valor,preg]=serchPregunta(vecPreg,idPreg)
		if valor:
			rtaParcial.append(preg.getPregunta())
			[cant, rtas]=serchRta(vecRta,idPreg)
			if cant>0:
				aux=[]
				for j in range(0,5):
					aux.append(rtas[j].getRta())
				for j in i.getPos():
					rtaParcial.append(aux[j-1])
		rta.append(rtaParcial)
	return rta

def correctExamen(vecExFisico,vecPreg,vecRta,vecRtaEcha,idExamen):
	rta=[]
	for i in vecExFisico:
		pos=i.getPos()
		idPreg=i.getIdPregunta()
		[cant, rtas]=serchRta(vecRta,idPreg)
		if cant>0:
			for j in range(0,5):
				if rtas[j].getEsVerdadera():
					print j,pos[j]
					rta.append(pos[j])
	contador=0
	print rta
	print vecRtaEcha
	for j in range(0,len(rta)):
		if rta[j]==vecRtaEcha[j]:
			contador=contador+1.0
	print contador
	contador=contador/len(rta)
	return contador
		
examen=Examen(1,"Examen1")		
vCategorias=[Categoria(1,"Categoria1"),Categoria(2,"Categoria2")]
vPregunta=[]
vPregunta.append(Pregunta(1, "Pregunta1",1))
vPregunta.append(Pregunta(2, "Pregunta2",1))
vPregunta.append(Pregunta(3, "Pregunta3",1))
vPregunta.append(Pregunta(4, "Pregunta4",2))
vRtas=[]
vRtas.append(Respuesta(1,1,"rta 1",True))
vRtas.append(Respuesta(2,1,"rta 2",False))
vRtas.append(Respuesta(3,1,"rta 3",False))
vRtas.append(Respuesta(4,1,"rta 4",False))
vRtas.append(Respuesta(5,1,"rta 5",False))
	
vRtas.append(Respuesta(6,2,"rta 6",True))
vRtas.append(Respuesta(7,2,"rta 7",False))
vRtas.append(Respuesta(8,2,"rta 8",False))
vRtas.append(Respuesta(9,2,"rta 9",False))
vRtas.append(Respuesta(10,2,"rta 10",False))

vRtas.append(Respuesta(11,3,"rta 11",True))
vRtas.append(Respuesta(12,3,"rta 12",False))
vRtas.append(Respuesta(13,3,"rta 13",False))
vRtas.append(Respuesta(14,3,"rta 14",False))
vRtas.append(Respuesta(15,3,"rta 15",False))

vEfisico=[]	
vEfisico.append(ExamenFisico(1, 3,[4,2,3,1,5]))	
vEfisico.append(ExamenFisico(1, 1,[2,1,3,4,5]))	
vEfisico.append(ExamenFisico(1, 2,[1,2,3,4,5]))	
	
resultado= makeExamen(vEfisico,vPregunta,vRtas,1)
for i in resultado:
	for j in i:
		print j
rtaCorr=[4,2,2]
print correctExamen(vEfisico,vPregunta,vRtas,rtaCorr,1)
		

