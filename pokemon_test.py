import unittest
from reques import get_pokemon_info

class MyTestCase(unittest.TestCase):
    def test_something(self):
        with self.assertRaises(BaseException) as e:
            get_pokemon_info('24352516')
        self.assertEquals("Ошибка сервера", e.exception.args[0])
    def test(self):
       self.assertEquals(get_pokemon_info('200'),('misdreavus', ['levitate'])

if __name__ == '__main__':
    unittest.main()
