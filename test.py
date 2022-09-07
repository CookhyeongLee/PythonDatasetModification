from ast import Assert
import pytest
from controller import readCSV

# Pytest to test if the row number is equal to 77


def test():
    list = readCSV()
    assert len(list) == 77


print("Programmed by Cookhyeong Lee")
