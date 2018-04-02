import random

class Node(object):
	"""docstring for Node"""
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next

	def __str__(self):
		return 'Node [' + str(self.value) + ']'

class OneWayList(object):
	"""docstring for OneWayList"""
	def __init__(self):
		self.first = None
		self.last = None
		self.assignments = 0
		self.equations = 0

	def __str__(self):
		if self.first != None:
			current = self.first
			out = 'OneWayList [' + str(current.value) + ', '

			while current.next != None:
				current = current.next
				out += str(current.value) + ', '
			return out[:-2] + ']'
		return 'OneWayList []'

	def clear(self):
		self.__init__()

# --- ZWRACA LICZBĘ PRZYPISAŃ ---
	def getAssignments(self):
		return self.assignments

# --- ZWRACA LICZBĘ PORÓWNAŃ ---
	def getEquations(self):
		return self.equations

# --- ZWRACA KONKRETNY ELEMENT LISTY ---
	def element(self, position = 1):
		self.assignments += 1
		node = self.first
		for x in range(1,position):
			self.assignments += 1
			node = node.next
		return node

# --- ZWRACA ROZMIAR LISTY ---
	def size(self):
		node = self.first
		counter = 0

		while node is not None:
			node = node.next
			counter += 1
		return counter

# --- DODAJE ELEMENT ---
	def push(self, value, position = None):
		if position == 0:
			position = 1
		if self.first == None:
			self.assignments += 2
			self.equations += 1
			self.first = Node(value, None)
			self.last = self.first

		elif self.last == self.first and position is None:
			self.assignments += 2
			self.equations += 1
			self.last = Node(value, None)
			self.first.next = self.last

		elif position == 1:
			self.assignments += 3
			self.equations += 1
			current = Node(value, None)
			current.next = self.first
			self.first = current

		elif position == None or position > self.size():
			self.assignments += 3
			self.equations += 1
			current = Node(value, None)
			self.last.next = current
			self.last = current
		else:
			self.assignments += 2
			self.equations += 1
			current = Node(value, None)
			node = self.first

			for i in range(position-2):
				self.assignments += 1
				node = node.next

			self.assignments += 2
			current.next = node.next
			node.next = current

#--- USUWA ELEMENT ---
	def pop(self, position = None):
		if position == None and self.first == self.last:
			self.assignments += 2
			self.equations += 1
			self.first = None
			self.last = None

		elif position == None or position >= self.size():
			self.assignments += 1
			self.equations += 1
			node = self.first

			while node.next.next != None:
				self.assignments += 1
				self.equations += 1
				node = node.next

			self.assignments += 1
			node.next = None
			self.last = node

		elif position == 1:
			self.assignments += 1
			self.equations += 1
			self.first = self.first.next

		else:
			self.assignments += 1
			self.equations += 1
			node = self.first

			for i in range(position-2):
				self.assignments += 1
				node = node.next

			self.assignments += 1
			node.next = node.next.next



# --- DODAWANIE ELEMETÓW PO KOLEI ---
def addOneByOne(lista = OneWayList):
	lista.assignments = 0
	lista.equations = 0
	lol = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		lista.push(lol)
		print(lol)

	print(lista)
	print("Liczba operacji porównania: " + str(lista.getEquations()))
	print("Liczba operacji przypisania: " + str(lista.getAssignments()))

# --- DODAWANIE ELEMENTÓW W LOSOWE MIEJSCA ---
def addRandom(lista = OneWayList):
	lista.assignments = 0
	lista.equations = 0
	lol = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		lista.push(lol, random.randint(0, lista.size()))
		print(lol)
	print(lista)
	print("Liczba operacji porównania: " + str(lista.getEquations()))
	print("Liczba operacji przypisania: " + str(lista.getAssignments()))

# --- DODAWANIE ELEMENTÓW PO PRZECIWNYCH STRONACH
def addOnSides(lista = OneWayList):
	lista.assignments = 0
	lista.equations = 0
	tmp = 0
	lol = 0
	for x in range(0,25):
		tmp += 1
		lol = random.randint(0, 300)

		if tmp % 2 == 1:
			lista.push(lol, 1)
		else:
			lista.push(lol)
		print(lol)

	print(lista)
	print("Liczba operacji porównania: " + str(lista.getEquations()))
	print("Liczba operacji przypisania: " + str(lista.getAssignments()))

# --- WYSZUKIWANIE WSZYSTKICH ELEMENTÓW ---
def printAllElements(lista = OneWayList):
	lista.assignments = 0
	lista.equations = 0
	for x in range(1,26):
		print()
		print(str(x) + ". " + str(lista.element(x)))
		print("Liczba operacji porównania: " + str(lista.getEquations()))
		print("Liczba operacji przypisania: " + str(lista.getAssignments()))

		lista.assignments = 0
		lista.equations = 0


# --- USUWANIE KOLEJNYCH ELEMENTÓW ---
def popElements(lista = OneWayList):
	lista.assignments = 0
	lista.equations = 0
	for x in range(1,26):
		print()
		print("usuwam element nr " + str(x))

		tmp = lista.element(x).value
		lista.assignments = 0
		lista.equations = 0
		lista.pop(x)
		print(lista)

		print("Liczba operacji porównania: " + str(lista.getEquations()))
		print("Liczba operacji przypisania: " + str(lista.getAssignments()))
		lista.push(tmp, x)

