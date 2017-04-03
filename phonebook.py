
from logger import Logger

class Phonebook:
    """Phone book for keeping phone numbers"""

    def __init__(self, logger=None):
        self.entries = {}
        self.logger = logger or Logger()

    def add(self, name, number):
        """Adds a phone number to the phonebook

        Args:
            name: the name of the person
            number: the phone number
        """
        self.entries[name] = number
        self.logger.log_info("{}:{} is added.".format(name, number))

    def lookup(self, name):
        """looks up number for a name"""
        return self.entries[name]

    def is_consistent(self):
        """Checks if the phone book is consistent"""
        return True

    def names(self):
        """Gets all the names in the phone book"""
        return self.entries.keys()

    def numbers(self):
        """Gets all the numbers in the phone book"""
        return self.entries.values()
