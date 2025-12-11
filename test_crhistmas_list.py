from christmas_list import ChristmasList
import pytest
import os

@pytest.fixture(autouse=True)
def clear_database():
    if not os.path.exists("christmas_list.pkl"):
            with open("christmas_list.pkl", "w") as f:
                pass 
    else:
        os.system("cp empty_christmas_list.pkl christmas_list.pkl")
    yield
    if os.path.exists("christmas_list.pkl"):
        os.system("cp empty_christmas_list.pkl christmas_list.pkl")

def describe_christmas_list():

    def it_saves_an_item():
        list = ChristmasList("christmas_list.pkl")
        list.add("Fred")
        result = list.loadItems()
        assert(result == [{'name': 'Fred', 'purchased': False}])

    def it_saves_multiple_items():
        list = ChristmasList("christmas_list.pkl")
        list.add("Fred")
        list.add("Ted")
        list.add("Red")
        result = list.loadItems()
        assert(result == [{'name': 'Fred', 'purchased': False}, {'name': 'Ted', 'purchased': False}, {'name': 'Red', 'purchased': False}])

    def it_checks_off_an_item():
        list = ChristmasList("christmas_list.pkl")
        list.add("Fred")
        list.check_off("Fred")
        result = list.loadItems()
        assert(result == [{'name': 'Fred', 'purchased': True}])

    def it_deletes_an_item():
        list = ChristmasList("christmas_list.pkl")
        list.add("Fred")
        list.add("Ted")
        list.add("Red")
        first = list.loadItems()
        list.remove("Red")
        result = list.loadItems()
        assert(result != first)

    def it_prints_a_list_with_x_and_check(capsys):
        list = ChristmasList("christmas_list.pkl")
        list.add("Fred")
        list.add("Ted")
        list.check_off("Fred")
        list.print_list()
        captured = capsys.readouterr()
        assert(captured.out == "[x] Fred\n[_] Ted\n")