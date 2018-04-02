import random

class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.data = []
		self.equations = 0
		self.assignments = 0

	def __str__(self):
		return str(self.data)

# --- ZWRACA ROZMIAR LISTY ---
	def size(self):
		return len(self.data)

# --- ZWRACA INFORMACJĘ O TYM CZY STOS JEST PUSTY ---
	def empty(self):
		if len(self.data) != 0:
			return True
		else:
			return False

# --- ZWRACA LICZBĘ PRZYPISAŃ ---
	def getAssignments(self):
		return self.assignments

# --- ZWRACA LICZBĘ PORÓWNAŃ ---
	def getEquations(self):
		return self.equations

# --- WYŚWIETLA CAŁY STOS ---
	def showStack(self):
		string = 'Stos ['
		for data in self.data:
			string += str(data) + ', '
		string = string[:-2]
		string += ']'
		print(string)

# --- ZWRACA KONKRETNY ELEMENT ---
	def element(self, position):

		if position == 1:
			self.equations += 1
			return self.data[0]
		else:
			self.equations += 1
			self.temp = []

			for i in range(1, position):
				self.assignments += 1
				self.temp.insert(0, self.data[0])
				self.data.pop(0)

			elem = self.data[0]

			for i in range(1, position):
				self.assignments += 1
				self.data.insert(0, self.temp[0])
				self.temp.pop(0)

			return elem

# --- DODAJE ELEMENT ---
	def push(self, data, position = None):

		if position is None or position == 1:
			self.equations += 1
			self.assignments += 1
			self.data.insert(0, data)
		else:
			self.equations += 1
			self.temp = []

			for i in range(1, position):
				self.assignments += 1
				self.temp.insert(0, self.data[0])
				self.data.pop(0)

			self.assignments += 1
			self.data.insert(0, data)
			for i in range(1, position):
				self.assignments += 1
				self.data.insert(0, self.temp[0])
				self.temp.pop(0)

# --- USUWA ELEMENT ---
	def pop(self, position = None):

		if position is None or position == 1:
			self.equations += 1
			self.assignments += 1
			self.data.pop(0)

		else:
			self.equations += 1
			self.temp = []

			for i in range(1, position):
				self.assignments += 1
				self.temp.insert(0, self.data[0])
				self.data.pop(0)

			self.assignments += 1
			self.data.pop(0)
			for i in range(1, position):
				self.assignments += 1
				self.data.insert(0, self.temp[0])
				self.temp.pop(0)

# === KONIEC KLASY ===


# --- DODAWANIE ELEMETÓW PO KOLEI ---
def addOneByOne(stos = Stack):
	stos.assignments = 0
	stos.equations = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		stos.push(lol)
		print(lol)

	stos.showStack()
	print("Liczba operacji porównania: " + str(stos.getEquations()))
	print("Liczba operacji przypisania: " + str(stos.getAssignments()))

# --- DODAWANIE ELEMENTÓW W LOSOWE MIEJSCA ---
def addRandom(stos = Stack):
	stos.assignments = 0
	stos.equations = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		stos.push(lol, random.randint(0, stos.size()))
	stos.showStack()
	print("Liczba operacji porównania: " + str(stos.getEquations()))
	print("Liczba operacji przypisania: " + str(stos.getAssignments()))

# --- DODAWANIE ELEMENTÓW PO PRZECIWNYCH STRONACH
def addOnSides(stos = Stack):
	stos.assignments = 0
	stos.equations = 0
	tmp = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		tmp += 1

		if tmp % 2 == 1:
			stos.push(lol, stos.size()+1)
		else:
			stos.push(lol)
		print(lol)

	stos.showStack()
	print("Liczba operacji porównania: " + str(stos.getEquations()))
	print("Liczba operacji przypisania: " + str(stos.getAssignments()))

# --- WYSZUKIWANIE WSZYSTKICH ELEMENTÓW ---
def printAllElements(stos = Stack):
	stos.assignments = 0
	stos.equations = 0
	for x in range(1,26):
		print()
		print(str(x) + ". " + str(stos.element(x)))
		print("Liczba operacji porównania: " + str(stos.getEquations()))
		print("Liczba operacji przypisania: " + str(stos.getAssignments()))

		stos.assignments = 0
		stos.equations = 0


# --- USUWANIE KOLEJNYCH ELEMENTÓW ---
def popElements(stos = Stack):
	stos.assignments = 0
	stos.equations = 0
	for x in range(1,26):
		print()
		print("usuwam element: " + str(stos.element(x)))

		tmp = stos.element(x)
		stos.assignments = 0
		stos.equations = 0
		stos.pop(x)
		stos.showStack()

		print("Liczba operacji porównania: " + str(stos.getEquations()))
		print("Liczba operacji przypisania: " + str(stos.getAssignments()))
		stos.push(tmp, x)



