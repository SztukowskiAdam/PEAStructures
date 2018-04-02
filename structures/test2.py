import random

class Node(object):
	"""docstring for Node"""
	def __init__(self, data = None):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)


class OneWayList(object):
	"""docstring for OneWayList"""
	def __init__(self):
		self.head = None
		self.tail = None
		self.nodes = []
		self.assignments = 0
		self.equations = 0

# --- ZWRACA ROZMIAR LISTY ---
	def size(self):
		return len(self.nodes)

# --- ZWRACA KONKRETNY ELEMENT LISTY ---
	def element(self, position = 1):
		self.assignments += 1
		node = self.head
		for x in range(1,position):
			self.assignments += 1
			node = node.next
		return node

# --- ZWRACA LICZBĘ PRZYPISAŃ ---
	def getAssignments(self):
		return self.assignments

# --- ZWRACA LICZBĘ PORÓWNAŃ ---
	def getEquations(self):
		return self.equations

# --- WYŚWIETLA LISTĘ ---
	def showList(self):
		node = self.head
		while node:
			print(node)
			node = node.next

# --- DODAJE ELEMENT DO LISTY ---
	def append(self, node, position = None):

		if self.head is None and self.tail is None:
			self.equations += 1
			self.assignments += 2
			self.head = node
			node.next = self.tail
			self.nodes.append(node)

		elif (position is None) or (position == 1) or (OneWayList.size(self) <= 1):
			self.equations += 1
			self.assignments += 2
			node.next = self.head
			self.head = node
			self.nodes.insert(0, node)

		else:
			self.equations += 1
			self.assignments += 2
			self.assignments += position
			node.next = self.nodes[position-2].next
			self.nodes[position-2].next = node
			self.nodes.insert(position-1, node)

# --- USUWA ELEMENT Z LISTY ---
	def pop(self, position = None):

		if (position is None) or (position == 1):
			self.equations += 1
			self.assignments += 1
			self.head = self.nodes[0].next
			self.nodes.pop(0)

		elif position == OneWayList.size(self):
			self.equations += 1
			self.assignments += position
			self.nodes[OneWayList.size(self)-2].next = self.tail
			self.nodes.pop(OneWayList.size(self)-1)

		else: 
			self.equations += 1
			self.assignments += position
			self.assignments += 1
			self.nodes[position-2].next = self.nodes[position]
			self.nodes.pop(position-1)

# === KONIEC KLASY ===



# --- DODAWANIE ELEMETÓW PO KOLEI ---
def addOneByOne(lista = OneWayList):
	lista.assignments = 0
	lista.equations = 0
	for x in range(0,25):
		lista.append(Node(random.randint(0, 300)))

	lista.showList()
	print("Liczba operacji porównania: " + str(lista.getEquations()))
	print("Liczba operacji przypisania: " + str(lista.getAssignments()))

# --- DODAWANIE ELEMENTÓW W LOSOWE MIEJSCA ---
def addRandom(lista = OneWayList):
	lista.assignments = 0
	lista.equations = 0
	for x in range(0,25):
		lista.append(Node(random.randint(0, 300)), random.randint(0, lista.size()))
	lista.showList()
	print("Liczba operacji porównania: " + str(lista.getEquations()))
	print("Liczba operacji przypisania: " + str(lista.getAssignments()))

# --- DODAWANIE ELEMENTÓW PO PRZECIWNYCH STRONACH
def addOnSides(lista = OneWayList):
	lista.assignments = 0
	lista.equations = 0
	tmp = 0
	for x in range(0,25):
		tmp += 1

		if tmp % 2 == 1:
			lista.append(Node(random.randint(0, 300)), lista.size()+1)
		else:
			lista.append(Node(random.randint(0, 300)))

	lista.showList()
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
		print("usuwam element: " + str(lista.element(x)))

		tmp = lista.element(x)
		lista.assignments = 0
		lista.equations = 0
		lista.pop(x)
		lista.showList()

		print("Liczba operacji porównania: " + str(lista.getEquations()))
		print("Liczba operacji przypisania: " + str(lista.getAssignments()))
		lista.append(tmp, x)

