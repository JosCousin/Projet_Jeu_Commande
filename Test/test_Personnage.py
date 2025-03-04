import unittest
from unittest.mock import patch
from Personnage.Guerrier import Guerrier
from Personnage.Mage import Mage
from Personnage.Voleur import Voleur
from Personnage.personnage import choixNom

class TestClasses(unittest.TestCase):

    @patch('builtins.input', return_value='TestNom')
    def test_choix_nom_Valid(self, mock_input):
        nom = choixNom()
        self.assertTrue(len(nom) <= 10)
        self.assertTrue(len(nom) >= 3)

    @patch('builtins.input', side_effect=["T", "TestNom"])
    def test_choix_nom_Court(self, mock_input):
        nom = choixNom()
        self.assertFalse(len(nom) >= 3)

    @patch('builtins.input', side_effect=["UnNomQuiEstBeaucoupTropLong", "TestNom"])
    def test_choix_nom(self, mock_input):
        nom = choixNom()
        self.assertFalse(len(nom) <= 10)

    def test_creation_guerrier(self):
        guerrier = Guerrier("GuerrierTest")
        self.assertEqual(guerrier.nom, "GuerrierTest")
        self.assertEqual(guerrier.PV, 150)
        self.assertEqual(guerrier.PM, 50)
        self.assertEqual(guerrier.force, 15)
        self.assertEqual(guerrier.intelligence, 5)
        self.assertEqual(guerrier.defPhysique, 12)
        self.assertEqual(guerrier.defMagique, 6)
        self.assertEqual(guerrier.agilite, 8)
        self.assertEqual(guerrier.chance, 5)
        self.assertEqual(guerrier.endurance, 10)
        self.assertEqual(guerrier.esprit, 4)
        self.assertEqual(guerrier.classe, "Guerrier")

    def test_creation_mage(self):
        mage = Mage("MageTest")
        self.assertEqual(mage.nom, "MageTest")
        self.assertEqual(mage.PV, 90)
        self.assertEqual(mage.PM, 150)
        self.assertEqual(mage.force, 4)
        self.assertEqual(mage.intelligence, 15)
        self.assertEqual(mage.defPhysique, 5)
        self.assertEqual(mage.defMagique, 12)
        self.assertEqual(mage.agilite, 7)
        self.assertEqual(mage.chance, 6)
        self.assertEqual(mage.endurance, 5)
        self.assertEqual(mage.esprit, 10)
        self.assertEqual(mage.classe, "Mage")

    def test_creation_voleur(self):
        voleur = Voleur("VoleurTest")
        self.assertEqual(voleur.nom, "VoleurTest")
        self.assertEqual(voleur.PV, 110)
        self.assertEqual(voleur.PM, 70)
        self.assertEqual(voleur.force, 10)
        self.assertEqual(voleur.intelligence, 7)
        self.assertEqual(voleur.defPhysique, 8)
        self.assertEqual(voleur.defMagique, 7)
        self.assertEqual(voleur.agilite, 15)
        self.assertEqual(voleur.chance, 12)
        self.assertEqual(voleur.endurance, 7)
        self.assertEqual(voleur.esprit, 6)
        self.assertEqual(voleur.classe, "Voleur")

if __name__ == "__main__":
    unittest.main()