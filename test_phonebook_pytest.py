# python -m pytest # It will also run the unittests
# doctest: python -m python --doctest-modules
import pytest

from phonebook import Phonebook 

@pytest.fixture
def phonebook():
    return Phonebook()

def test_add_and_lookup_entry(phonebook):
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")

def test_phonebook_gives_access_to_names(phonebook):
    phonebook.add("Alice", "123")
    assert "Alice" in phonebook.names()

def test_phonebook_gives_access_to_numbers(phonebook):
    phonebook.add("Alice", "123")
    assert "123" in phonebook.numbers()

def test_miising_entry_raises_KeyError(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")
