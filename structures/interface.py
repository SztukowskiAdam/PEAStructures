class Interface(object):


	def __init__(self):
		self.container = 1
		self.method = 1

	def selectContainer(self):

		print("Witaj! wybierz strukturę, której chcesz użyć: ")
		print("1. Tablica")
		print("2. Lista jednokierujnkowa")
		print("3. Lista samoorganizująca się")
		print("4. Kolejka")
		print("5. Stos")
		print("0. Zakończ program")

		while True:
		  try:
		     self.container = int(input("Podaj swoją decyzję: "))       
		  except ValueError:
		     print("Nie podałeś numeru decyzji. Spróbuj jeszcze raz!")
		     continue
		  if self.container > 5 or self.container < 0:
		  	print("Wyszedłeś poza zakres. Spróbuj jeszcze raz!")
		  else:
		  	break


	def selectInsertMethod(self):

		print("Wybierz metodę wprowadzania danych: ")
		print("1. Po kolei")
		print("2. Wstawiając wartość raz na początek, raz na koniec")
		print("3. Wstawiając wartość w losowe miejsce")
		print("0. Zakończ program")

		while True:
		  try:
		     self.method = int(input("Podaj numer metody: "))       
		  except ValueError:
		     print("Nie podałeś numeru metody. Spróbuj jeszcze raz!")
		     continue
		  if self.method > 3 or self.method < 0:
		  	print("Wyszedłeś poza zakres. Spróbuj jeszcze raz!")
		  else:
		  	break