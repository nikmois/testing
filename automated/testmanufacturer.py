import unittest
from pcwares import *

# Домашнее задание:
# * реализовать класс ProductType (см. файл ProductTypes.csv)
#   и методы в нём
# * сделать тесты для этого класса в отдельном тестовом классе,
#   например ProductTypeTest

class ManufacturerTest(unittest.TestCase):
    def testInit(self):
        m = Manufacturer()

        self.assertIsNotNone(m.GetID())
        self.assertIsNotNone(m.GetName())
        self.assertIsNotNone(m.GetCountry())

    # Задание: Тест 2:
    # Проверить конструктор с заданными значениями
    # Проверить, чтобы данные, получаемые через Get...()
    # соответствовали ожидаемым
    def testGet(self):
        m = Manufacturer(1,"Intel","USA")
        self.assertEqual(m.GetID(),1)

    # Тест 3: Проверить Set()->Get()
    def testSet(self):
        m = Manufacturer()
        m.SetID(3)
        m.SetID(Manufacturer())
        m.SetName(6)

        self.assertEqual(m.GetID(),3)

    # Тест 4: Проверить ReadCsv()

    # Тест 5: Проверить подстановку некорректных типов в Set
    # Тест 6: То же самое с конструктором

if __name__ == '__main__':
    unittest.main()
