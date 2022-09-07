from tkinter import W
from model import Model
import csv


class Controller:
    def __init__(self):
        self.model = Model()

# Open and read CSV file and its output shows in view


def readCSV():
    try:
        rows = []
        with open('Monthly average retail prices.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            index = 0
            for row in spamreader:
                if index == 0:
                    index = index + 1
                    continue
                index = index + 1
                dataSet = Model(row)
                rows.append(dataSet)
            return rows
    except:
        print("Something's wrong!")

# Define for save the data into a file in assignment2 as a CSV file


def saveCSV(filename, list):
    try:
        with open(filename + ".CSV", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(list)
    except:
        print("Something's wrong!")
