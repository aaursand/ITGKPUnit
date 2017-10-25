import unittest
import random
testList1 = [1,2,3,4,5,6,7,8,9,10]
testList2 = [1,22,3,4,45,6,7,2,8,9,10,11,9,3,41,8]
mulitList = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [6, 12, 18, 24, 30, 36, 42, 48, 54, 60], [7, 14, 21, 28, 35, 42, 49, 56, 63, 70], [8, 16, 24, 32, 40, 48, 56, 64, 72, 80], [9, 18, 27, 36, 45, 54, 63, 72, 81, 90], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]
multiList2 = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

def separate(numbers, treshold):
    """""
    TODO: Funksjonen tar inn en liste (numbers) og et heltall (treshold). Den skal så sortere alle tallene som er lavere enn treshold i en ny liste,
    og legge alle tall lik eller større enn treshold, inkludert treshold, hvis det eksisterer i numbers, i en annen liste, for å så returnere begge listene.
    """""
    #Skriv din kode under:


def multiplication_table(number):
    """""
    TODO: Funksjonen tar inn et heltall, og skal returnere en matrise med de n første elementene i de n første gangetabellene.
    Et tips er å lage matrisen først, før man fyller inn tallene
    """""
    #skriv din kode under:


class TestCase(unittest.TestCase):

    def test_separate(self):
        assert separate(testList1, 5) == ([1, 2, 3, 4], [5, 6, 7, 8, 9, 10]), "separate() burde returnere to lister med sorterte tall som er mindre og like stor og større enn 5"
        assert separate(testList2, 10) == ([1, 2, 3, 3, 4, 6, 7, 8, 8, 9, 9], [10, 11, 22, 41, 45]), "Skulle ha returnert to lister med tall sortert før og etter verdien 10"

    def test_multiplicationTable(self):
        assert multiplication_table(5) == multiList2 , "multiplication_table() burde ha returnert en matrise med de 5 første tallene i de 5 første gangetabellene"
        assert multiplication_table(10) == mulitList , "multiplication_table() burde ha returnert en matrise med de 10 første tallene i alle 10 gangetabellene"

if __name__ == '__main__':
    unittest.main()
