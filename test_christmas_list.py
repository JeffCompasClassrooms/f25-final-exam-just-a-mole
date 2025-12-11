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
    if os.path.exists("bad.pkl"):
        os.system("rm bad.pkl")

def describe_christmas_list():
    def describe_init():
        def it_loads_an_empty_db():
            list = ChristmasList("christmas_list.pkl")
            result = list.loadItems()
            assert(result == [])

        def it_creates_a_file():
            list = ChristmasList("bad.pkl")
            result = list.loadItems()
            assert(result == [])

        def it_crashes_on_invalid_input():
            with pytest.raises(OSError):
                list = ChristmasList(67)

    def describe_save():
        def it_saves_an_item():
            list = ChristmasList("christmas_list.pkl")
            list.saveItems([{'name': 'Fred', 'purchased': False}])
            result = list.loadItems()
            assert(result == [{'name': 'Fred', 'purchased': False}])

        def it_saves_multiple_items():
            list = ChristmasList("christmas_list.pkl")
            list.saveItems([{'name': 'Fred', 'purchased': False}, {'name': 'Ted', 'purchased': False}, {'name': 'Red', 'purchased': False}])
            result = list.loadItems()
            assert(result == [{'name': 'Fred', 'purchased': False}, {'name': 'Ted', 'purchased': False}, {'name': 'Red', 'purchased': False}])
        
        def it_saves_bad_input():
            list = ChristmasList("christmas_list.pkl")
            list.saveItems("this is bad not a list!")
            result = list.loadItems()
            assert(result == "this is bad not a list!")
            # This is a bug, we probably don't want this to not return a list

    def describe_add():
        def it_adds_a_name():
            list = ChristmasList("christmas_list.pkl")
            list.add("Fred")
            result = list.loadItems()
            assert(result == [{'name': 'Fred', 'purchased': False}])

        def it_adds_multiple():
            list = ChristmasList("christmas_list.pkl")
            list.add("Fred")
            list.add("Ted")
            list.add("Red")
            result = list.loadItems()
            assert(result == [{'name': 'Fred', 'purchased': False}, {'name': 'Ted', 'purchased': False}, {'name': 'Red', 'purchased': False}])
        
        def it_adds_bad_input():
            list = ChristmasList("christmas_list.pkl")
            list.add(True)
            result = list.loadItems()
            assert(result == [{'name': True, 'purchased': False}])
            # This is a super bad one

    def describe_check_off():
        def it_checks_off_an_item():
            list = ChristmasList("christmas_list.pkl")
            list.add("Fred")
            list.check_off("Fred")
            result = list.loadItems()
            assert(result == [{'name': 'Fred', 'purchased': True}])
        
        def it_checks_off_an_already_checked_item():
            list = ChristmasList("christmas_list.pkl")
            list.add("Fred")
            list.check_off("Fred")
            list.check_off("Fred")
            result = list.loadItems()
            assert(result == [{'name': 'Fred', 'purchased': True}])
        
        def it_crashes_off_bad_input():
            with pytest.raises(TypeError):
                list = ChristmasList("christmas_list.pkl")
                list.saveItems("Test")
                list.check_off(True)
                result = list.loadItems()

    def describe_delete():
        def it_deletes_an_item():
            list = ChristmasList("christmas_list.pkl")
            list.add("Fred")
            list.add("Ted")
            list.add("Red")
            first = list.loadItems()
            list.remove("Red")
            result = list.loadItems()
            assert(result != first)
        
        def it_deletes_no_invalid_item():
            list = ChristmasList("christmas_list.pkl")
            first = list.loadItems()
            list.remove("Red")
            result = list.loadItems()
            assert(result == first)

        def it_deletes_invalid_item():
            list = ChristmasList("christmas_list.pkl")
            first = list.loadItems()
            list.add(True)
            list.remove(True)
            result = list.loadItems()
            assert(result == first)

    def describe_print():
        def it_prints_a_list_with_x_and_check(capsys):
            list = ChristmasList("christmas_list.pkl")
            list.add("Fred")
            list.add("Ted")
            list.check_off("Fred")
            list.print_list()
            captured = capsys.readouterr()
            assert(captured.out == "[x] Fred\n[_] Ted\n")
        
        def it_prints_with_bad_input(capsys):
            list = ChristmasList("christmas_list.pkl")
            list.add(True)
            list.print_list()
            captured = capsys.readouterr()
            assert(captured.out == "[_] True\n")