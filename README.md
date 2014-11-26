django-choices
==============

A handy class for creating "choices" objects, primarily for use in Django


# Usage

Essentially you just wrap a normal iterable of (value, label) pairs in the `Choices` class.

```
my_choices = Choices([
    ('BLUE', 'Blue'),
    ('BANANA', 'Banana'),
    ('THING', 'Some Thing'),
])

```

You then have access to:

* `my_choices.choices` - this gives an iterable of pairs, as you would pass to a Django model field.
* `my_choices.constants` - this gives an iterable of the *values* only.
* `my_choices.THING` - this is a reference to this particular choice, useful for defining things by reference rather than hard coding the same string literal in multiple places.


## Example

```
from choices import Choices

MY_CHOICES = Choices([
    ('YES', 'Yes'),
    ('NO', 'No'),
    ('MAYBE', 'Maybe')
])

class MyModel(models.Model):

    decision = models.CharField(
        choices=MY_CHOICES.choices,
        default=MY_CHOICES.YES
    )
```
