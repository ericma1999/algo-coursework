import csv
import math
from AbstractClass import AbstractLondonRailwayMapper
from implementation.Edge import Edge
from implementation.Graph import Graph

class StationInfo:

    def __init__(self, station_id, lat, lng):
        self.station_id = station_id
        self.lat = float(lat)
        self.lng = float(lng)

    def __str__(self):
        return f"station_id: {self.station_id}, latitude: {self.lat}, longitude: {self.lng}"

class LondonRailwayMapper(AbstractLondonRailwayMapper):
    
    stations = {}
    stationNames = []

    def __init__(self):
        # ADD YOUR CODE HERE
        self.loadStationsAndLines()
            
     
    
        
    def loadStationsAndLines(self):
        # ADD YOUR CODE HERE
        with open('londonstations.csv') as file:
            reader = csv.reader(file, delimiter='\n')
            first = True
            id_counter = 0
            for row in reader:
                if first:
                    first = False
                    continue
                rowContent = row[0].split(',')
                self.stations[rowContent[0]] = StationInfo(id_counter, rowContent[1], rowContent[2])
                self.stationNames.append(rowContent[0])
                id_counter+=1

            self.graph = Graph(id_counter + 1)


        with open('londonrailwaylines.csv') as file:
            reader = csv.reader(file, delimiter='\n')
            first = True

            for row in reader:
                if first:
                    first = False
                    continue
                rowContent = row[0].split(',')
                fromStation = self.stations[rowContent[1]]
                toStation = self.stations[rowContent[2]]

                self.graph.addEdge(Edge(fromStation.station_id, toStation.station_id, math.dist([fromStation.lat, fromStation.lng], [toStation.lat, toStation.lng])))
    
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