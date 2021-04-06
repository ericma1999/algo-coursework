import csv
from AbstractClass import AbstractLondonRailwayMapper

class Location:

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return f"latitude: {self.lat}, longitude: {self.lng}"

class LondonRailwayMapper(AbstractLondonRailwayMapper):
    
    stations = {}

    def __init__(self):
        # ADD YOUR CODE HERE
        self.loadStationsAndLines()

        pass           
     
    
        
    def loadStationsAndLines(self):
        # ADD YOUR CODE HERE
        with open('londonstations.csv') as file:
            reader = csv.reader(file, delimiter='\n')
            first = True
            for row in reader:
                if first:
                    first = False
                    continue
                rowContent = row[0].split(',')
                self.stations[rowContent[0]] = Location(rowContent[1], rowContent[2])
    
        pass
    
    

    def minStops(self, fromS, toS):     
        numStops = -1
        # ADD YOUR CODE HERE

        
        return numStops    
    
    
    
    def minDistance(self, fromS, toS):
        minDistance = -1.0
        # ADD YOUR CODE HERE

        
        return minDistance
    
    
    
    
    def newRailwayLine(self, inputList):
        outputList = []
        # ADD YOUR CODE HERE

        
        return outputList


test = LondonRailwayMapper()