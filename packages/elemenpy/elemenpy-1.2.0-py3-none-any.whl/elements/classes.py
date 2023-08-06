"""Element class for elemenpy."""
from elements import lists

class Element:

    """
    Element class
    Instance variables: name, symbol, number, mass, group, period
    Methods: get_name, get_symbol, get_number, get_mass, get_group, get_period
    """
    def __init__(self, name, symbol, number, mass, group, period):
        """
        Constructor for Element class.

        Parameters: name (str), symbol (str), number (int), mass (float), group (char), period (int) (in that order)
        """
        self.name = name
        self.symbol = symbol
        self.number = number
        self.mass = mass
        self.group = group
        self.period = period

    def get_name(self):
        """
        Returns element name
        """
        return self.name

    def get_symbol(self):
        """
        Returns element symbol
        """
        return self.symbol

    def get_number(self):
        """
        Returns element number
        """
        return self.number

    def get_mass(self):
        """
        Returns element mass
        """
        return self.mass

    def get_group(self):
        """
        Returns element group
        """
        return self.group

    def get_period(self):
        """
        Returns element period
        """
        return self.period

elements_dict = {
    # Python requires declaration of a dict before
    # possible usage
    1: Element('Hydrogen', 'H', 1, 1.00794, "1", 1),
}

for i in range(2, 119):
    elements_dict[i] = Element(
        lists.names[i - 2],
        lists.symbols[i - 2],
        lists.numbers[i - 2],
        lists.masses[i - 2],
        lists.groups[i - 2],
        lists.periods[i - 2]
        )
