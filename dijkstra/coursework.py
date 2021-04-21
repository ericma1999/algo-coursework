import csv
from matplotlib import pyplot as plt


from AbstractClass import AbstractLondonRailwayMapper
from implementation.Edge import Edge
from implementation.Graph import Graph, TSPGraph
from implementation.BFS import BFS
from implementation.Dijkstra import DijkstraSP
from implementation.Harvenstein import harvensineDistance,euclidean_distance
from implementation.NearestNeighbor import NearestNeighbor
from implementation.TwoApprox import TwoApprox
from implementation.Bruteforce import BruteForce
from implementation.Bruteforce2 import BruteForce2
from implementation.Christofides import Christofides

class StationInfo:

    def __init__(self, station_id, name, lat, lng):
        self.station_id = station_id
        self.name = name
        self.lat = float(lat)
        self.lng = float(lng)
    
    def getName(self):
        return self.name

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
                self.stations[rowContent[0]] = StationInfo(id_counter, rowContent[0], rowContent[1], rowContent[2])
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

    def __useNearestNeighbor(self, graph):
        result = NearestNeighbor(graph)
        print(result.getPaths())
        print(result.getScore())

        return result.getPaths(), result.x, result.y

    def __useTwoApprox(self, graph):
        result = TwoApprox(graph)
        print(result.getPath())
        return result.getPath()

    def __useBruteForce(self, graph):
        result = BruteForce(graph)
        return result

    def __useBruteForce2(self, graph):
        result = BruteForce2(graph)
        return result.bestPath, result.x, result.y

    def __useChristofides(self, graph):
        result =  Christofides(graph).getPath()
        return result
    
    def newRailwayLine(self, inputList):
        outputList = []
        # ADD YOUR CODE HERE
        stations = []
        for stationName in inputList:
            stations.append(self.stations[stationName])

        newGraph = TSPGraph(len(inputList), stations)
        # path, x, y = self.__useChristofides(newGraph)
        path, x, y = self.__useNearestNeighbor(newGraph)

        print(x)
        print(y)

        print(path)


        # paths, x, y = self.__useTwoApprox(newGraph)
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])

        ax.plot(x,y, 'o-')
        plt.show()





        # print(self.__useBruteForce2(newGraph))

        # return self.__useNearestNeighbor(newGraph)
        # result = self.__useBruteForce(newGraph)
        # for id in result.best_path:
        #     print(newGraph.getStationName(id))


test = LondonRailwayMapper()

# test.newRailwayLine(['Abbey Road', 'Barbican', 'Bethnal Green', 'Cambridge Heath', 'Covent Garden', 'Dollis Hill', 'East Finchley', 'Finchley Road and Frognal', 'Great Portland Street', 'Hackney Wick', 'Isleworth', 'Kentish Town West', 'Leyton', 'Marble Arch', 'North Wembley', 'Old Street', 'Pimlico', 'Queens Park', 'Richmond', 'Shepherds Bush', 'Tottenham Hale', 'Uxbridge', 'Vauxhall', 'Wapping'])

test.newRailwayLine(["Queens Park", "Chigwell", "Moorgate", "Swiss Cottage", "Liverpool Street", "Highgate"])

# test.newRailwayLine(['Abbey Road', 'Barbican', 'Bethnal Green', 'Cambridge Heath', 'Covent Garden', 'Dollis Hill', 'East Finchley', 'Finchley Road and Frognal', 'Great Portland Street', 'Hackney Wick', 'Isleworth', 'Kentish Town West', 'Leyton', 'Marble Arch', 'North Wembley', 'Old Street', 'Pimlico', 'Queens Park', 'Richmond', 'Shepherds Bush', 'Tottenham Hale', 'Uxbridge', 'Vauxhall', 'Wapping'])

# test.newRailwayLine(['Finchley Central' , 'Tottenham Hale' , 'Stamford Hill' , 'Whitechapel' , 'Canada Water' , 'Borough' , 'Brixton' , 'Imperial Wharf' , 'Hackney Downs' , 'Alperton' , 'Kenton'])
# print(test.minStops("Abbey Road", "Abbey Wood"))
# print(test.minStops("Baker Street", "North Wembley")) # should be 6

# print(test.minDistance("Baker Street", "North Wembley"))

# print(test.minDistance("Abbey Road", "Abbey Wood"))

# print(test.stationNames[0])
# print(test.stationNames[614])
# print(test.stationNames[94])
# print(test.stationNames[467])
# print(test.stationNames[150])
# print(test.stationNames[649])
# print(test.stationNames[1])