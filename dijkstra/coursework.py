import csv
import math
from AbstractClass import AbstractLondonRailwayMapper
from implementation.Edge import Edge
from implementation.Graph import Graph
from implementation.BFS import BFS

class StationInfo:

    def __init__(self, station_id, lat, lng):
        self.station_id = station_id
        self.lat = float(lat)
        self.lng = float(lng)

    def __str__(self):
        return f"station_id: {self.station_id}, latitude: {self.lat}, longitude: {self.lng}"

class LondonRailwayMapper(AbstractLondonRailwayMapper):
    
    stations = {}
    # auxiliary array to reverse map index to name of station
    stationNames = []

    def __init__(self):
        # ADD YOUR CODE HERE
        self.loadStationsAndLines()
            
     
    def __loadStations(self):
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

    def __loadLines(self):
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
    
    
    def loadStationsAndLines(self):
        # ADD YOUR CODE HERE
        self.__loadStations()
        self.__loadLines()
    
    

    def minStops(self, fromS, toS):     
        numStops = -1
        # ADD YOUR CODE HERE

        result = BFS(self.graph, fromS)
        numStops = result.lengthTo(toS)
        print(result.pathTo(toS))

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

print(test.minStops(0, 1))

print(test.stationNames[0])
print(test.stationNames[614])
print(test.stationNames[94])
print(test.stationNames[467])
print(test.stationNames[150])
print(test.stationNames[649])
print(test.stationNames[1])