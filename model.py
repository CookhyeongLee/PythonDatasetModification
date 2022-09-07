import csv

# Dataset in a row


class Model:
    def __init__(self, row):
        self.products = row[0]
        self.jan20 = row[1]
        self.feb20 = row[2]
        self.mar20 = row[3]
        self.apr20 = row[4]
        self.may20 = row[5]
        self.jun20 = row[6]
        self.jul20 = row[7]
        self.aug20 = row[8]
        self.sep20 = row[9]
        self.oct20 = row[10]
        self.nov20 = row[11]
        self.dec20 = row[12]
        self.jan21 = row[13]
        self.feb21 = row[14]
        self.mar21 = row[15]
        self.apr21 = row[16]
        self.may21 = row[17]
        self.jun21 = row[18]
        self.jul21 = row[19]
        self.aug21 = row[20]
        self.sep21 = row[21]
        self.oct21 = row[22]
        self.nov21 = row[23]
        self.dec21 = row[24]
        self.jan22 = row[25]
        self.feb22 = row[26]
        self.mar22 = row[27]

    # A format of data
    def __str__(self):

        return (self.products + " | " +
                str(self.jan20) + " | " + str(self.feb20) + " | " + str(self.mar20) + " | " + str(self.apr20) + " | " + str(self.may20) + " | " + str(self.jun20) + " | " + str(self.jul20) + " | " + str(self.aug20) + " | " + str(self.sep20) + " | " + str(self.oct20) + " | " + str(self.nov20) + " | " + str(self.dec20) + " | " +
                str(self.jan21) + " | " + str(self.feb21) + " | " + str(self.mar21) + " | " + str(self.apr21) + " | " + str(self.may21) + " | " + str(self.jun21) + " | " + str(self.jul21) + " | " + str(self.aug21) + " | " + str(self.sep21) + " | " + str(self.oct21) + " | " + str(self.nov21) + " | " + str(self.dec21) + " | " +
                str(self.jan22) + " | " + str(self.feb22) + " | " + str(self.mar22) + " |")
