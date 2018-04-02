import structures.interface as interface

# --- INTERFEJS ---
interface = interface.Interface()
interface.selectContainer()
if interface.container == 0:
	quit()
interface.selectInsertMethod()


# --- WYBÓR STRUKTURY ---

def zero():
	quit()

def tab():
	global container
	global structure
	import structures.table_class as container
	structure = container.Table()

def oneWayList():
	global container
	global structure
	import structures.one_way_list_class as container
	structure = container.OneWayList()

def selfOrganizedList():
	global container
	global structure
	import structures.self_organized_list_class as container
	structure = container.SelfOrganizedList()

def queue():
	global container
	global structure
	import structures.queue_class as container
	structure = container.Queue()

def stack():
	global container
	global structure
	import structures.stack_class as container
	structure = container.Stack()


options = {0 : zero,
           1 : tab,
           2 : oneWayList,
           3 : selfOrganizedList,
           4 : queue,
           5 : stack,
}

options[interface.container]()



#--- OPERACJE NA STRUKTURZE ---
print(" ")
print("-------------------")
print("DODAWANIE ELEMENTÓW")
print("-------------------")

if interface.method == 1:
	container.addOneByOne(structure)
elif interface.method == 2:
	container.addOnSides(structure)
elif interface.method == 3:
	container.addRandom(structure)
else:
	quit()

print(" ")
print("----------------------")
print("WYSZUKIWANIE ELEMENTÓW")
print("----------------------")
print(" ")
container.printAllElements(structure)

print(" ")
print("------------------")
print("USUWANIE ELEMENTÓW")
print("------------------")
print(" ")
container.popElements(structure)


