def getExamenMesclado(self,cant):
		print self.cantPreguntas+1
		items=range(1,self.cantPreguntas+1)

		self.randomPreg=random.sample(items,self.cantPreguntas)
		print self.randomPreg
		for i in self.preguntas:
			items2=range(1,i.getCantRtas()+1)
			vecAux1=random.sample(items2,len(items2))
			self.randomRta.append(vecAux1)
		Mat=[]
		for i in range(0,cant):
			vec=[]
			indPreg=self.randomPreg[i]-1
			print indPreg
			print len(self.preguntas)
			print self.preguntas[indPreg].getPregunta()
			vec.append(self.preguntas[indPreg].getPregunta())
			print self.randomRta
			print indPreg
			for j in self.randomRta[indPreg]:
				print j
				print j
				print self.preguntas[indPreg].getRta(j-1)
				vec.append(self.preguntas[indPreg].getRta(j-1))
			Mat.append(vec)
		return Mat
			
		#random.sample(items,3) 
	def getResultadoCorrecto(self):
		self.
