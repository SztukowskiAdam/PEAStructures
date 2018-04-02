import random

class Table(object):
	"""docstring for Table"""
	def __init__(self):
		self.evidence = []
		self.assignments = 0
		self.equations = 0
		self.temp = []

	def size(self):
		return len(self.evidence)

# --- ZWRACA LICZBĘ PRZYPISAŃ ---
	def getAssignments(self):
		return self.assignments

# --- ZWRACA LICZBĘ PORÓWNAŃ ---
	def getEquations(self):
		return self.equations

# --- WYŚWIETLA CAŁĄ TABLICĘ ---
	def showTable(self):
		string = 'Tablica ['
		for value in self.evidence:
			string += str(value) + ', '
		string = string[:-2]
		string += ']'
		print(string)

# --- ZWRACA KONKRETNY ELEMENT TABLICY ---
	def element(self, position):
		return self.evidence[position-1]

# --- DODAJE ELEMENT DO TABLICY ---
	def push(self, data, position = 1):

		for i in range(len(self.evidence)):
			self.assignments += 1
			self.temp.append(self.evidence.pop(0))

		self.assignments += 1
		self.temp.insert(position-1, data)

		for i in range(len(self.temp)):
			self.assignments += 1
			self.evidence.append(self.temp.pop(0))

# --- USUWA ELEMENT Z TABLICY ---
	def pop(self,position = 1):
		for i in range(len(self.evidence)):
			self.assignments += 1
			self.temp.append(self.evidence.pop(0))

		self.assignments += 1
		self.temp.pop(position-1)

		for i in range(len(self.temp)):
			self.assignments += 1
			self.evidence.append(self.temp.pop(0))




# --- DODAWANIE ELEMETÓW PO KOLEI ---
def addOneByOne(table = Table):
	table.assignments = 0
	table.equations = 0
	lol = 0
	for x in range(0,25):
		lol = random.randint(0,300)
		table.push(lol)
		print(lol)

	table.showTable()
	print("Liczba operacji porównania: " + str(table.getEquations()))
	print("Liczba operacji przypisania: " + str(table.getAssignments()))

# --- DODAWANIE ELEMENTÓW W LOSOWE MIEJSCA ---
def addRandom(table = Table):
	table.assignments = 0
	table.equations = 0
	lol = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		table.push(lol, random.randint(0, table.size()))
		print(lol)
	table.showTable()
	print("Liczba operacji porównania: " + str(table.getEquations()))
	print("Liczba operacji przypisania: " + str(table.getAssignments()))

# --- DODAWANIE ELEMENTÓW PO PRZECIWNYCH STRONACH
def addOnSides(table = Table):
	table.assignments = 0
	table.equations = 0
	tmp = 0
	lol = 0
	for x in range(0,25):
		tmp += 1
		lol = random.randint(0,300)
		print(lol)

		if tmp % 2 == 1:
			table.push(lol, table.size()+1)
		else:
			table.push(lol)

	table.showTable()
	print("Liczba operacji porównania: " + str(table.getEquations()))
	print("Liczba operacji przypisania: " + str(table.getAssignments()))

# --- WYSZUKIWANIE WSZYSTKICH ELEMENTÓW ---
def printAllElements(table = Table):
	table.assignments = 0
	table.equations = 0
	for x in range(1,26):
		print()
		print(str(x) + ". " + str(table.element(x)))
		print("Liczba operacji porównania: " + str(table.getEquations()))
		print("Liczba operacji przypisania: " + str(table.getAssignments()))

		table.assignments = 0
		table.equations = 0


# --- USUWANIE KOLEJNYCH ELEMENTÓW ---
def popElements(table = Table):
	table.assignments = 0
	table.equations = 0
	for x in range(1,26):
		print()
		print("usuwam element: " + str(table.element(x)))

		tmp = table.element(x)
		table.assignments = 0
		table.equations = 0
		table.pop(x)
		table.showTable()

		print("Liczba operacji porównania: " + str(table.getEquations()))
		print("Liczba operacji przypisania: " + str(table.getAssignments()))
		table.push(tmp, x)

				


		