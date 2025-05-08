#!/usr/bin/env python

""" Scaffolding: Starter template for code written in Python. """

import os
import sys




def clear():
	os.system("cls" if os.name == "nt" else "clear")


def main(nickname):
    """
    Main entry point of the script.

    Parameters:
        nickname (str): The nickname of a person.

    Returns:
        str: A greeting message.

    Raises:
        TypeError: If any element in the list is not a number.
    """
    print("Hello, " + nickname + "!")


if __name__ == '__main__':
    sys.exit(main("Dd"))










__author__ = "Ednalyn C. De Dios, et al."
__copyright__ = "Copyright 2025, X Project"
__credits__ = ["One Fish", "Two Fish", "Blue Fish", "Red Fish"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"