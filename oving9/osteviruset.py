import unittest

cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

infected_cheeses_list = ['B13','B14','B15','A234','A235','C31']

def port_salut_hylleplasser():
	return cheeses['port salut']

def infected_cheeses():#b
	potentially_infected_cheeses = []
	for key in cheeses.keys():
		for value in cheeses.get(key):
			splitted = value.split('-')
			if(splitted[0] in infected_cheeses_list):
				if(key not in potentially_infected_cheeses):
					potentially_infected_cheeses.append(key)
	return potentially_infected_cheeses

def ostetype_ikke_smittet():
	list_to_return = []
	infected_cheeses_list = infected_cheeses()
	for key in cheeses.keys():
		if(key not in infected_cheeses_list):
			for value in cheeses.get(key):
				list_to_return.append((value,key))

	return list_to_return



class TestMethods(unittest.TestCase):

	def test_a_type(self):
		student_answer = port_salut_hylleplasser()
		self.assertEqual(type(student_answer), type(('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4')), "Funksjonen skal returnere en tuple")

	def test_a(self):
		student_answer = port_salut_hylleplasser()
		self.assertEqual(student_answer, ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'))

	def test_b_type(self):
		student_answer = infected_cheeses()
		self.assertEqual(type(student_answer), type(['mozarella', 'camembert', 'cheddar', 'port salut']), "Funksjonen skal returnere en vanlig liste med oster")

	def test_b(self):
		student_answer = infected_cheeses()
		self.assertEqual(sorted(student_answer), sorted(['mozarella', 'camembert', 'cheddar', 'port salut']))


	def test_c_type(self):
		student_answer = ostetype_ikke_smittet()
		self.assertEqual(type(student_answer), 
		type([('GOMBOS-4', 'ridder'),
		('B16-3', 'ridder'), 
		('ZLAFS55-4', 'gombost'), 
		('ZLAFS55-9', 'gombost'), 
		('GOMBOS-7', 'gombost'), 
		('A236-4', 'gombost'), 
		('SPAZ-1', 'geitost'), 
		('SPAZ-3', 'geitost'), 
		('EMACS45-0', 'geitost')]), "Funksjonen skal returnere en liste med alle tuplene")

	def test_c(self):
		student_answer = ostetype_ikke_smittet()
		self.assertEqual(student_answer, 
		[('GOMBOS-4', 'ridder'),
		('B16-3', 'ridder'), 
		('ZLAFS55-4', 'gombost'), 
		('ZLAFS55-9', 'gombost'), 
		('GOMBOS-7', 'gombost'), 
		('A236-4', 'gombost'), 
		('SPAZ-1', 'geitost'), 
		('SPAZ-3', 'geitost'), 
		('EMACS45-0', 'geitost')])

if __name__ == '__main__':
	unittest.main()