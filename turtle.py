import subprocess,time
'''
карта для черепашки (двумерный массив). 0 - пустое пространство, 1 - стена, 5 - цель
'''
polygon = [[0,0,0,0,0,0],
		   [0,0,0,0,0,0],
		   [0,1,1,1,0,0],
		   [0,0,0,0,0,0],
		   [0,0,0,0,0,0],
		   [0,0,5,0,0,0]]

class turtle:
	def __init__(self,loc,targetValue,startX = 0,startY = 0):
		'''
		Задаем стартовую позицию(self.startPos), позицию черепахи(self.x self.y), карту для передвижения (self.loc)
		и целевое значение (self.tagetValue)
		'''
		self.x = startX
		self.y = startY
		self.startPos = {"x":startX,"y":startY}
		self.loc = loc
		self.targetValue = targetValue


	def up(self):
		'''
		Двигаем черепаху наверх если это не выходит за пределы карты
		'''
		self.y-=1
		if self.y<0:
			self.y = 0
		return self.x,self.y


	def down(self):
		'''
		Двигаем черепаху вниз если это не выходит за пределы карты
		'''
		self.y+=1
		if self.y>len(self.loc)-1:
			print("-------")
			self.y = len(self.loc)-1
		return self.x,self.y


	def left(self):
		'''
		Двигаем черепаху влево если это не выходит за пределы карты
		'''
		self.x-=1
		if self.x<0:
			print("-------")
			self.x = 0
		return self.x,self.y


	def right(self):
		'''
		Двигаем черепаху вправо если это не выходит за пределы карты
		'''
		self.x+=1
		if self.x>len(self.loc[0])-1:
			print("-------")
			self.x = len(self.loc[0])-1
		return self.x,self.y


	def goToStartPos(self):
		'''
		Кидаем черепаху на стартовую позицию
		'''
		self.x, self.y = self.startPos['x'],self.startPos['y']
		return self.x,self.y


	def cellChecker(self, **kwargs):
		'''
		Выводим содержимое ячейки (по умолчанию проверяется та в которой стоит черепаха)
		'''		 
		try:
			y = kwargs['y']
			x = kwargs['x']
		except Exception:
			y = self.y
			x = self.x

		return self.loc[y][x]


	def endChecker(self):
		'''
		Проверяет находится ли черепаха в целевой ячейке
		'''
		if self.cellChecker() == self.targetValue:
			return True
		else:
			return False


	def getTarget(self):
		'''
		возвращает координаты цели
		'''
		for y in range(len(self.loc)):
			for x in range(len(self.loc[y])):
				if self.loc[y][x] == self.targetValue:
					return x,y

###################################################################################################
###########################################__MAIN_FUNCS__##########################################
###################################################################################################

def drawMatrix(m):
	'''
	отрисовываем кадр (нынешнее состояние массива)
	'''
	mtx = "╔"+"═"*len(m[0])+"╗"
	for i in m:
		mtx += "\n║"
		for j in i:
			mtx+=str(j)
		mtx += "║"
	mtx += "\n╚"+"═"*len(m[0])+"╝"
	print(mtx)
	return mtx


turt = turtle(loc = polygon,targetValue = 5)
targetPos = turt.getTarget()

tX,tY = targetPos[0],targetPos[1]
step = 0 
pre_X,pre_Y = 0,0

turt.goToStartPos()

while not turt.endChecker():
	#отрисовочка
	subprocess.call("cls",shell = True) #очищаем экран

	polygon[pre_Y][pre_X] = 0
	polygon[turt.y][turt.x] = 3
	
	drawMatrix(polygon) #рисуем новый кадр
	#===============================================

	#тут писать алгоритм
	
	#===============================================
	preX,preY = turt.x,turt.y
	
	print("x:",turt.x,"y:",turt.y)
	print("target - ","x:",tX,"y:",tY)
	print("step:",step)

	time.sleep(2)

##########################
print("Finish!")
##########################