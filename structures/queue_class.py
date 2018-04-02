import random

class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.nodes = []
		self.assignments = 0
		self.equations = 0

# --- ZWRACA ROZMIAR KOLEJKI ---
	def size(self):
		return len(self.nodes)

# --- WYŚWIETLA CAŁĄ KOLEJKĘ ---
	def showQueue(self):
		string = 'Kolejka ['
		for nod in self.nodes:
			string += str(nod) + ', '
		
		string = string[:-2]
		string += ']'
		print(string)

# --- ZWRACA LICZBĘ PRZYPISAŃ ---
	def getAssignments(self):
		return self.assignments

# --- ZWRACA LICZBĘ PORÓWNAŃ ---
	def getEquations(self):
		return self.equations

# --- ZWRACA KONKRETNY ELEMENT KOLEJKI ---
	def element(self, position):
		if position == 1:
			self.equations += 1
			return self.nodes[0]
		else:
			self.equations += 1
			self.assignments += 1
			self.temp = []
			self.tempSize = Queue.size(self)
			for i in range(1, self.tempSize+1):		
				self.temp.append(self.nodes[0])
				Queue.pop(self)

			for i in range(1, self.tempSize+1):	
				self.nodes.append(self.temp[0])
				self.temp.pop(0)

				if i == position-1:
					elem = self.temp[0]	
		return elem
		
# --- DODAJE ELEMENT ---
	def push(self, node, position = None):
		if position == 0: 
			position = 1
		if position is None or position > Queue.size(self) or Queue.size(self) == 0:
			self.equations += 1
			self.nodes.append(node)
		else:
			self.equations += 1
			self.temp = []
			self.tempSize = Queue.size(self)
			for i in range(1, self.tempSize+1):				
				self.temp.append(self.nodes[0])
				Queue.pop(self)
				self.assignments += 1

			for i in range(1, self.tempSize+1):				
				if i == position:
					self.nodes.append(node)
				self.nodes.append(self.temp[0])
				self.temp.pop(0)
				self.assignments += 1

# --- USUWA ELEMENT ---
	def pop(self, position = 1):
		if position == 0 or position == 1:
			self.equations += 1
			self.nodes.pop(0)
		else:
			self.equations += 1
			self.temp = []
			self.tempSize = Queue.size(self)

			for i in range(1, self.tempSize+1):	
				self.assignments += 1
				if i != position:		
					self.temp.append(self.nodes[0])
					self.nodes.pop(0)
				else:
					self.nodes.pop(0)

			for i in range(0, self.tempSize-1):	
				self.assignments += 1			
				self.nodes.append(self.temp[i])

# === KONIEC KLASY ===


# --- DODAWANIE ELEMETÓW PO KOLEI ---
def addOneByOne(kolejka = Queue):
	kolejka.equations = 0
	kolejka.assignments = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		kolejka.push(lol)
		print(lol)

	kolejka.showQueue()
	print("Liczba operacji porównania: " + str(kolejka.getEquations()))
	print("Liczba operacji przypisania: " + str(kolejka.getAssignments()))

# --- DODAWANIE ELEMENTÓW W LOSOWE MIEJSCA ---
def addRandom(kolejka = Queue):
	kolejka.equations = 0
	kolejka.assignments = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		kolejka.push(lol, random.randint(0, kolejka.size()))
		print(lol)
	kolejka.showQueue()
	print("Liczba operacji porównania: " + str(kolejka.getEquations()))
	print("Liczba operacji przypisania: " + str(kolejka.getAssignments()))

# --- DODAWANIE ELEMENTÓW PO PRZECIWNYCH STRONACH
def addOnSides(kolejka = Queue):
	kolejka.equations = 0
	kolejka.assignments = 0
	tmp = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		tmp += 1

		if tmp % 2 == 1:
			kolejka.push(lol, 1)
		else:
			kolejka.push(lol)
		print(lol)

	kolejka.showQueue()
	print("Liczba operacji porównania: " + str(kolejka.getEquations()))
	print("Liczba operacji przypisania: " + str(kolejka.getAssignments()))

# --- WYSZUKIWANIE WSZYSTKICH ELEMENTÓW ---
def printAllElements(kolejka = Queue):
	kolejka.equations = 0
	kolejka.assignments = 0
	for x in range(1,26):

		print()
		print(str(x) + ". " + str(kolejka.element(x)))
		print("Liczba operacji porównania: " + str(kolejka.getEquations()))
		print("Liczba operacji przypisania: " + str(kolejka.getAssignments()))

		kolejka.equations = 0
		kolejka.assignments = 0


# --- USUWANIE KOLEJNYCH ELEMENTÓW ---
def popElements(kolejka = Queue):
	kolejka.equations = 0
	kolejka.assignments = 0
	for x in range(1,26):
		print()
		print("usuwam element nr " + str(x))

		tmp = kolejka.element(x)
		kolejka.equations = 0
		kolejka.assignments = 0
		kolejka.pop(x)
		kolejka.showQueue()

		print("Liczba operacji porównania: " + str(kolejka.getEquations()))
		print("Liczba operacji przypisania: " + str(kolejka.getAssignments()))
		kolejka.push(tmp, x)


