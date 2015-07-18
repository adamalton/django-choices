from collections import OrderedDict


#TODO: can we just sub-class tuple and be a tuple of tuples with attributes?
class Choices(object):
    """ An enum-type class for creating immutable choices for django CharFields.
        Usage:
        MY_CHOICES = Choices([('YES', 'Yes'), ('NO', 'No'), ('MAYBE', 'Maybe')])
        CharField(choices=MY_CHOICES.choices, default=MY_CHOICES.YES)
        """

    def __init__(self, choices):
        super(Choices, self).__setattr__('_choices', OrderedDict(choices))
        assert 'choices' not in self._choices.keys()
        assert 'constants' not in self._choices.keys()

    def __getattr__(self, name):
        try:
            self._choices[name] #check it exists
            return name
        except KeyError:
            return super(Choices, self).__getattr__(name)

    def __setattr__(self, name, value):
        """ Prevent values being changed. """
        raise AttributeError("You cannot modify attributes on a %s" % self.__class__.__name__)

    def __iter__(self):
        return iter(self.constants)

    def __repr__(self):
        return unicode(self.choices)

    @property
    def constants(self):
        return self._choices.keys() #TODO: can we make this faster by storing a constant reference?

    @property
    def choices(self):
        return self._choices.items() #TODO: can we make this faster by storing a constant reference?
