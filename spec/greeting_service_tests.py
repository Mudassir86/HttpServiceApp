import unittest
from src.greeting_service import GreetingService


class HelloServiceTestCase(unittest.TestCase):
    def test_say_hello_no_input(self):
        sut = GreetingService()
        result = sut.say_hello(None)
        expected = 'Hello Stranger'

        self.assertEqual(result, expected)

    def test_say_hello_with_input(self):
        sut = GreetingService()
        result = sut.say_hello('AlfredMesselWeg')
        expected = 'Hello Alfred Messel Weg'

        self.assertEqual(result, expected)

    def test_say_hello_with_input_all_caps(self):
        sut = GreetingService()
        result = sut.say_hello('ALFREDMESSELWEG')
        expected = 'Hello ALFREDMESSELWEG'

        self.assertEqual(result, expected)

    def test_say_hello_with_input_all_small(self):
        sut = GreetingService()
        result = sut.say_hello('alfredmesselweg')
        expected = 'Hello alfredmesselweg'

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
