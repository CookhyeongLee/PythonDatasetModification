"""
This Programme created by Cookhyeong Lee
Course Number: CST8333_305
Student Number: 041021980
"""
from controller import saveCSV
from model import Model
from controller import readCSV


class View:

    def __init__(self, controller):
        self.controller = controller


list = []
# While True to get the CSV data It ends when it's false for selection 6 which is "EXit"
while True:
    # If statement in while loop start with 0 to 76 instead 1 to 77
    if len(list) == 0:
        list = readCSV()
    # To get the counter in row from 1
    counter = 1
    for product in list:
        print(counter)
        print(product)
        print('\n')
        # increment operator from 1 to 77 by rows
        counter += 1
    # User input to get selections
    selection = input(
        "Please enter an option:\n(1) Edit record\n(2) Delete record\n(3) Insert record\n(4) Reset records\n(5) Save record\n(6) Exit\nProgramme by Cookhyeong Lee\n: ")

    # if else statement 1 for edit table made a list for each rows that can edit table product name and prices and it converts to integer
    if selection == "1":
        selectedproduct = input('What product number would you like to edit: ')
        print(list[int(selectedproduct)])
        productname = input('Enter product name: ')
        list[int(selectedproduct)].products = productname
        productpricejan20 = input('Enter price jan20: ')
        list[int(selectedproduct)].jan20 = productpricejan20
        productpricefeb20 = input('Enter price feb20: ')
        list[int(selectedproduct)].feb20 = productpricefeb20
        productpricemar20 = input('Enter price mar20: ')
        list[int(selectedproduct)].mar20 = productpricemar20
        productpriceapr20 = input('Enter price apr20: ')
        list[int(selectedproduct)].apr20 = productpriceapr20
        productpricemay20 = input('Enter price may20: ')
        list[int(selectedproduct)].may20 = productpricemay20
        productpricejun20 = input('Enter price jun20: ')
        list[int(selectedproduct)].jun20 = productpricejun20
        productpricejul20 = input('Enter price jul20: ')
        list[int(selectedproduct)].jul20 = productpricejul20
        productpriceaug20 = input('Enter price aug20: ')
        list[int(selectedproduct)].aug20 = productpriceaug20
        productpricesep20 = input('Enter price sep20: ')
        list[int(selectedproduct)].sep20 = productpricesep20
        productpriceoct20 = input('Enter price oct20: ')
        list[int(selectedproduct)].oct20 = productpriceoct20
        productpricenov20 = input('Enter price nov20: ')
        list[int(selectedproduct)].nov20 = productpricenov20
        productpricedec20 = input('Enter price dec20: ')
        list[int(selectedproduct)].dec20 = productpricedec20
        productpricejan21 = input('Enter price jan21: ')
        list[int(selectedproduct)].jan21 = productpricejan21
        productpricefeb21 = input('Enter price feb21: ')
        list[int(selectedproduct)].feb21 = productpricefeb21
        productpricemar21 = input('Enter price mar20: ')
        list[int(selectedproduct)].mar21 = productpricemar21
        productpriceapr21 = input('Enter price apr21: ')
        list[int(selectedproduct)].apr21 = productpriceapr21
        productpricemay21 = input('Enter price may21: ')
        list[int(selectedproduct)].may21 = productpricemay21
        productpricejun21 = input('Enter price jun21: ')
        list[int(selectedproduct)].jun21 = productpricejun21
        productpricejul21 = input('Enter price jul20: ')
        list[int(selectedproduct)].jul21 = productpricejul21
        productpriceaug21 = input('Enter price aug21: ')
        list[int(selectedproduct)].aug21 = productpriceaug21
        productpricesep21 = input('Enter price sep21: ')
        list[int(selectedproduct)].sep21 = productpricesep21
        productpriceoct21 = input('Enter price oct21: ')
        list[int(selectedproduct)].oct21 = productpriceoct21
        productpricenov21 = input('Enter price nov21: ')
        list[int(selectedproduct)].nov21 = productpricenov21
        productpricedec21 = input('Enter price dec21: ')
        list[int(selectedproduct)].dec21 = productpricedec21
        productpricejan22 = input('Enter price jan22: ')
        list[int(selectedproduct)].jan22 = productpricejan22
        productpricefeb22 = input('Enter price feb22: ')
        list[int(selectedproduct)].feb22 = productpricefeb22
        productpricemar22 = input('Enter price mar22: ')
        list[int(selectedproduct)].mar22 = productpricemar22
        print('Programme by Cookhyeong Lee')
    # Second condition for delete a table from the list by number of rows
    elif selection == "2":
        selectedproduct = input(
            'What product number would you like to delete: ')
        del list[int(selectedproduct)]
        print('Programme by Cookhyeong Lee')
    # Third condition for insert a new table with product name and date
    elif selection == "3":
        productname = input('Enter product name: ')
        productpricejan20 = input('Enter price jan20: ')
        productpricefeb20 = input('Enter price feb20: ')
        productpricemar20 = input('Enter price mar20: ')
        productpriceapr20 = input('Enter price apr20: ')
        productpricemay20 = input('Enter price may20: ')
        productpricejun20 = input('Enter price jun20: ')
        productpricejul20 = input('Enter price jul20: ')
        productpriceaug20 = input('Enter price aug20: ')
        productpricesep20 = input('Enter price sep20: ')
        productpriceoct20 = input('Enter price oct20: ')
        productpricenov20 = input('Enter price nov20: ')
        productpricedec20 = input('Enter price dec20: ')
        productpricejan21 = input('Enter price jan21: ')
        productpricefeb21 = input('Enter price feb21: ')
        productpricemar21 = input('Enter price mar20: ')
        productpriceapr21 = input('Enter price apr21: ')
        productpricemay21 = input('Enter price may21: ')
        productpricejun21 = input('Enter price jun21: ')
        productpricejul21 = input('Enter price jul20: ')
        productpriceaug21 = input('Enter price aug21: ')
        productpricesep21 = input('Enter price sep21: ')
        productpriceoct21 = input('Enter price oct21: ')
        productpricenov21 = input('Enter price nov21: ')
        productpricedec21 = input('Enter price dec21: ')
        productpricejan22 = input('Enter price jan22: ')
        productpricefeb22 = input('Enter price feb22: ')
        productpricemar22 = input('Enter price mar22: ')

        # It has a attribute and list by each product and it's into new product list
        productattributes = [productname, productpricejan20, productpricefeb20, productpricemar20, productpriceapr20, productpricemay20, productpricejun20, productpricejul20, productpriceaug20, productpricesep20, productpriceoct20, productpricenov20, productpricedec20,
                             productpricejan21, productpricefeb21, productpricemar21, productpriceapr21, productpricemay21, productpricejun21, productpricejul21, productpriceaug21, productpricesep21, productpriceoct21, productpricenov21, productpricedec21,
                             productpricejan22, productpricefeb22, productpricemar22]
        newproduct = Model(productattributes)
        list.append(newproduct)
        print('Programme by Cookhyeong Lee')
    # Fourth condition to reset the table has been changed by either deleting or editing table
    elif selection == "4":
        list = readCSV()
    # Fifth condition to change the path and it has its own loop for the data saves into the new file that I create
    elif selection == "5":
        saveproduct = input('What folder would you like to change: ')
        fileproduct = input('What file would you like to change : ')
        fullpath = saveproduct + '/' + fileproduct
        record = []
        recordcounter = 0
        for product in list:
            record.append([list[recordcounter].products, list[recordcounter].jan20, list[recordcounter].feb20, list[recordcounter].mar20, list[recordcounter].apr20, list[recordcounter].may20, list[recordcounter].jun20, list[recordcounter].jul20, list[recordcounter].aug20, list[recordcounter].sep20, list[recordcounter].oct20, list[recordcounter].nov20, list[recordcounter].dec20, list[recordcounter].jan21,
                          list[recordcounter].feb21, list[recordcounter].mar21, list[recordcounter].apr21, list[recordcounter].may21, list[recordcounter].jun21, list[recordcounter].jul21, list[recordcounter].aug21, list[recordcounter].sep21, list[recordcounter].oct21, list[recordcounter].nov21, list[recordcounter].dec21, list[recordcounter].jan22, list[recordcounter].feb22, list[recordcounter].mar22])
            recordcounter += 1
        # A new save object and parameters from Controller class
        saveCSV(fullpath, record)
    # Last condition to exit the Programme with a print
    elif selection == "6":
        print('Programme Designed By Cookhyeong Lee!')
        break
