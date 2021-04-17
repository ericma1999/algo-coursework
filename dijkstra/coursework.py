import csv
from AbstractClass import AbstractLondonRailwayMapper
from implementation.Edge import Edge
from implementation.Graph import Graph
from implementation.BFS import BFS
from implementation.Dijkstra import DijkstraSP
from implementation.Harvenstein import harvensineDistance,euclidean_distance

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

                self.graph.addEdge(Edge(fromStation.station_id, toStation.station_id, harvensineDistance(fromStation.lat,fromStation.lng, toStation.lat, toStation.lng)))
    
    
    def loadStationsAndLines(self):
        # ADD YOUR CODE HERE
        self.__loadStations()
        self.__loadLines()
    
    

    def minStops(self, fromS, toS):     
        numStops = -1
        # ADD YOUR CODE HERE
        result = BFS(self.graph, self.stations[fromS].station_id)
        numStops = result.lengthTo(self.stations[toS].station_id)
        stationsId = result.pathTo(self.stations[toS].station_id)
        print(self.__convertToStationName(stationsId))

        return numStops

    # method for debuging
    def __convertToStationName(self, station_ids):
        output = []
        for station_id in station_ids:
            print(station_id)
            output += [self.stationNames[station_id]]
        return output
        
    
    
    
    def minDistance(self, fromS, toS):
        minDistance = -1.0
        # ADD YOUR CODE HERE
        result = DijkstraSP(self.graph, self.stations[fromS].station_id)
        minDistance = result.lengthTo(self.stations[toS].station_id)

        return minDistance
    
    
    
    
    def newRailwayLine(self, inputList):
        outputList = []
        # ADD YOUR CODE HERE

        
        return outputList


test = LondonRailwayMapper()

print(test.minStops("Abbey Road", "Abbey Wood"))
print(test.minStops("Baker Street", "North Wembley")) # should be 6

print(test.minDistance("Baker Street", "North Wembley"))

print(test.minDistance("Abbey Road", "Abbey Wood"))

# print(test.stationNames[0])
# print(test.stationNames[614])
# print(test.stationNames[94])
# print(test.stationNames[467])
# print(test.stationNames[150])
# print(test.stationNames[649])
# print(test.stationNames[1])