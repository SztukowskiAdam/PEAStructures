import random
from structures.one_way_list_class import *


class SelfOrganizedList(OneWayList):


# --- ZWRACA WARTOŚĆ KONKRETNEGO ELEMENTU LISTY ---
	def elementValue(self, position = 1):
		node = self.first

		if position == 1:
			return node.value
		elif position == self.size():
			return self.last.value
		else:
			for i in range(position-1):
				self.assignments += 1
				node = node.next
			return node.value

# --- ZWRACA KONKRETNY ELEMENT LISTY
	def element(self, position = 1):
		self.assignments += 1
		
		node = self.first

		if position == 1:
			return node
		else:
			for i in range(position-1):
				self.assignments += 1
				node = node.next

			self.push(node.value, 1)
			self.pop(position+1)

			return node

# --- DODAWANIE ELEMETÓW PO KOLEI ---
def addOneByOne(lista = SelfOrganizedList):
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
def addRandom(lista = SelfOrganizedList):
	lista.assignments = 0
	lista.equations = 0
	lol = 0
	for x in range(0,25):
		lol = random.randint(0, 300)
		lista.push(lol, random.randint(0, x))
		print(lol)
	print(lista)
	print("Liczba operacji porównania: " + str(lista.getEquations()))
	print("Liczba operacji przypisania: " + str(lista.getAssignments()))

# --- DODAWANIE ELEMENTÓW PO PRZECIWNYCH STRONACH
def addOnSides(lista = SelfOrganizedList):
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
def printAllElements(lista = SelfOrganizedList):
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
def popElements(lista = SelfOrganizedList):
	lista.assignments = 0
	lista.equations = 0
	for x in range(1,26):
		print()
		print("usuwam element nr: " + str(x))

		tmp = lista.elementValue(x)
		lista.assignments = 0
		lista.equations = 0
		lista.pop(x)
		print(lista)

		print("Liczba operacji porównania: " + str(lista.getEquations()))
		print("Liczba operacji przypisania: " + str(lista.getAssignments()))
		lista.push(tmp, x)
