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

    def test_hyphens_and_spaces(self):
        special = Choices([
            ("en-GB", "ID"),
            ("my thing", "One"),
        ])

        self.assertEqual(special.en_GB, "en-GB")
        self.assertEqual(special.my_thing, "my thing")

        # Check that we don't allow conflicting choices
        self.assertRaises(ValueError, Choices, [("en-GB", "1"), ("en_GB", "2")])

    def test_python_keywords_and_numbers(self):
        special = Choices([
            ("id", "ID"),
            ("1", "One"),
            ("in", "IN"),
            ("xx", "XX")
        ])

        self.assertEqual(special._id, "id")
        self.assertEqual(special._1, "1")
        self.assertEqual(special._in, "in")

        # Underscore access should only work for keywords and numbers
        self.assertRaises(AttributeError, getattr, special, "_xx")

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
