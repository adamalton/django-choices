from collections import OrderedDict
import keyword

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
            if name.startswith("_") and name[1:] in self._choices:
                without_underscore = name[1:]

                # Check if the name is a Python keyword, builtin or an integer
                # if it is, we allow access with a leading underscore, but if not
                # we fall through and throw the normal KeyError
                special = False
                try:
                    int(without_underscore)
                    special = True
                except (TypeError, ValueError):
                    special = without_underscore in keyword.kwlist or \
                              without_underscore in __builtins__.keys()

                if special:
                    return without_underscore

            if name not in self._choices:
                # Another special case, if we have spaces or hyphens, provide
                # access using underscores in place
                for k in self._choices:
                    if k.replace("-", "_").replace(" ", "_") == name:
                        return k

            self._choices[name] #check it exists
            return name
        except KeyError:
            raise AttributeError("Choices object has no such attribute {}".format(name))

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
