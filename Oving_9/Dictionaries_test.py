import Dict_family as dict
import unittest

class MyTestCase(unittest.TestCase):


    def test_add_family_member(self):
        dict.add_family_member('far', 'Petter')

        #Testfunksjon
        self.assertDictEqual(dict.get_my_family(), {'far': "Petter"})

        dict.add_family_member('søster', "pamela")

        #Testfunksjon
        self.assertDictEqual(dict.get_my_family(), {'far': "Petter", 'søster': "pamela"})

    def test_add_mutlipler_members(self):
        dict.add_multiple_members('far', "Thorbjørn")
        dict.add_multiple_members('bror', ["Petter", "Andreas", "Fredrik"] )

        #Testfunksjon
        self.assertDictEqual(dict.get_my_family(), {'bror' : ["Petter", "Andreas", "Fredrik"], 'far': "Thorbjørn"})

        dict.reset_my_family()

        dict.add_multiple_members('fettere', ["Nils" , "Johan" , "Per"])
        dict.add_family_member('onkel' , "Tore")
        dict.add_multiple_members('søstre', ["Perina", "Perhutu", "Lille My"])

        #Testfunksjon
        self.assertDictEqual(dict.get_my_family(), {'fettere': ["Nils" , "Johan" , "Per"], 'onkel': "Tore" , 'søstre': ["Perina", "Perhutu", "Lille My"] })

if __name__ == '__main__':
    unittest.main()
