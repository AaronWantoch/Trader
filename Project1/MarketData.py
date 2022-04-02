import csv

class MarketData:
    def __init__(self, fileName):
        self.data = []
        self.day = []
        self.readData(fileName)

    def readData(self, fileName):
        with open(fileName, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.data.append(float(row["Open"]))
                self.day.append(row["Date"])


