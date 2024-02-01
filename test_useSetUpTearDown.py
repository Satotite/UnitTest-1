import unittest

#Exemple de Classe qui permet de tester l'allocation des ressources avant le test et la liberation des ressources apres le test
class ClasseDeTest(unittest.TestCase):
#Instruction avant pour initialiser les ressources
    def test_setup(self):
        print("Avant le test")

#Execution des tests
    def test_simple(self):
        print("Réalisation de test")
        self.assertEqual(1 + 1 , 2)
#Instruction pour desengager les ressources
    def test_tearDown(self):
        print("Après le test")

if __name__ == '__main__':
    unittest.main()
