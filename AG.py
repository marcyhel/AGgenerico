
from multiprocessing import Pool 
import multiprocessing
import random
import copy

class Individuo:
	def __init__(self,inicia=None):
		self.pontos=0
		self.pontos_t=0
		self.volta=0
		self.id=int(random.random()*1000)
		self.ini_d=inicia

	def void():
		pass
	def inicia(self):
		if(self.ini_d!=None):

			self.ini_d()

		return self
	def update(self):
		pass
	def cross(a,b):
		pass
	def muta(self):
		pass

	def reset_individuo(self,func=void):
		self.pontos=0
		self.pontos_t=0
		self.volta=0
		func()
	def semi_reset_individuo(self,func=void):
		self.pontos=0
		func()
	def end(self):
		pass

class Temp_pool:
	def __call__(self, indiv):
		d=copy.deepcopy(indiv)

		d.update()
		d.pontos_t+=d.pontos
		return d
class Genetico:
	def __init__(self,individuo,geracao=3,indiv=10,indiv_selec=3,mutacao=0.3,cross=0.7,voltas=1,call_inicio=True,ordena='d',show_v=False,show_g=False,thread=multiprocessing.cpu_count()):
		self.geracao=geracao
		self.indiv=indiv
		self.mutacao=mutacao
		self.indiv_selec=indiv_selec
		self.cross=cross
		self.voltas=voltas
		self.call_inicio=call_inicio
		self.individuo=individuo
		self.list_indiv=[]
		self.melhores=[]
		self.cont_geracao=0
		self.ordena=ordena
		self.show_v=show_v
		self.show_g=show_g
		self.pool = Pool(thread)
		print("Número de thread : ",thread)
	def cria_populacao(self):
		for i in range(self.indiv):
			self.list_indiv.append(copy.deepcopy(self.individuo))
			
			if(self.call_inicio):
				#print("inicia")
				self.list_indiv[-1:][0].inicia()
			self.list_indiv[-1:][0].id='g: '+str(self.cont_geracao)+' - i: '+str(i)#int(random.random()*1000)
	def update(self):
		#att = xmp.Vectorizer(self.att_individual, num_workers=2)
		#result=att.process(copy.deepcopy(self.list_indiv))


		result=self.pool.map(Temp_pool(),list(self.list_indiv))
		self.list_indiv=copy.deepcopy(list(result))
		#for i in self.list_indiv:
		#	i.update()
		#	i.pontos_t+=i.pontos
	def ordenar(self):
		if(self.ordena=='d'):
			aux=0
			for i in range(len(self.list_indiv)):
				for c in range(len(self.list_indiv)):
					if(self.list_indiv[i].pontos>self.list_indiv[c].pontos):
						aux=copy.deepcopy(self.list_indiv[i])
						self.list_indiv[i]=copy.deepcopy(self.list_indiv[c])
						self.list_indiv[c]=copy.deepcopy(aux)	
		if(self.ordena=='c'):
			aux=0
			for i in range(len(self.list_indiv)):
				for c in range(len(self.list_indiv)):
					if(self.list_indiv[i].pontos<self.list_indiv[c].pontos):
						aux=copy.deepcopy(self.list_indiv[i])
						self.list_indiv[i]=copy.deepcopy(self.list_indiv[c])
						self.list_indiv[c]=copy.deepcopy(aux)
	def ordenar_t(self):
		if(self.ordena=='d'):
			aux=0
			for i in range(len(self.list_indiv)):
				for c in range(len(self.list_indiv)):
					if(self.list_indiv[i].pontos_t>self.list_indiv[c].pontos_t):
						aux=copy.deepcopy(self.list_indiv[i])
						self.list_indiv[i]=copy.deepcopy(self.list_indiv[c])
						self.list_indiv[c]=copy.deepcopy(aux)
		if(self.ordena=='c'):
			aux=0
			for i in range(len(self.list_indiv)):
				for c in range(len(self.list_indiv)):
					if(self.list_indiv[i].pontos_t<self.list_indiv[c].pontos_t):
						aux=copy.deepcopy(self.list_indiv[i])
						self.list_indiv[i]=copy.deepcopy(self.list_indiv[c])
						self.list_indiv[c]=copy.deepcopy(aux)

	def get_melhores(self):
		self.melhores=copy.deepcopy(self.list_indiv[:self.indiv_selec])
		self.list_indiv=copy.deepcopy(self.melhores)
	def semi_reset(self):
		for i in self.list_indiv:
			i.semi_reset_individuo()
	def reset(self):
		for i in self.list_indiv:
			i.reset_individuo()
	def crossOver(self):
		for i in range(self.indiv-self.indiv_selec):
			self.list_indiv.append(copy.deepcopy(self.individuo))
			self.list_indiv[-1:][0].inicia()
			self.list_indiv[-1:][0].id='g: '+str(self.cont_geracao+1)+' - i: '+str(i)
			if(self.cross>random.random()):
				a,b=random.sample(self.melhores,2)
				self.list_indiv[-1:][0].cross(a,b)
			if(self.mutacao>random.random()):
				self.list_indiv[-1:][0].muta()
		  
	def iniciar(self):
		self.cria_populacao()

		while True:
			self.reset()
			for i in range(self.voltas):
				self.semi_reset()
				self.update()
				self.ordenar()
				self.get_melhores()
				if(self.show_v):
					print("   --- v: {} ---".format(i))
					for i in self.melhores:
						print('   id: {} - pontos: {}'.format(i.id,i.pontos))

			self.ordenar_t()
			self.get_melhores()
			if(self.show_g):
				print("------- G: {} ------".format(self.cont_geracao))
				for i in self.melhores:
					print('id: {} - pontos: {}'.format(i.id,i.pontos_t))
				self.melhores[0].end()
				print('--------------------------------')
			self.crossOver()

			self.cont_geracao+=1
			if(self.cont_geracao == self.geracao and self.geracao!=0):
				break
		self.melhores[0].end()

