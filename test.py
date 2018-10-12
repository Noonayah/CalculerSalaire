#Importation du module unittest et du fichier calculSalaire pour pouvoir utiliser la fonction:
import unittest
from calculSalaire import *

#classe des tests de la fonction :

class testVerif(unittest.TestCase):

    def test_calculSalaire_architecte(self):
        self.assertEqual(calculSalaire('architecte', 4), '4000 euros')

    def test_calculSalaire_consultant(self):
         self.assertEqual(calculSalaire('consultant',5),'5000 euros')

    def test_calculSalaire_medecin(self):
         self.assertEqual(calculSalaire('médecin',8),'7000 euros')

if __name__=='__main__':
    unittest.main()