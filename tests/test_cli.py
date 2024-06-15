"""
tests for the python file
"""
import os

# import custom python packages


def test_top_parser_help():
    """
    tests, if help of top parser can be called
    """

    result = os.system("python -m wahoomc -h")

    assert result == 0

def test_cli_help():
    """
    tests, if CLI help can be called
    """

    print("alf")
    result = os.system("python -m wahoomc cli -h")

    assert result == 0

def test_gui_help():
    """
    tests, if GUI help can be called
    """

    result = os.system("python -m wahoomc gui -h")

    assert result == 0
