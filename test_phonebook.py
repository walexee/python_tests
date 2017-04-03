# python -m unittest
import unittest

from unittest.mock import Mock
from logger import Logger
from phonebook import Phonebook 

class PhonebookTest(unittest.TestCase):

	def setUp(self):
		logger = Mock(Logger)
		self.phonebook = Phonebook(logger)

	# def tearDown(self):
	# 	pass

	def test_create_phonebook(self):
		phonebook = Phonebook()

	def test_lookup_entry_by_name(self):
		self.phonebook.add("Bob", "12345")
		self.assertEqual("12345", self.phonebook.lookup("Bob"))

	def test_miising_entry_raises_KeyError(self):
		with self.assertRaises(KeyError):
			self.phonebook.lookup("missing")

	def test_empty_phonebook_is_consistent(self):
		self.assertTrue(self.phonebook.is_consistent())

	def test_phonebook_gives_access_to_names(self):
		self.phonebook.add("Alice", "123")
		self.assertIn("Alice", self.phonebook.names())

	def test_phonebook_gives_access_to_numbers(self):
		self.phonebook.add("Alice", "123")
		self.assertIn("123", self.phonebook.numbers())
