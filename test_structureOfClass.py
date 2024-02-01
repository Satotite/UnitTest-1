import unittest
import sys

# Exemple d’une classe de test avec des tests ignorés
class ClasseDeTest(unittest.TestCase):

    @unittest.skip("démonstration du skipping")
    def test_nothing(self):
        self.fail("Ce test ne devrait pas être exécuté.")

    def test_simple(self):
        self.assertTrue(True)

    @unittest.skipIf(sys.version_info < (3, 0), "Requiert Python 3 ou supérieur")
    def test_python_version(self):
        # Ce test vérifie quelque chose qui n'est pertinent que pour Python 3 ou supérieur.
        self.assertTrue(True)

    @unittest.skipUnless(sys.platform.startswith("win"), "Requiert Windows")
    def test_windows_only(self):
        # Ce test ne s'exécute que sous Windows.
        self.assertTrue(True)

# Pour exécuter une classe de test, il faut utiliser la fonction unittest.main()
if __name__ == '__main__':
    unittest.main(verbosity=2)
