import unittest

from choices import Choices


colours = Choices([
    ('red', 'strawberry'),
    ('white', 'vanilla'),
    ('black', 'chocolate'),
])


class ChoicesTestCase(unittest.TestCase):
    def test_create_choices(self):
        self.assertEqual(colours.red, 'red')
        self.assertEqual(colours.white, 'white')
        self.assertEqual(colours.black, 'black')

    def test_choices_property(self):
        self.assertEqual(
            tuple(colours.choices),
            (
                ('red', 'strawberry'),
                ('white', 'vanilla'),
                ('black', 'chocolate'),
            ),
        )

    def test_constants_property(self):
        self.assertEqual(
            tuple(colours.constants),
            ('red', 'white', 'black'),
        )

    def test_cannot_set_attribute_value(self):
        with self.assertRaises(AttributeError):
            colours.red = 'blueberry'

    def test_cannot_assign_new_attribute(self):
        with self.assertRaises(AttributeError):
            colours.yellow = 'banana'

    def test_is_iterable(self):
        self.assertEqual(
            tuple(colours),
            ('red', 'white', 'black'),
        )

    def test_cannot_use_class_names(self):
        for name in ('constants', 'choices'):
            with self.assertRaises(AssertionError):
                Choices([
                    (name, name),
                ])


if __name__ == '__main__':
    unittest.main()
