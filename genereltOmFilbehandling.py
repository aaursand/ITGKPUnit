import unittest

def write_to_file(data):
	f = open('my_file.txt','w')
	f.write(data)
	f.close()

def read_from_file(filename):
	f = open(filename,'r')
	innhold = f.read()
	f.close()	
	return innhold


class TestMethods(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestMethods, self).__init__(*args, **kwargs)
		self.my_string = "Hei jeg heter Per"
		self.file_name = "my_file.txt"
	
	def test_a_filename(self):
		test = True
		write_to_file("Testing filename")
		try:
			open(self.file_name,"r")
		except IOError as e:
			print(e.strerror)
			test = False
		self.assertTrue(test,"Bruk filnavnet: 'my_file.txt'")

	def test_a(self):
		write_to_file(self.my_string)
		f = open(self.file_name,'r')
		innhold = f.read()
		f.close()
		self.assertEqual(innhold,self.my_string)


	def test_b(self):
		write_to_file(self.my_string)
		innhold = read_from_file(self.file_name)
		self.assertEqual(innhold,self.my_string)

		

if __name__ == '__main__':
	unittest.main()